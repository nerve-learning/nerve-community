"""test_main.py"""
import subprocess, sys, os
BASE = os.path.dirname(__file__)
def test_archivo_existe():
    assert os.path.exists(os.path.join(BASE, "test_reto_avanzado.py"))
def test_tests_avanzados_pasan():
    r = subprocess.run(
        [sys.executable, "-m", "pytest", "test_reto_avanzado.py", "-v"],
        capture_output=True, text=True, cwd=BASE, timeout=30)
    assert r.returncode == 0, f"Fallaron:\n{r.stdout}\n{r.stderr}"
    assert "3 passed" in r.stdout, "Deben pasar exactamente 3 tests"
