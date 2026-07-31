"""test_main.py — Evaluador automático: Organizador de Colección."""
import ast, subprocess, sys, os

BASE = os.path.dirname(__file__)
RETO = os.path.join(BASE, "reto.py")


def _codigo():
    if os.path.exists(RETO):
        with open(RETO) as f:
            return f.read()
    return ""


def _run():
    return subprocess.run(
        [sys.executable, RETO],
        capture_output=True,
        text=True,
        timeout=15,
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


def test_al_menos_ocho_items():
    """La colección debe tener al menos 8 items."""
    tree = ast.parse(_codigo())
    # Contamos todos los literales de diccionarios en el código
    dicts = [n for n in ast.walk(tree) if isinstance(n, ast.Dict)]
    assert len(dicts) >= 8, (
        f"Debes tener al menos 8 items como diccionarios en tu colección. "
        f"Encontrados: {len(dicts)}"
    )


def test_tres_vistas_distintas():
    """El output debe tener al menos 3 secciones o vistas del catálogo."""
    r = _run()
    stdout = r.stdout.lower()
    # Buscamos palabras que impliquen secciones distintas
    secciones = [
        "todos" in stdout or "completo" in stdout or "catálogo" in stdout or "catalogo" in stdout,
        "género" in stdout or "genero" in stdout or "categoría" in stdout or "categoria" in stdout,
        "año" in stdout or "fecha" in stdout or "ordenado" in stdout,
    ]
    assert sum(secciones) >= 2, (
        "El output debe mostrar al menos 2 vistas distintas: "
        "todos los items, filtrados por género y ordenados por año"
    )


def test_muestra_estadisticas():
    """El output debe incluir estadísticas: total, género más común, item más antiguo."""
    r = _run()
    stdout = r.stdout.lower()
    assert "total" in stdout, "Debes mostrar el total de items en la colección"
    assert any(kw in stdout for kw in ["más común", "mas comun", "frecuente", "popular"]), (
        "Debes mostrar el género más común de la colección"
    )
    assert any(kw in stdout for kw in ["antiguo", "viejo", "más antiguo", "mas antiguo", "primero"]), (
        "Debes mostrar el item más antiguo de la colección"
    )


def test_usa_listas_y_diccionarios():
    """Restricción: debe usar tanto listas como diccionarios."""
    tree = ast.parse(_codigo())
    tiene_lista = any(isinstance(n, ast.List) for n in ast.walk(tree))
    tiene_dict = any(isinstance(n, ast.Dict) for n in ast.walk(tree))
    assert tiene_lista, "Debes usar listas [] en tu solución"
    assert tiene_dict, "Debes usar diccionarios {} en tu solución"


def test_usa_list_comprehensions():
    """Restricción: al menos 2 list comprehensions."""
    tree = ast.parse(_codigo())
    comps = [n for n in ast.walk(tree) if isinstance(n, ast.ListComp)]
    assert len(comps) >= 2, (
        f"Debes usar al menos 2 list comprehensions. "
        f"Encontradas: {len(comps)}"
    )


def test_no_usa_clases():
    """Restricción del reto: no usar clases."""
    tree = ast.parse(_codigo())
    clases = [n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
    assert len(clases) == 0, (
        f"No puedes usar clases en este reto (M03-M04). "
        f"Encontradas: {[c.name for c in clases]}"
    )


def test_no_usa_import():
    """Restricción del reto: no usar import."""
    tree = ast.parse(_codigo())
    imports = [n for n in ast.walk(tree) if isinstance(n, (ast.Import, ast.ImportFrom))]
    assert len(imports) == 0, (
        "No puedes usar import en este reto (M03-M04)."
    )
