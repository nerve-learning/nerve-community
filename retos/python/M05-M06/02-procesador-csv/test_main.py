"""test_main.py — Evaluador automático: Procesador de CSV."""
import ast, subprocess, sys, os, csv, tempfile, shutil

BASE = os.path.dirname(__file__)
RETO = os.path.join(BASE, "reto.py")
REPORTE_CSV = os.path.join(BASE, "reporte_limpio.csv")


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
        timeout=60,  # Más tiempo porque hace una descarga de red
        cwd=env_cwd or BASE,
    )


def test_archivo_existe():
    assert os.path.exists(RETO), "Debes crear el archivo reto.py"


def test_codigo_valido():
    try:
        ast.parse(_codigo())
    except SyntaxError as e:
        assert False, f"Tu código tiene errores de sintaxis: {e}"


def test_al_menos_cuatro_funciones():
    """Restricción: al menos 4 funciones separadas."""
    tree = ast.parse(_codigo())
    funciones = [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
    assert len(funciones) >= 4, (
        f"Debes definir al menos 4 funciones separadas. "
        f"Encontradas: {funciones}"
    )


def test_usa_modulo_csv():
    """Restricción: debe usar el módulo csv de la librería estándar."""
    codigo = _codigo()
    assert "import csv" in codigo or "from csv" in codigo, (
        "Debes usar el módulo 'csv' de la librería estándar de Python"
    )


def test_usa_requests():
    """Restricción: debe usar el módulo requests para descargar el CSV."""
    codigo = _codigo()
    assert "requests" in codigo, (
        "Debes usar el módulo 'requests' para descargar el CSV de internet"
    )


def test_no_usa_pandas_ni_numpy():
    """Restricción: no usar pandas ni numpy."""
    codigo = _codigo()
    assert "pandas" not in codigo, "No puedes usar pandas en este reto (M05-M06)"
    assert "numpy" not in codigo, "No puedes usar numpy en este reto (M05-M06)"


def test_genera_reporte_csv():
    """El programa debe generar un archivo reporte_limpio.csv."""
    # Limpiamos cualquier CSV previo para que el test sea determinista
    if os.path.exists(REPORTE_CSV):
        os.remove(REPORTE_CSV)
    r = _run()
    assert os.path.exists(REPORTE_CSV), (
        f"El programa debe generar 'reporte_limpio.csv' al ejecutarse. "
        f"Stderr:\n{r.stderr}"
    )


def test_reporte_csv_tiene_datos():
    """El reporte_limpio.csv no debe estar vacío y debe tener cabeceras."""
    if not os.path.exists(REPORTE_CSV):
        # Ejecutamos primero para generarlo
        _run()
    assert os.path.exists(REPORTE_CSV), "reporte_limpio.csv no existe"
    with open(REPORTE_CSV, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        filas = list(reader)
    assert len(filas) >= 2, (
        "El reporte_limpio.csv debe tener al menos una cabecera y una fila de datos"
    )


def test_muestra_metricas_en_consola():
    """El output en consola debe mostrar mínimo, máximo y promedio."""
    r = _run()
    stdout = r.stdout.lower()
    assert any(kw in stdout for kw in ["mínimo", "minimo", "min"]), (
        "El output debe mostrar el valor mínimo de al menos una columna"
    )
    assert any(kw in stdout for kw in ["máximo", "maximo", "max"]), (
        "El output debe mostrar el valor máximo de al menos una columna"
    )
    assert any(kw in stdout for kw in ["promedio", "media", "avg", "average"]), (
        "El output debe mostrar el promedio de al menos una columna"
    )
