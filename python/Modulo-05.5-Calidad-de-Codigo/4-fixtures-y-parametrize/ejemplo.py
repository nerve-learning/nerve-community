print("--- Este archivo muestra cómo usar Fixtures y Parametrize ---")
print("Cámbiale el nombre a test_ejemplo.py y ejecuta: pytest test_ejemplo.py en la terminal\n")

# Importamos la caja de herramientas de pytest
import pytest

print("--- Parte 1: Fixtures (Ayudantes) ---")

# Creamos un fixture usando el decorador @pytest.fixture
@pytest.fixture
def usuario_falso():
    """Un ayudante que nos fabrica un diccionario de usuario listo para probar."""
    return {"nombre": "Kaia", "edad": 25, "rol": "admin"}

# El test pide el 'usuario_falso' en sus paréntesis. pytest se lo entrega mágicamente.
def test_usuario_es_admin(usuario_falso):
    # Ya no tengo que crear el diccionario aquí adentro, ¡ya viene hecho!
    assert usuario_falso["rol"] == "admin"

def test_usuario_tiene_edad_correcta(usuario_falso):
    # ¡Puedo reusar el mismo ayudante en múltiples tests!
    assert usuario_falso["edad"] == 25


print("\n--- Parte 2: Parametrize (Pruebas Múltiples) ---")

def es_par(numero: int) -> bool:
    """Devuelve True si el número es par."""
    return numero % 2 == 0

# En vez de hacer 3 tests diferentes, hacemos uno solo que se repite 3 veces.
# Le damos el nombre del parámetro entre comillas ("num") y la lista de valores a probar.
@pytest.mark.parametrize("num", [2, 8, 100])
def test_numeros_pares(num):
    assert es_par(num) == True

# También podemos probar varios parámetros a la vez.
# Ponemos los nombres separados por comas, y pasamos una lista de "paquetitos" (listas internas).
# Esto significa: prueba sumar 1+1 esperando 2. Luego 5+5 esperando 10. Etc.
@pytest.mark.parametrize("a, b, esperado", [
    [1, 1, 2],
    [5, 5, 10],
    [10, -5, 5]
])
def test_suma_variada(a, b, esperado):
    assert a + b == esperado
