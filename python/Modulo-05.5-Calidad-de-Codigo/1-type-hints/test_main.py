"""test_main.py"""
import subprocess, sys, os
BASE = os.path.dirname(__file__)
def test_archivo_existe():
    assert os.path.exists(os.path.join(BASE, "reto.py"))
def test_type_hints_presentes():
    sys.path.insert(0, BASE)
    import importlib
    mod = importlib.import_module("reto")
    funciones = [v for k, v in vars(mod).items() if callable(v) and not k.startswith("_")]
    assert any(hasattr(f, "__annotations__") and f.__annotations__ for f in funciones), \
        "Al menos una función debe tener type hints"
