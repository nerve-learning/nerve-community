"""test_main.py"""
import subprocess, sys, os
BASE = os.path.dirname(__file__)
RETO = os.path.join(BASE, "reto.py")
def test_archivo_existe():
    assert os.path.exists(RETO)
def test_carrera():
    r = subprocess.run([sys.executable, RETO], capture_output=True, text=True, timeout=10)
    assert r.returncode == 0, r.stderr
    assert "Rayo" in r.stdout and "Tortuga" in r.stdout
    assert "terminado" in r.stdout.lower()
