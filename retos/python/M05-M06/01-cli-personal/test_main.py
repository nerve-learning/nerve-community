"""test_main.py — Evaluador automático: CLI Personal Útil."""
import ast, subprocess, sys, os, json, tempfile, shutil

BASE = os.path.dirname(__file__)
RETO = os.path.join(BASE, "reto.py")


def _codigo():
    if os.path.exists(RETO):
        with open(RETO) as f:
            return f.read()
    return ""


def _run(*args, env_cwd=None):
    return subprocess.run(
        [sys.executable, RETO, *args],
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


def test_sin_argumentos_muestra_ayuda():
    """Sin argumentos, el programa debe mostrar instrucciones de uso (ayuda)."""
    r = _run()
    stdout = r.stdout.lower()
    assert any(kw in stdout for kw in ["uso", "uso:", "ayuda", "help", "commands", "comandos"]), (
        "Sin argumentos, el programa debe mostrar un mensaje de ayuda con los comandos disponibles"
    )


def test_comando_add():
    """El comando para agregar debe funcionar sin crashear."""
    # Usamos un directorio temporal para no contaminar el repo
    with tempfile.TemporaryDirectory() as tmpdir:
        shutil.copy(RETO, os.path.join(tmpdir, "reto.py"))
        r = _run("add", "item de prueba", env_cwd=tmpdir)
        assert r.returncode == 0, (
            f"El comando 'add' terminó con error:\n{r.stderr}"
        )


def test_comando_list():
    """El comando para listar debe funcionar sin crashear."""
    with tempfile.TemporaryDirectory() as tmpdir:
        shutil.copy(RETO, os.path.join(tmpdir, "reto.py"))
        # Primero añadimos algo
        _run("add", "elemento de prueba", env_cwd=tmpdir)
        r = _run("list", env_cwd=tmpdir)
        assert r.returncode == 0, (
            f"El comando 'list' terminó con error:\n{r.stderr}"
        )


def test_datos_persisten():
    """Los datos deben persistir: añadir y luego listar en el mismo directorio."""
    with tempfile.TemporaryDirectory() as tmpdir:
        shutil.copy(RETO, os.path.join(tmpdir, "reto.py"))
        _run("add", "tarea persistente", env_cwd=tmpdir)
        r = _run("list", env_cwd=tmpdir)
        assert "tarea persistente" in r.stdout or "persistente" in r.stdout, (
            "Los datos deben persistir entre invocaciones. "
            "Guarda los datos en un archivo (.txt o .json)."
        )


def test_no_crashea_con_argumento_invalido():
    """El programa no debe crashear con argumentos inválidos."""
    r = _run("comando_que_no_existe")
    assert r.returncode == 0 or "error" not in r.stderr.lower(), (
        "El programa no debe crashear con comandos desconocidos. "
        "Muestra un mensaje de error amigable."
    )


def test_usa_sys_argv():
    """Restricción: debe usar sys.argv para los comandos."""
    codigo = _codigo()
    assert "sys.argv" in codigo, (
        "Debes usar sys.argv para leer los argumentos de línea de comandos"
    )


def test_al_menos_tres_funciones_con_docstring():
    """Restricción: al menos 3 funciones definidas con docstring."""
    tree = ast.parse(_codigo())
    funciones_con_doc = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            tiene_doc = (
                node.body
                and isinstance(node.body[0], ast.Expr)
                and isinstance(node.body[0].value, ast.Constant)
                and isinstance(node.body[0].value.value, str)
            )
            if tiene_doc:
                funciones_con_doc.append(node.name)
    assert len(funciones_con_doc) >= 3, (
        f"Debes definir al menos 3 funciones con docstring. "
        f"Con docstring encontradas: {funciones_con_doc}"
    )


def test_manejo_de_errores_con_try_except():
    """Restricción: debe usar try/except para manejar errores."""
    tree = ast.parse(_codigo())
    try_blocks = [n for n in ast.walk(tree) if isinstance(n, ast.Try)]
    assert len(try_blocks) >= 1, (
        "Debes usar al menos un bloque try/except para manejar errores"
    )


def test_no_usa_librerías_prohibidas():
    """Restricción: no usar argparse, click ni typer."""
    codigo = _codigo()
    for lib in ["argparse", "click", "typer"]:
        assert lib not in codigo, (
            f"No puedes usar '{lib}' en este reto. Usa sys.argv directamente."
        )
