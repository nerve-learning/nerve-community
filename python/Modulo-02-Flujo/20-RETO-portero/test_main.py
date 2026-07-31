"""test_main.py"""
import subprocess, sys, os
RETO = os.path.join(os.path.dirname(__file__), "reto.py")
def test_archivo_existe():
    assert os.path.exists(RETO)
def test_portero_rechaza_ropa_deportiva():
    r = subprocess.run([sys.executable, RETO], capture_output=True, text=True, timeout=15)
    assert r.returncode == 0, r.stderr
    assert "vestimenta" in r.stdout.lower(), \
        "Con ropa deportiva debe rechazar por código de vestimenta"
