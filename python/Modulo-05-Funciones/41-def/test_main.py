"""test_main.py"""
import subprocess, sys, os
BASE = os.path.dirname(__file__)
RETO = os.path.join(BASE, "reto.py")
def test_archivo_existe():
    assert os.path.exists(RETO)
def test_alerta_impresa_tres_veces():
    r = subprocess.run([sys.executable, RETO], capture_output=True, text=True, timeout=15)
    assert r.stdout.count("\n") >= 3, "La función debe llamarse al menos 3 veces"
