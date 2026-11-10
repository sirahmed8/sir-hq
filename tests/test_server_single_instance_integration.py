"""Integration test: two copies of serve-control-room.py, the second must exit.

Uses isolated SIR_OPS_DIR / SIR_CONTROL_PORT / SIR_CONTROL_MUTEX so the
live server on port 8899 is never touched.
"""
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


class TestServerSingleInstanceIntegration(unittest.TestCase):
    def test_two_processes_cant_start(self):
        """Start server in background, try to start second, verify second exits."""
        ops_dir = tempfile.mkdtemp(prefix="sir-ops-int-")
        port = free_port()
        env = os.environ.copy()
        env.update({
            "SIR_OPS_DIR": ops_dir,
            "SIR_CONTROL_PORT": str(port),
            "SIR_CONTROL_MUTEX": f"Global\\SIR_ControlRoom_TestInt_{os.getpid()}_{port}",
            "SIR_CONTROL_DISABLE_REFRESH": "1",
            "PYTHONUTF8": "1",
        })
        procs = []
        try:
            proc1 = subprocess.Popen(
                [sys.executable, SERVER], env=env,
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            )
            procs.append(proc1)
            self.assertTrue(wait_port(port), "first copy never started listening")

            # The scheduled task / dev-start.vbs path launches a fresh copy every
            # few minutes; that copy must refuse to run while this one is alive.
            proc2 = subprocess.Popen(
                [sys.executable, SERVER], env=env,
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            )
            procs.append(proc2)
            try:
                proc2.wait(timeout=20)
            except subprocess.TimeoutExpired:
                self.fail("second copy is still running: single-instance guard failed")
            self.assertEqual(proc2.returncode, 0)
            self.assertIsNone(proc1.poll(), "first copy must stay alive")

            # The port still answers, served by the surviving copy.
            self.assertTrue(wait_port(port))
        finally:
            for p in procs:
                if p.poll() is None:
                    p.terminate()
                    try:
                        p.wait(timeout=10)
                    except subprocess.TimeoutExpired:
                        p.kill()
            shutil.rmtree(ops_dir, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
