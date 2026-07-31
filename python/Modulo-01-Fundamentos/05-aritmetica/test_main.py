"""test_main.py — Evaluador automático del reto."""
import subprocess, sys, os
BASE = os.path.dirname(__file__)
RETO = os.path.join(BASE, "reto.py")
def run():
    return subprocess.run([sys.executable, RETO],
        capture_output=True, text=True, timeout=15)
def test_archivo_existe():
    assert os.path.exists(RETO), "Debes crear reto.py"
def test_sin_errores():
    r = run()
    assert r.returncode == 0, f"Error:\n{r.stderr}"
def test_resultado_correcto():
    r = run()
    assert "1250" in r.stdout, "El costo total debe ser 1250.0"
