"""test_main.py"""
import subprocess, sys, os
BASE = os.path.dirname(__file__)
RETO = os.path.join(BASE, "reto.py")
def test_archivo_existe():
    assert os.path.exists(RETO)
def test_microondas():
    r = subprocess.run([sys.executable, RETO], capture_output=True, text=True, timeout=10)
    assert r.returncode == 0, r.stderr
    assert "Comida lista" in r.stdout
    assert "A comer" in r.stdout
