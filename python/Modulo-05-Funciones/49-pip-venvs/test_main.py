"""test_main.py"""
import subprocess, sys, os
BASE = os.path.dirname(__file__)
RETO = os.path.join(BASE, "reto.py")
def test_archivo_existe():
    assert os.path.exists(RETO)
def test_pintor_corre():
    r = subprocess.run([sys.executable, RETO], capture_output=True, text=True, timeout=15)
    assert "ModuleNotFoundError" not in r.stderr or "colorama" in r.stderr
