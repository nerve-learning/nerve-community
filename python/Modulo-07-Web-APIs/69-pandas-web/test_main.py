"""test_main.py"""
import ast, os, sys
BASE = os.path.dirname(__file__)
RETO = os.path.join(BASE, "reto.py")
def _parse():
    with open(RETO) as f:
        return ast.parse(f.read())
def _codigo():
    with open(RETO) as f:
        return f.read()
def test_archivo_existe():
    assert os.path.exists(RETO), "Debes crear reto.py"
def test_importa_requests():
    tree = _parse()
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports += [a.name for a in node.names]
        if isinstance(node, ast.ImportFrom):
            imports.append(node.module)
    assert "requests" in imports or "bs4" in imports or "selenium" in imports or "aiohttp" in imports, \
        "Debes importar la librería correspondiente al nivel"
def test_especifico():
    code = _codigo()
    tree = _parse()
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports += [a.name for a in node.names]
        if isinstance(node, ast.ImportFrom):
            imports.append(node.module)
    assert "svg" in code
