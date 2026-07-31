"""test_main.py"""
import subprocess, sys, os
RETO = os.path.join(os.path.dirname(__file__), "reto.py")
def test_archivo_existe():
    assert os.path.exists(RETO)
def test_reporte_nocturno():
    r = subprocess.run([sys.executable, RETO], capture_output=True, text=True, timeout=15)
    assert "2,431" in r.stdout or "2431" in r.stdout
    assert "960" in r.stdout
    assert "4" in r.stdout
