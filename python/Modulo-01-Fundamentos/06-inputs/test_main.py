"""test_main.py — Evaluador automático del reto."""
import subprocess, sys, os
BASE = os.path.dirname(__file__)
RETO = os.path.join(BASE, "reto.py")
def run(stdin_data):
    return subprocess.run([sys.executable, RETO],
        input=stdin_data, capture_output=True, text=True, timeout=15)
def test_archivo_existe():
    assert os.path.exists(RETO), "Debes crear reto.py"
def test_acepta_input_y_responde():
    r = run("Ana\nTierra\n")
    assert r.returncode == 0, f"Error:\n{r.stderr}"
    assert "Ana" in r.stdout, "Debes mostrar el nombre ingresado"
    assert "Tierra" in r.stdout, "Debes mostrar el planeta ingresado"
