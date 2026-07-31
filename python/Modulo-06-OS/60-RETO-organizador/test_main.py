"""test_main.py"""
import subprocess, sys, os
BASE = os.path.dirname(__file__)
RETO = os.path.join(BASE, "reto.py")
def test_archivo_existe():
    assert os.path.exists(RETO)
def test_organizador():
    ejemplo = os.path.join(BASE, "ejemplo.py")
    if os.path.exists(ejemplo):
        subprocess.run([sys.executable, ejemplo], cwd=BASE, timeout=15)
    r = subprocess.run([sys.executable, RETO], capture_output=True, text=True, cwd=BASE, timeout=15)
    assert r.returncode == 0, r.stderr
