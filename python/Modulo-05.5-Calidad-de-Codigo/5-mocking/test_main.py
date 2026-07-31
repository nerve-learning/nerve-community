"""test_main.py"""
import subprocess, sys, os
BASE = os.path.dirname(__file__)
def test_archivo_existe():
    assert os.path.exists(os.path.join(BASE, "test_reto_mock.py"))
def test_mock_pasa():
    r = subprocess.run(
        [sys.executable, "-m", "pytest", "test_reto_mock.py", "-v"],
        capture_output=True, text=True, cwd=BASE, timeout=30)
    assert r.returncode == 0, f"Fallaron:\n{r.stdout}\n{r.stderr}"
