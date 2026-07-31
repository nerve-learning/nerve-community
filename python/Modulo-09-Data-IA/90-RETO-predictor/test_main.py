"""test_main.py"""
import ast, os, sys
import subprocess
BASE = os.path.dirname(__file__)
RETO = os.path.join(BASE, "reto.py")
def _parse():
    with open(RETO) as f:
        return ast.parse(f.read())
def test_archivo_existe():
    assert os.path.exists(RETO), "Debes crear reto.py"
def test_logica_datos():
    with open(RETO) as f:
        codigo = f.read()
    tree = ast.parse(codigo)
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports += [a.name for a in node.names]
        if isinstance(node, ast.ImportFrom):
            imports.append(node.module)
    r = subprocess.run([sys.executable, RETO], capture_output=True, text=True, timeout=15); assert "240" in r.stdout
