"""test_main.py"""
import subprocess, sys, os
RETO = os.path.join(os.path.dirname(__file__), "reto.py")
def test_archivo_existe():
    assert os.path.exists(RETO)
def test_sin_errores():
    r = subprocess.run([sys.executable, RETO], capture_output=True, text=True, timeout=15)
    assert r.returncode == 0, r.stderr
def test_output():
    r = subprocess.run([sys.executable, RETO], capture_output=True, text=True, timeout=15)
    if "11-" in RETO or "12-" in RETO:
        assert "True" in r.stdout or "False" in r.stdout
    else:
        assert len(r.stdout.strip()) > 0
