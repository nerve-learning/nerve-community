"""test_main.py — Evaluador automático: Analizador de Texto Simple."""
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


def test_cuenta_palabras_totales():
    """El output debe mostrar el conteo de palabras totales."""
    r = _run()
    stdout = r.stdout.lower()
    assert any(kw in stdout for kw in ["total", "palabras totales", "palabras:"]), (
        "El output debe mostrar el número total de palabras del texto"
    )


def test_cuenta_palabras_unicas():
    """El output debe mostrar palabras únicas."""
    r = _run()
    stdout = r.stdout.lower()
    assert any(kw in stdout for kw in ["única", "unica", "únicas", "unicas", "distintas"]), (
        "El output debe mostrar el conteo de palabras únicas"
    )


def test_muestra_palabra_mas_larga_y_corta():
    """El output debe mencionar la palabra más larga y la más corta."""
    r = _run()
    stdout = r.stdout.lower()
    assert any(kw in stdout for kw in ["más larga", "mas larga", "larga:"]), (
        "El output debe mostrar la palabra más larga"
    )
    assert any(kw in stdout for kw in ["más corta", "mas corta", "corta:"]), (
        "El output debe mostrar la palabra más corta"
    )


def test_muestra_top5_frecuentes():
    """El output debe mostrar las 5 palabras más frecuentes."""
    r = _run()
    stdout = r.stdout.lower()
    assert any(kw in stdout for kw in ["frecuentes", "frecuencia", "top 5", "top5", "más usadas"]), (
        "El output debe mostrar las 5 palabras más frecuentes"
    )


def test_clasifica_texto():
    """El output debe clasificar el texto como 'rico' o 'repetitivo'."""
    r = _run()
    stdout = r.stdout.lower()
    assert "rico" in stdout or "repetitivo" in stdout, (
        "El output debe clasificar el texto como 'rico' (>50% únicas) o 'repetitivo'"
    )


def test_texto_tiene_minimo_100_palabras():
    """El texto hardcoded en el código debe tener al menos 100 palabras."""
    codigo = _codigo()
    # Buscamos el string más largo en el código (el texto hardcoded)
    tree = ast.parse(codigo)
    strings = [
        node.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    ]
    max_palabras = max((len(s.split()) for s in strings), default=0)
    assert max_palabras >= 100, (
        f"El texto hardcoded en tu código debe tener al menos 100 palabras. "
        f"El más largo encontrado tiene {max_palabras} palabras."
    )


def test_usa_sets():
    """Restricción: debe usar sets para palabras únicas."""
    tree = ast.parse(_codigo())
    # Buscamos llamadas a set() o literales de set
    usa_set = any(
        (isinstance(n, ast.Call) and isinstance(getattr(n.func, "id", None) or object(), str) and n.func.id == "set")
        or isinstance(n, ast.Set)
        for n in ast.walk(tree)
    )
    assert usa_set, "Debes usar set() para almacenar palabras únicas (requisito del reto)"


def test_usa_diccionarios_para_frecuencias():
    """Restricción: debe usar diccionarios para contar frecuencias."""
    tree = ast.parse(_codigo())
    tiene_dict = any(isinstance(n, ast.Dict) for n in ast.walk(tree))
    assert tiene_dict, "Debes usar un diccionario {} para contar la frecuencia de palabras"


def test_no_usa_imports_prohibidos():
    """Restricción: no usar collections, pandas ni nltk."""
    codigo = _codigo()
    prohibidos = ["collections", "pandas", "nltk"]
    for lib in prohibidos:
        assert lib not in codigo, (
            f"No puedes usar '{lib}' en este reto (M03-M04)"
        )
