"""test_main.py"""
import subprocess, sys, os
BASE = os.path.dirname(__file__)
RETO = os.path.join(BASE, "reto.py")
def test_archivo_existe():
    assert os.path.exists(RETO)
def test_calcular_dano():
    sys.path.insert(0, BASE)
    from reto import calcular_dano
    assert calcular_dano(50, 30) == 20
    assert calcular_dano(10, 50) == 0 or calcular_dano(10, 50) < 0
