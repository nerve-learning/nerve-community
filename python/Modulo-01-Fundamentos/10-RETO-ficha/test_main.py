"""test_main.py — Evaluador automático del reto."""
import subprocess, sys, os
BASE = os.path.dirname(__file__)
RETO = os.path.join(BASE, "reto.py")
def run(stdin_data):
    return subprocess.run([sys.executable, RETO],
        input=stdin_data, capture_output=True, text=True, timeout=15)
def test_archivo_existe():
    assert os.path.exists(RETO), "Debes crear reto.py"
def test_ficha_completa():
    r = run("Gandalf\n10\n500\n")
    assert r.returncode == 0, f"Error:\n{r.stderr}"
    assert "Gandalf" in r.stdout, "La ficha debe mostrar el nombre del héroe"
    assert "150" in r.stdout, "El poder debe ser nivel × 15 = 150"
    assert "489" in r.stdout or "490" in r.stdout, \
        "El dinero debe ser 500 - 10.5 ≈ 489.5"
