"""test_main.py — Evaluador automático: Scraper de Tablas Útiles (nerve.community.aleniastudios.me)."""
import ast, subprocess, sys, os, json

BASE = os.path.dirname(__file__)
RETO = os.path.join(BASE, "reto.py")
DATOS_JSON = os.path.join(BASE, "datos.json")


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
        timeout=60,  # Más tiempo para scraping de red
        cwd=BASE,
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


def test_genera_datos_json():
    """El programa debe generar un archivo datos.json."""
    if os.path.exists(DATOS_JSON):
        os.remove(DATOS_JSON)
    r = _run()
    assert os.path.exists(DATOS_JSON), (
        f"El programa debe generar 'datos.json'. Stderr:\n{r.stderr}"
    )


def test_datos_json_es_valido():
    """El datos.json debe ser JSON válido y no estar vacío."""
    if not os.path.exists(DATOS_JSON):
        _run()
    assert os.path.exists(DATOS_JSON), "datos.json no existe"
    with open(DATOS_JSON, encoding="utf-8") as f:
        contenido = f.read().strip()
    assert len(contenido) > 10, "datos.json está vacío"
    try:
        datos = json.loads(contenido)
    except json.JSONDecodeError as e:
        assert False, f"datos.json no es JSON válido: {e}"
    assert isinstance(datos, (list, dict)), "datos.json debe ser una lista o diccionario JSON"
    # Si es lista, debe tener al menos una fila de datos
    if isinstance(datos, list):
        assert len(datos) >= 1, "datos.json debe contener al menos un registro"


TARGET_URL = "nerve.community.aleniastudios.me"
TARGET_URL_FULL = "https://nerve.community.aleniastudios.me"


def test_apunta_a_nerve_community():
    """El código debe hacer scraping de nerve.community.aleniastudios.me."""
    codigo = _codigo()
    assert TARGET_URL in codigo, (
        f"Tu scraper debe apuntar a '{TARGET_URL_FULL}'. "
        "Ese es el objetivo del reto, no Wikipedia ni otra URL."
    )


def test_usa_beautifulsoup():
    """Restricción: debe usar BeautifulSoup."""
    codigo = _codigo()
    assert "BeautifulSoup" in codigo or "beautifulsoup" in codigo.lower() or "bs4" in codigo, (
        "Debes usar BeautifulSoup (bs4) para extraer la tabla de la web"
    )


def test_define_al_menos_una_clase():
    """Restricción: al menos una clase para representar los datos."""
    tree = ast.parse(_codigo())
    clases = [n.name for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
    assert len(clases) >= 1, (
        f"Debes definir al menos una clase para representar los datos scrapeados. "
        f"Clases encontradas: {clases}"
    )


def test_no_usa_pandas_ni_selenium():
    """Restricción: no usar pandas ni selenium."""
    codigo = _codigo()
    assert "pandas" not in codigo, "No puedes usar pandas en este reto (M07-M08)"
    assert "selenium" not in codigo, "No puedes usar selenium en este reto (M07-M08)"


def test_permite_filtrado():
    """El programa debe incluir lógica de filtrado por columna/valor."""
    tree = ast.parse(_codigo())
    # Buscamos funciones cuyo nombre sugiera filtrado
    funciones = [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
    nombres_filtro = [f for f in funciones if any(
        kw in f.lower() for kw in ["filtr", "filter", "buscar", "search", "find"]
    )]
    # También aceptamos que haya list comprehensions con condición if (filtro inline)
    comps_con_if = [
        n for n in ast.walk(tree)
        if isinstance(n, (ast.ListComp, ast.GeneratorExp))
        and any(isinstance(g, ast.comprehension) and g.ifs for g in n.generators)
    ]
    assert len(nombres_filtro) >= 1 or len(comps_con_if) >= 1, (
        "Tu programa debe incluir lógica para filtrar la tabla "
        "(una función de filtrado o una list comprehension con condición)"
    )
