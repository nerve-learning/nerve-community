"""test_main.py"""
import subprocess, sys, os
BASE = os.path.dirname(__file__)
RETO = os.path.join(BASE, "reto.py")
def test_archivo_existe():
    assert os.path.exists(RETO)
def test_suite_completa():
    r = subprocess.run(
        [sys.executable, "-m", "pytest", "reto.py", "-v"],
        capture_output=True, text=True, cwd=BASE, timeout=30)
    assert r.returncode == 0, f"Fallaron:\n{r.stdout}\n{r.stderr}"
    assert "4 passed" in r.stdout, "Deben pasar exactamente 4 tests"
