"""test_main.py"""
import subprocess, sys, os
RETO = os.path.join(os.path.dirname(__file__), "reto.py")
def test_archivo_existe():
    assert os.path.exists(RETO)
def test_turnos_generados():
    r = subprocess.run([sys.executable, RETO], capture_output=True, text=True, timeout=15)
    assert "turno: 1" in r.stdout
    assert "turno: 5" in r.stdout
