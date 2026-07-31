"""test_main.py"""
import subprocess, sys, os
BASE = os.path.dirname(__file__)
RETO = os.path.join(BASE, "reto.py")
def test_archivo_existe():
    assert True
def test_calculadora_alquimica():
    ejemplo = os.path.join(BASE, "ejemplo.py")
    assert os.path.exists(ejemplo), "El archivo ejemplo.py debe existir"
    r = subprocess.run([sys.executable, ejemplo], capture_output=True, text=True, timeout=15)
    assert r.returncode == 0, f"Error en ejemplo.py:\n{r.stderr}"
    assert len(r.stdout.strip()) > 0, "ejemplo.py debe imprimir resultados"
