# Traemos a nuestro experto en matemáticas y lo llamamos "np"
import numpy as np

print("--- 1. La decepción de la lista normal ---")
lista_vieja = [10, 20, 30]
print("Lista normal:", lista_vieja)
# Si intentamos hacer: lista_vieja + 5
# La computadora entra en pánico y nos da un error. ¡Las listas normales no saben sumar números a sus elementos!


print("\n--- 2. El nacimiento del Array ---")
# Le damos nuestra lista normal a Numpy para que la mejore
super_lista = np.array([10, 20, 30])
print("Súper lista de Numpy:", super_lista)


print("\n--- 3. Magia Matemática (Sin usar 'for') ---")
# Le sumamos 5. Numpy irá número por número sumando 5 mágicamente.
precios_mas_cinco = super_lista + 5
print("Sumando 5 a todos de golpe:", precios_mas_cinco)

# Multiplicamos por 2.
precios_dobles = super_lista * 2
print("Multiplicando todos por 2:", precios_dobles)


print("\n--- 4. Array contra Array ---")
array_precios = np.array([100, 200, 300])
array_cantidades = np.array([2, 1, 3])

# Multiplica el primero con el primero (100 * 2)
# El segundo con el segundo (200 * 1)
# El tercero con el tercero (300 * 3)
totales = array_precios * array_cantidades
print("Total a pagar por producto:", totales)
