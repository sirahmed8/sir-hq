import io
import json
import sys
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).parent))
import telegram_lib  # noqa: E402
from telegram_lib import TelegramBot, TelegramError, escape_html  # noqa: E402


def fake_response(payload, status=200):
    raw = json.dumps(payload).encode("utf-8")

    class R:
        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

        def read(self):
            return raw

    return R()


class FakeOpener:
    """Records requests; replays queued (payload, status) or exceptions."""

    def __init__(self, script):
        self.script = list(script)
        self.requests = []

    def __call__(self, req, timeout=60):
        self.requests.append(req)
        item = self.script.pop(0)
        if isinstance(item, Exception):
            raise item
        payload, status = item if isinstance(item, tuple) else (item, 200)
        if status >= 400:
            import urllib.error
            raise urllib.error.HTTPError(req.full_url, status, "err", {}, io.BytesIO(json.dumps(payload).encode()))
        return fake_response(payload)


OK = ({"ok": True, "result": {"message_id": 1}}, 200)


class LibTests(unittest.TestCase):
    def test_escape_html(self):
        self.assertEqual(escape_html('a<b>&"c"'), 'a&lt;b&gt;&amp;"c"')

    def test_send_message_shape(self):
        op = FakeOpener([OK])
        tg = TelegramBot("T", "C", opener=op)
        r = tg.send_message("hello")
        self.assertEqual(r["message_id"], 1)
        body = json.loads(op.requests[0].data.decode())
        self.assertEqual(body["chat_id"], "C")
        self.assertEqual(body["text"], "hello")
        self.assertTrue(op.requests[0].full_url.endswith("/botT/sendMessage"))

    def test_edit_message_text(self):
        op = FakeOpener([OK])
        tg = TelegramBot("T", "C", opener=op)
        tg.edit_message_text(7, "final")
        body = json.loads(op.requests[0].data.decode())
        self.assertEqual(body["message_id"], 7)

    def test_reaction(self):
        op = FakeOpener([({"ok": True, "result": True}, 200)])
        tg = TelegramBot("T", "C", opener=op)
        tg.set_message_reaction(9, "🔥")
        body = json.loads(op.requests[0].data.decode())
        self.assertEqual(body["reaction"], [{"type": "emoji", "emoji": "🔥"}])

    def test_retry_on_http_500(self):
        op = FakeOpener([
            ({"ok": False, "error_code": 500, "description": "boom"}, 500),
            OK,
        ])
        tg = TelegramBot("T", "C", opener=op, retries=2)
        with mock.patch.object(telegram_lib.time, "sleep"):
            r = tg.send_message("hi")
        self.assertEqual(r["message_id"], 1)
        self.assertEqual(len(op.requests), 2)

    def test_400_raises(self):
        op = FakeOpener([({"ok": False, "error_code": 400, "description": "chat not found"}, 400)])
        tg = TelegramBot("T", "C", opener=op, retries=0)
        with self.assertRaises(TelegramError) as cm:
            tg.send_message("hi")
        self.assertIn("chat not found", str(cm.exception))

    def test_api_error_result_raises(self):
        op = FakeOpener([{"ok": False, "error_code": 403, "description": "Forbidden"}])
        tg = TelegramBot("T", "C", opener=op, retries=0)
        with self.assertRaises(TelegramError):
            tg.send_message("hi")

    def test_multipart_document(self):
        op = FakeOpener([OK])
        tg = TelegramBot("T", "C", opener=op)
        tmp = Path(self._tmp.name)
        tg.send_document(tmp, caption="cap")
        req = op.requests[0]
        self.assertIn(b"multipart/form-data", req.headers.get("Content-type", b"").encode() if isinstance(req.headers.get("Content-type"), str) else req.headers.get("Content-type"))
        self.assertIn(b"hello-doc", req.data)

    def setUp(self):
        import tempfile
        self._tmp = tempfile.NamedTemporaryFile(suffix=".txt", delete=False)
        self._tmp.write(b"hello-doc")
        self._tmp.close()

    def tearDown(self):
        Path(self._tmp.name).unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
