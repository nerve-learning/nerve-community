print("--- Suite de Ejemplo: Sistema de Inventario ---")
print("Ejecuta 'pytest ejemplo.py' en la terminal para ver correr la suite.")

import pytest

# ==========================================
# CÓDIGO DE PRODUCCIÓN (El sistema real)
# ¡Nota lo bien documentado y etiquetado que está!
# ==========================================

def agregar_al_inventario(inventario: dict, producto: str, cantidad: int) -> dict:
    """
    Suma una cantidad de un producto al inventario de la tienda.
    
    Args:
        inventario: El diccionario actual con los productos y existencias.
        producto: El nombre del producto a agregar.
        cantidad: Cuántos elementos sumar al inventario.
        
    Returns:
        El diccionario del inventario ya actualizado.
    """
    if producto in inventario:
        inventario[producto] = inventario[producto] + cantidad
    else:
        inventario[producto] = cantidad
        
    return inventario


# ==========================================
# LA SUITE DE TESTS (Nuestro robot inspector)
# ==========================================

# 1. Los Ayudantes (Fixtures)
@pytest.fixture
def inventario_vacio():
    """Entrega un inventario totalmente vacío."""
    return {}

@pytest.fixture
def inventario_con_manzanas():
    """Entrega un inventario que ya tiene 5 manzanas."""
    return {"manzanas": 5}


# 2. Test simple (usando el fixture vacío)
def test_agregar_un_producto_nuevo(inventario_vacio):
    # El ayudante nos dio {}, le agregamos 10 peras
    resultado = agregar_al_inventario(inventario_vacio, "peras", 10)
    
    # Exigimos que ahora existan 10 peras
    assert resultado["peras"] == 10


# 3. Test Parametrizado (usando fixture y parametrize a la vez)
# Vamos a probar agregar 2, 10 y 0 manzanas.
@pytest.mark.parametrize("cantidad_extra, total_esperado", [
    [2, 7],   # 5 + 2 = 7
    [10, 15], # 5 + 10 = 15
    [0, 5]    # 5 + 0 = 5
])
def test_agregar_producto_ya_existente(inventario_con_manzanas, cantidad_extra, total_esperado):
    
    # El ayudante nos da el dict con 5 manzanas
    resultado = agregar_al_inventario(inventario_con_manzanas, "manzanas", cantidad_extra)
    
    # Exigimos que la suma matemática se haya hecho bien
    assert resultado["manzanas"] == total_esperado
