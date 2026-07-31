"""test_main.py — Evaluador automático del reto."""
import subprocess, sys, os
BASE = os.path.dirname(__file__)
RETO = os.path.join(BASE, "reto.py")
def run(stdin_data):
    return subprocess.run([sys.executable, RETO],
        input=stdin_data, capture_output=True, text=True, timeout=15)
def test_archivo_existe():
    assert os.path.exists(RETO), "Debes crear reto.py"
def test_f_string_con_nombre():
    r = run("Carlos\n30\n")
    assert r.returncode == 0, f"Error:\n{r.stderr}"
    assert "Carlos" in r.stdout, "El f-string debe incluir el nombre ingresado"
