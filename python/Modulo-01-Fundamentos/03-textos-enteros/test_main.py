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
def test_imprime_texto_y_numero():
    r = run()
    tiene_numero = any(c.isdigit() for c in r.stdout)
    tiene_texto = any(c.isalpha() for c in r.stdout)
    assert tiene_numero and tiene_texto, "Debes imprimir texto y números"
