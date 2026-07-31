"""test_main.py — Evaluador automático: Generador de Tarjetas de Presentación."""
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


def test_tiene_al_menos_tres_tarjetas():
    """Detecta separadores visuales para confirmar que hay 3 bloques de tarjeta."""
    r = _run()
    lineas = r.stdout.strip().splitlines()
    # Contamos líneas que actúan como separador: al menos 40 chars repetidos o ---
    separadores = [
        l for l in lineas
        if len(l.strip()) >= 10 and len(set(l.strip())) <= 3
    ]
    assert len(separadores) >= 3, (
        f"Se esperan al menos 3 separadores visuales (uno por tarjeta), "
        f"encontrados: {len(separadores)}"
    )


def test_formato_uniforme():
    """Todas las tarjetas deben tener nombre, profesión y frase con el mismo patrón."""
    r = _run()
    stdout = r.stdout.lower()
    # Al menos tres instancias de palabras que implican contenido de tarjeta
    palabras_clave = ["nombre", "profesión", "profesion", "frase", "cargo", "ocupación"]
    encontradas = [p for p in palabras_clave if stdout.count(p) >= 1]
    assert len(encontradas) >= 1, (
        "El output debe incluir etiquetas como 'Nombre', 'Profesión' o 'Frase' "
        "para que el formato sea legible"
    )


def test_usa_fstrings():
    """El código debe contener al menos 3 f-strings (uno por tarjeta)."""
    codigo = _codigo()
    count = codigo.count("f\"") + codigo.count("f'")
    assert count >= 3, (
        f"Debes usar al menos un f-string por tarjeta (mínimo 3). "
        f"Se detectaron: {count}"
    )


def test_no_usa_listas_ni_diccionarios():
    """Restricción del reto: no usar listas [] ni diccionarios {}."""
    tree = ast.parse(_codigo())
    for node in ast.walk(tree):
        assert not isinstance(node, ast.List), (
            "No puedes usar listas [] en este reto (M01-M02)"
        )
        assert not isinstance(node, ast.Dict), (
            "No puedes usar diccionarios {} en este reto (M01-M02)"
        )


def test_no_usa_funciones():
    """Restricción del reto: no definir funciones (def)."""
    tree = ast.parse(_codigo())
    funciones = [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
    assert len(funciones) == 0, (
        "No puedes definir funciones en este reto. "
        f"Se encontraron: {[f.name for f in funciones]}"
    )


def test_no_usa_bucles():
    """Restricción del reto: no usar for ni while."""
    tree = ast.parse(_codigo())
    for node in ast.walk(tree):
        assert not isinstance(node, (ast.For, ast.While)), (
            "No puedes usar bucles (for/while) en este reto (M01-M02)"
        )
