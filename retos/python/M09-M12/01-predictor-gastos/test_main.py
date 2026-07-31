"""test_main.py — Evaluador automático: Predictor de Gastos."""
import ast, subprocess, sys, os, csv

BASE = os.path.dirname(__file__)
RETO = os.path.join(BASE, "reto.py")
CSV_GASTOS = os.path.join(BASE, "gastos.csv")  # El alumno debe crearlo


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
        timeout=60,
        cwd=BASE,
    )


def test_archivo_reto_existe():
    assert os.path.exists(RETO), "Debes crear el archivo reto.py"


def test_codigo_valido():
    try:
        ast.parse(_codigo())
    except SyntaxError as e:
        assert False, f"Tu código tiene errores de sintaxis: {e}"


def test_csv_de_gastos_existe():
    """El alumno debe incluir un archivo CSV con al menos 12 meses de gastos."""
    # Buscamos cualquier .csv en el directorio del reto
    csvs = [f for f in os.listdir(BASE) if f.endswith(".csv")]
    assert len(csvs) >= 1, (
        "Debes incluir un archivo CSV con los gastos históricos (al menos 12 meses). "
        "No hay ningún .csv en el directorio del reto."
    )


def test_csv_tiene_doce_meses():
    """El CSV debe tener al menos 12 filas de datos (más la cabecera)."""
    csvs = [os.path.join(BASE, f) for f in os.listdir(BASE) if f.endswith(".csv")]
    if not csvs:
        assert False, "No se encontró ningún archivo CSV"
    # Usamos el primer CSV encontrado
    with open(csvs[0], newline="", encoding="utf-8") as f:
        filas = list(csv.reader(f))
    # Restamos la cabecera
    datos = [fila for fila in filas if fila and not fila[0].strip().lower() in ["mes", "month", "fecha", "date"]]
    assert len(datos) >= 12, (
        f"El CSV debe tener al menos 12 filas de datos (12 meses). "
        f"Filas de datos encontradas: {len(datos)}"
    )


def test_usa_scikit_learn():
    """Restricción: debe usar scikit-learn para la regresión lineal."""
    codigo = _codigo()
    assert "sklearn" in codigo or "scikit" in codigo.lower() or "LinearRegression" in codigo, (
        "Debes usar scikit-learn para el modelo de regresión lineal. "
        "Importa LinearRegression de sklearn."
    )


def test_usa_matplotlib():
    """Restricción: debe usar matplotlib para la gráfica."""
    codigo = _codigo()
    assert "matplotlib" in codigo or "plt" in codigo, (
        "Debes usar matplotlib para generar la gráfica de tendencia"
    )


def test_no_usa_pandas_para_modelo():
    """Restricción: no usar pandas para el modelo (solo numpy y scikit-learn)."""
    codigo = _codigo()
    # pandas sí puede usarse para leer el CSV, pero el reto dice "para el modelo"
    # Verificamos que el alumno no use pandas directamente con sklearn
    if "pandas" in codigo and "sklearn" in codigo:
        # Aceptamos pandas para lectura del CSV, solo validamos que use numpy también
        assert "numpy" in codigo or "np." in codigo, (
            "Si usas pandas, también debes usar numpy para alimentar el modelo sklearn. "
            "No uses pandas directamente en el fit/predict."
        )


def test_muestra_prediccion_en_consola():
    """El output debe mostrar una predicción numérica."""
    r = _run()
    stdout = r.stdout.lower()
    assert r.returncode == 0, f"El programa terminó con error:\n{r.stderr}"
    assert any(kw in stdout for kw in [
        "predicción", "prediccion", "próximo mes", "proximo mes",
        "proyección", "proyeccion", "estimado", "prediction"
    ]), (
        "El output debe mostrar la predicción de gastos para el siguiente mes"
    )


def test_genera_grafica():
    """El programa debe generar o mostrar una gráfica (archivo .png o plt.show)."""
    codigo = _codigo()
    # Verificamos que el código intente mostrar o guardar una gráfica
    assert "plt.show" in codigo or "savefig" in codigo or ".plot(" in codigo, (
        "Tu código debe generar una gráfica. Usa plt.show() o plt.savefig()"
    )
