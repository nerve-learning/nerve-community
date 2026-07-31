"""test_main.py — Evaluador automático: Red de Scripts con Nerve."""
import ast, os

BASE = os.path.dirname(__file__)
RETO = os.path.join(BASE, "reto.py")

# Los 3 scripts requeridos por el reto
PRODUCTOR = os.path.join(BASE, "productor.py")
PROCESADOR = os.path.join(BASE, "procesador.py")
MONITOR = os.path.join(BASE, "monitor.py")


def _codigo(path):
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return ""


def _todos_los_scripts():
    """Devuelve el código concatenado de todos los archivos Python del reto."""
    archivos = [f for f in os.listdir(BASE) if f.endswith(".py") and f != "test_main.py"]
    return "\n".join(_codigo(os.path.join(BASE, a)) for a in archivos)


def test_tres_scripts_existen():
    """El reto requiere 3 scripts separados: productor, procesador y monitor."""
    # Buscamos scripts con nombres que impliquen esos roles
    archivos_py = [f for f in os.listdir(BASE) if f.endswith(".py") and f != "test_main.py"]
    assert len(archivos_py) >= 3, (
        f"Debes crear al menos 3 scripts Python separados "
        f"(productor, procesador, monitor). Encontrados: {archivos_py}"
    )


def test_scripts_tienen_sintaxis_valida():
    """Todos los scripts deben tener sintaxis Python válida."""
    archivos_py = [
        os.path.join(BASE, f)
        for f in os.listdir(BASE)
        if f.endswith(".py") and f != "test_main.py"
    ]
    for ruta in archivos_py:
        codigo = _codigo(ruta)
        try:
            ast.parse(codigo)
        except SyntaxError as e:
            assert False, f"El archivo '{os.path.basename(ruta)}' tiene error de sintaxis: {e}"


def test_usa_nerve_nexus_client():
    """Restricción: deben usar NexusClient de nerve."""
    codigo = _todos_los_scripts()
    assert "NexusClient" in codigo, (
        "Debes importar y usar NexusClient de la librería nerve en tus scripts"
    )


def test_usa_nerve_nexus_hub():
    """Restricción: deben usar NexusHub o NexusClient de nerve."""
    codigo = _todos_los_scripts()
    assert "NexusHub" in codigo or "NexusClient" in codigo, (
        "Debes usar NexusHub o NexusClient de nerve en tu arquitectura"
    )


def test_usa_async_await():
    """Restricción: debe usar async/await (no threading directo)."""
    codigo = _todos_los_scripts()
    assert "async def" in codigo or "await " in codigo or "asyncio" in codigo, (
        "Debes usar async/await y asyncio para la concurrencia. "
        "No puedes usar threading directamente."
    )


def test_no_usa_threading_directo():
    """Restricción: no usar threading directamente."""
    codigo = _todos_los_scripts()
    assert "import threading" not in codigo and "from threading" not in codigo, (
        "No puedes usar el módulo 'threading' directamente. Usa async/await con asyncio."
    )


def test_manejo_de_reconexion():
    """El sistema debe manejar reconexión automática."""
    codigo = _todos_los_scripts()
    reconexion_keywords = [
        "reconect", "reconnect", "retry", "reintentar",
        "try", "except", "while True", "while true"
    ]
    tiene_reconexion = any(kw in codigo.lower() for kw in reconexion_keywords)
    assert tiene_reconexion, (
        "Debes implementar lógica de reconexión automática en al menos un script. "
        "Usa try/except + un bucle de reintento."
    )


def test_hay_logica_de_produccion_datos():
    """El script productor debe generar datos con algún intervalo de tiempo."""
    codigo = _todos_los_scripts()
    assert "sleep" in codigo or "asyncio.sleep" in codigo, (
        "El productor debe enviar datos con un intervalo (usa asyncio.sleep o time.sleep)"
    )


def test_hay_logica_de_dashboard_o_display():
    """El monitor debe mostrar algo en pantalla (print o similar)."""
    codigo = _todos_los_scripts()
    assert "print(" in codigo, (
        "El script monitor debe mostrar un dashboard en consola con print()"
    )
