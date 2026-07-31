"""test_main.py"""
import subprocess, sys, os
BASE = os.path.dirname(__file__)
def test_archivo_existe():
    assert os.path.exists(os.path.join(BASE, "test_reto.py")), "Debes crear test_reto.py"
def test_tests_del_alumno_pasan():
    r = subprocess.run(
        [sys.executable, "-m", "pytest", "test_reto.py", "-v"],
        capture_output=True, text=True, cwd=BASE, timeout=30)
    assert r.returncode == 0, f"Tus tests fallaron:\n{r.stdout}\n{r.stderr}"
