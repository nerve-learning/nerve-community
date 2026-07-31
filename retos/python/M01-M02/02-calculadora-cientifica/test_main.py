"""test_main.py — Evaluador automático: Calculadora Científica Básica."""
import ast, subprocess, sys, os, re

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


def test_tres_calculos_distintos():
    """El output debe mostrar al menos 3 bloques o líneas de resultado."""
    r = _run()
    lineas_con_numero = [
        l for l in r.stdout.strip().splitlines()
        if re.search(r"\d+\.\d{2}", l)  # líneas que muestran números con 2 decimales
    ]
    assert len(lineas_con_numero) >= 3, (
        f"Se esperan al menos 3 resultados formateados con 2 decimales. "
        f"Encontrados: {len(lineas_con_numero)}"
    )


def test_resultados_con_dos_decimales():
    """Todos los resultados numéricos deben tener exactamente 2 decimales."""
    r = _run()
    numeros = re.findall(r"\d+\.\d+", r.stdout)
    assert len(numeros) >= 3, (
        "Debes mostrar al menos 3 resultados con formato decimal (ej: 12.34)"
    )
    for n in numeros:
        decimales = len(n.split(".")[1])
        assert decimales == 2, (
            f"El número '{n}' debe tener exactamente 2 decimales, tiene {decimales}"
        )


def test_calcula_velocidad():
    """El output debe mencionar velocidad (v, vel o velocidad)."""
    r = _run()
    assert any(
        kw in r.stdout.lower() for kw in ["velocidad", " vel", "v =", "v="]
    ), "El output debe mostrar el cálculo de velocidad (v = d/t)"


def test_calcula_fuerza():
    """El output debe mencionar fuerza (f, fuerza o newton)."""
    r = _run()
    assert any(
        kw in r.stdout.lower() for kw in ["fuerza", "newton", "f =", "f="]
    ), "El output debe mostrar el cálculo de fuerza (F = m*a)"


def test_calcula_energia():
    """El output debe mencionar energía cinética."""
    r = _run()
    assert any(
        kw in r.stdout.lower() for kw in ["energía", "energia", "cinética", "cinetica", "ec", "joule"]
    ), "El output debe mostrar el cálculo de energía cinética (Ec = 0.5*m*v²)"


def test_no_usa_funciones():
    """Restricción del reto: no definir funciones (def)."""
    tree = ast.parse(_codigo())
    funciones = [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
    assert len(funciones) == 0, (
        f"No puedes definir funciones en este reto. "
        f"Encontradas: {[f.name for f in funciones]}"
    )


def test_no_usa_import():
    """Restricción del reto: no usar import."""
    tree = ast.parse(_codigo())
    imports = [n for n in ast.walk(tree) if isinstance(n, (ast.Import, ast.ImportFrom))]
    assert len(imports) == 0, (
        "No puedes usar import en este reto (M01-M02). "
        "Usa solo operadores aritméticos y variables."
    )


def test_usa_fstrings():
    """El código debe usar f-strings para formatear los resultados."""
    codigo = _codigo()
    count = codigo.count("f\"") + codigo.count("f'")
    assert count >= 3, (
        f"Debes usar f-strings para mostrar los resultados. "
        f"Se detectaron: {count}"
    )
