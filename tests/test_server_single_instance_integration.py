"""Test that the server refuses to start a second instance (integration test)."""
import unittest
import os
import sys
import tempfile
import subprocess
import time
import shutil


class TestServerSingleInstanceIntegration(unittest.TestCase):
    def test_two_processes_cant_start(self):
        """Start server in background, try to start second, verify second exits."""
        server_script = os.path.join(os.path.dirname(__file__), "..", "scripts", "serve-control-room.py")
        python_exe = sys.executable
        
        # Use a temporary lock file path to avoid conflicts
        test_dir = tempfile.mkdtemp()
        lock_file = os.path.join(test_dir, "control-room.lock")
        
        try:
            # Modify environment to use test lock file
            env = os.environ.copy()
            env["SIR_OPS"] = test_dir
            env["SIR_TEST_MODE"] = "1"
            
            # Start first server process in background (it will hold the lock)
            # We run a script that acquires the lock and then waits
            proc1 = subprocess.Popen([
                python_exe, "-c", f"""
import sys
import time
sys.path.insert(0, r'{os.path.dirname(server_script)}')
import importlib.util
spec = importlib.util.spec_from_file_location('serve_control_room', r'{server_script}')
mod = importlib.util.module_from_spec(spec)
sys.modules['serve_control_room'] = mod
spec.loader.exec_module(mod)

# Override lock file path
mod.LOCK_FILE = r'{lock_file}'
mod.INSTANCE_LOCK_FH = None
mod.INSTANCE_MUTEX = None

result = mod.take_instance_lock()
print('PROC1_GOT_LOCK=' + str(result), file=sys.__stdout__)
sys.__stdout__.flush()

if result:
    # Hold the lock for a while
    time.sleep(5)
    mod.release_instance_lock()
    print('PROC1_RELEASED', file=sys.__stdout__)
    sys.__stdout__.flush()
"""
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=env)
            
            # Give proc1 time to acquire the lock
            time.sleep(1)
            
            # Try to start second process - should fail to get lock
            result2 = subprocess.run([
                python_exe, "-c", f"""
import sys
sys.path.insert(0, r'{os.path.dirname(server_script)}')
import importlib.util
spec = importlib.util.spec_from_file_location('serve_control_room', r'{server_script}')
mod = importlib.util.module_from_spec(spec)
sys.modules['serve_control_room'] = mod
spec.loader.exec_module(mod)

# Override lock file path
mod.LOCK_FILE = r'{lock_file}'
mod.INSTANCE_LOCK_FH = None
mod.INSTANCE_MUTEX = None

result = mod.take_instance_lock()
print('PROC2_GOT_LOCK=' + str(result), file=sys.__stdout__)
sys.__stdout__.flush()
"""
            ], capture_output=True, text=True, timeout=10, env=env)
            
            combined2 = result2.stdout + result2.stderr
            print("PROC2 OUTPUT:", combined2)
            self.assertEqual(result2.returncode, 0)
            self.assertIn("PROC2_GOT_LOCK=False", combined2)
            
            # Wait for proc1 to finish
            proc1.wait(timeout=10)
            out1, err1 = proc1.communicate()
            print("PROC1 OUTPUT:", out1 + err1)
            self.assertIn("PROC1_GOT_LOCK=True", out1 + err1)
            
        finally:
            # Cleanup
            shutil.rmtree(test_dir, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()