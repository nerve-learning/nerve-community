"""test_main.py — Evaluador automático: Sistema de Inventario con POO."""
import ast, subprocess, sys, os, json, tempfile, shutil

BASE = os.path.dirname(__file__)
RETO = os.path.join(BASE, "reto.py")


def _codigo():
    if os.path.exists(RETO):
        with open(RETO) as f:
            return f.read()
    return ""


def _run(env_cwd=None):
    return subprocess.run(
        [sys.executable, RETO],
        capture_output=True,
        text=True,
        timeout=15,
        cwd=env_cwd or BASE,
    )


def test_archivo_existe():
    assert os.path.exists(RETO), "Debes crear el archivo reto.py"


def test_codigo_valido():
    try:
        ast.parse(_codigo())
    except SyntaxError as e:
        assert False, f"Tu código tiene errores de sintaxis: {e}"


def test_sin_errores_de_ejecucion():
    r = _run()
    assert r.returncode == 0, f"El programa terminó con error:\n{r.stderr}"


def test_define_clase_producto():
    """El código debe definir una clase llamada Producto."""
    tree = ast.parse(_codigo())
    clases = [n.name for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
    assert "Producto" in clases, (
        f"Debes definir una clase llamada 'Producto'. Clases encontradas: {clases}"
    )


def test_define_clase_inventario():
    """El código debe definir una clase llamada Inventario."""
    tree = ast.parse(_codigo())
    clases = [n.name for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
    assert "Inventario" in clases, (
        f"Debes definir una clase llamada 'Inventario'. Clases encontradas: {clases}"
    )


def test_usa_herencia():
    """Restricción: al menos una clase debe heredar de otra."""
    tree = ast.parse(_codigo())
    clases_con_herencia = [
        n.name for n in ast.walk(tree)
        if isinstance(n, ast.ClassDef) and len(n.bases) > 0
    ]
    assert len(clases_con_herencia) >= 1, (
        "Debes usar herencia: al menos una clase debe heredar de otra "
        f"(ej: class ProductoPerecible(Producto))"
    )


def test_usa_property():
    """Restricción: al menos un @property en alguna clase."""
    tree = ast.parse(_codigo())
    funciones_con_property = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            for decorator in node.decorator_list:
                if isinstance(decorator, ast.Name) and decorator.id == "property":
                    funciones_con_property.append(node.name)
    assert len(funciones_con_property) >= 1, (
        f"Debes usar al menos un @property en tus clases. "
        f"Ninguno encontrado."
    )


def test_implementa_dunder_str():
    """Restricción: cada clase principal debe implementar __str__."""
    tree = ast.parse(_codigo())
    str_methods = [
        n.name for n in ast.walk(tree)
        if isinstance(n, ast.FunctionDef) and n.name == "__str__"
    ]
    assert len(str_methods) >= 2, (
        f"Debes implementar __str__ en al menos 2 clases. "
        f"Encontrados: {len(str_methods)}"
    )


def test_muestra_valor_total():
    """El output debe mostrar el valor total del inventario."""
    r = _run()
    stdout = r.stdout.lower()
    assert any(kw in stdout for kw in ["valor total", "total:", "total inventario", "valor inventario"]), (
        "El output debe mostrar el valor total del inventario"
    )


def test_alerta_stock_bajo():
    """El output debe mostrar algún tipo de alerta de stock bajo."""
    r = _run()
    stdout = r.stdout.lower()
    assert any(kw in stdout for kw in ["stock bajo", "alerta", "low stock", "pocas unidades", "agotando"]), (
        "El programa debe alertar cuando un producto tiene stock bajo"
    )


def test_persiste_datos_en_json():
    """Los datos deben persistir en un archivo JSON entre ejecuciones."""
    with tempfile.TemporaryDirectory() as tmpdir:
        shutil.copy(RETO, os.path.join(tmpdir, "reto.py"))
        _run(env_cwd=tmpdir)
        # Verificamos que se generó al menos un archivo JSON
        jsons = [f for f in os.listdir(tmpdir) if f.endswith(".json")]
        assert len(jsons) >= 1, (
            "El inventario debe persistirse en un archivo .json. "
            f"Archivos encontrados en el directorio de trabajo: {os.listdir(tmpdir)}"
        )


def test_no_usa_bases_de_datos():
    """Restricción: no usar sqlite3, sqlalchemy ni ORMs."""
    codigo = _codigo()
    for lib in ["sqlite3", "sqlalchemy", "peewee", "tortoise"]:
        assert lib not in codigo, f"No puedes usar '{lib}' en este reto"
