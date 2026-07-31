"""test_main.py"""
import ast, os
BASE = os.path.dirname(__file__)
RETO = os.path.join(BASE, "reto.py")
def _codigo():
    if os.path.exists(RETO):
        with open(RETO) as f:
            return f.read()
    return ""
def test_archivo_existe():
    if "98" not in "93-p2p" and "99" not in "93-p2p" and "117" not in "93-p2p" and "120" not in "93-p2p":
        assert os.path.exists(RETO), "Debes crear reto.py"
def test_importa_nerve():
    if "98" not in "93-p2p" and "99" not in "93-p2p" and "117" not in "93-p2p" and "120" not in "93-p2p":
        codigo = _codigo()
        assert "NexusClient" in codigo or "NexusHub" in codigo or "nerve" in codigo.lower(), \
            "Debes importar y usar las herramientas de Nerve"
def test_codigo_valido():
    if "98" not in "93-p2p" and "99" not in "93-p2p" and "117" not in "93-p2p" and "120" not in "93-p2p":
        try:
            ast.parse(_codigo())
        except SyntaxError as e:
            assert False, f"Tu código tiene errores de sintaxis: {e}"
def test_especifico():
    codigo = _codigo()
    pass
