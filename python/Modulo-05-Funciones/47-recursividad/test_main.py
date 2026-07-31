"""test_main.py"""
import subprocess, sys, os
BASE = os.path.dirname(__file__)
RETO = os.path.join(BASE, "reto.py")
def test_archivo_existe():
    assert os.path.exists(RETO)
def test_eco_recursivo():
    r = subprocess.run([sys.executable, RETO], capture_output=True, text=True, timeout=15)
    assert r.stdout.count("¡Hola!") == 3, "La palabra debe repetirse 3 veces"
    assert "..." in r.stdout, "Debe terminar con '...'"
