"""Test that the control room server refuses to start a second instance.

Spawns real `scripts/serve-control-room.py` processes with isolated
SIR_OPS_DIR / SIR_CONTROL_PORT / SIR_CONTROL_MUTEX so the test never
touches the live server on port 8899.
"""
import json
import os
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SERVER = os.path.normpath(os.path.join(HERE, "..", "scripts", "serve-control-room.py"))


def free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def wait_port(port: int, timeout: float = 20.0) -> bool:
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=1):
                return True
        except OSError:
            time.sleep(0.25)
    return False


class ServerInstanceCase(unittest.TestCase):
    def setUp(self):
        self.ops_dir = tempfile.mkdtemp(prefix="sir-ops-")
        self.port = free_port()
        self.mutex = f"Global\\SIR_ControlRoom_Test_{os.getpid()}_{self.port}"
        self.env = os.environ.copy()
        self.env.update({
            "SIR_OPS_DIR": self.ops_dir,
            "SIR_CONTROL_PORT": str(self.port),
            "SIR_CONTROL_MUTEX": self.mutex,
            "SIR_CONTROL_DISABLE_REFRESH": "1",
            "PYTHONUTF8": "1",
        })
        self.procs = []

    def tearDown(self):
        for p in self.procs:
            if p.poll() is None:
                p.terminate()
                try:
                    p.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    p.kill()
        shutil.rmtree(self.ops_dir, ignore_errors=True)

    def start_server(self) -> subprocess.Popen:
        proc = subprocess.Popen(
            [sys.executable, SERVER],
            env=self.env,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        self.procs.append(proc)
        return proc


class TestServerSingleInstance(ServerInstanceCase):
    def test_first_instance_starts_and_second_exits(self):
        first = self.start_server()
        self.assertTrue(wait_port(self.port), "first instance did not start listening")

        second = self.start_server()
        try:
            second.wait(timeout=20)
        except subprocess.TimeoutExpired:
            self.fail("second instance did not exit while the first holds the lock")
        self.assertEqual(second.returncode, 0, "second instance should exit cleanly")
        self.assertIsNone(first.poll(), "first instance must keep running")

    def test_new_instance_allowed_after_first_stops(self):
        first = self.start_server()
        self.assertTrue(wait_port(self.port), "first instance did not start listening")
        first.terminate()
        first.wait(timeout=10)

        second = self.start_server()
        try:
            self.assertTrue(wait_port(self.port), "new instance did not take over the port")
            time.sleep(1.5)
            self.assertIsNone(second.poll(), "new instance exited even though the lock was free")
        finally:
            if second.poll() is None:
                second.terminate()


if __name__ == "__main__":
    unittest.main()
