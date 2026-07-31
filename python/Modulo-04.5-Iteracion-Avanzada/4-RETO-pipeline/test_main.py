"""test_main.py"""
import subprocess, sys, os
RETO = os.path.join(os.path.dirname(__file__), "reto.py")
def test_archivo_existe():
    assert os.path.exists(RETO)
def test_pipeline_deportes():
    r = subprocess.run([sys.executable, RETO], capture_output=True, text=True, timeout=15)
    assert "DEPORTES" in r.stdout
    assert "publicada" in r.stdout.lower()
    assert "4" in r.stdout
