print("--- Parte 1: La función que queremos probar ---")

def calcular_doble(numero: int) -> int:
    """Devuelve el doble de un número."""
    return numero * 2

print("Normalmente probaríamos así a mano:")
print("El doble de 4 es:", calcular_doble(4))


print("\n--- Parte 2: Usando assert manualmente ---")
# El assert evalúa si algo es True. Si lo es, no hace nada (todo está bien).
# Si es False, el programa "explota" con un error gigante.

print("Exigiendo que calcular_doble(5) sea 10 con assert...")
assert calcular_doble(5) == 10
print("¡Todo bien! El código sobrevivió al assert porque 5*2 sí es 10.")


print("\n--- Parte 3: Así se ve un test de pytest ---")
# Para pytest, los tests se encierran en funciones que empiezan con "test_"

def test_calcular_doble_con_positivos():
    """Prueba que el doble de 3 sea 6."""
    resultado = calcular_doble(3)
    assert resultado == 6

def test_calcular_doble_con_ceros():
    """Prueba que el doble de 0 sea 0."""
    assert calcular_doble(0) == 0

# NOTA IMPORTANTE: 
# Si ejecutas este archivo normalmente con el botón "Run" de Python, 
# Python no ejecutará las funciones `test_` automáticamente. No pasará nada.
#
# Para que los tests corran de verdad, debes decirle al programa "pytest" que los busque.
# Se hace escribiendo en tu terminal: pytest ejemplo.py
