"""test_main.py"""
import subprocess, sys, os
BASE = os.path.dirname(__file__)
RETO = os.path.join(BASE, "reto.py")
def test_archivo_existe():
    assert os.path.exists(RETO)
def test_scope_global():
    r = subprocess.run([sys.executable, RETO], capture_output=True, text=True, timeout=15)
    assert "30" in r.stdout, "El oro restante debe ser 30"
