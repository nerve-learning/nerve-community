"""test_main.py"""
import subprocess, sys, os
BASE = os.path.dirname(__file__)
RETO = os.path.join(BASE, "reto.py")
def test_archivo_existe():
    assert os.path.exists(RETO)
def test_crea_diario():
    r = subprocess.run([sys.executable, RETO], capture_output=True, text=True, cwd=BASE, timeout=15)
    assert r.returncode == 0, r.stderr
    assert os.path.exists(os.path.join(BASE, "diario.txt")), "Debe crear el archivo diario.txt"
