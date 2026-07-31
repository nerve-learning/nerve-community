"""test_main.py — Evaluador automático del reto."""
import subprocess, sys, os
BASE = os.path.dirname(__file__)
RETO = os.path.join(BASE, "reto.py")
def run():
    return subprocess.run([sys.executable, RETO],
        capture_output=True, text=True, timeout=15)
def test_archivo_existe():
    assert os.path.exists(RETO), "Debes crear reto.py"
def test_imprime_algo():
    r = run()
    assert r.returncode == 0, f"Error:\n{r.stderr}"
    assert len(r.stdout.strip()) > 0, "Tu programa no imprime nada"
def test_contiene_separador_visual():
    r = run()
    assert "---" in r.stdout or "===" in r.stdout, \
        "Debe contener un separador visual (--- o ===)"
