"""test_main.py"""
import subprocess, sys, os
BASE = os.path.dirname(__file__)
RETO = os.path.join(BASE, "reto.py")
def test_archivo_existe():
    assert os.path.exists(RETO)
def test_lambdas():
    r = subprocess.run([sys.executable, RETO], capture_output=True, text=True, timeout=15)
    assert "25" in r.stdout, "El cuadrado de 5 es 25"
    assert "20.0" in r.stdout, "El área del triángulo (base 10, altura 4) es 20.0"
