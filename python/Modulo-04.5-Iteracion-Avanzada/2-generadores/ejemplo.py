print("--- Parte 1: El cubo vs el grifo ---")

# EL CUBO: una lista que guarda TODO de una vez
cubo = [1, 2, 3, 4, 5]
print("Tipo cubo:", type(cubo))   # <class 'list'>

# EL GRIFO: una función con yield que produce bajo demanda
def grifo():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

mi_grifo = grifo()                       # Crea el grifo, no produce nada aún
print("Tipo grifo:", type(mi_grifo))     # <class 'generator'>


print("--- Parte 2: ambos producen el mismo resultado ---")

print("Desde el cubo:")
for n in cubo:
    print(n)

print("Desde el grifo:")
for n in grifo():   # Nota: llamamos grifo() de nuevo porque el anterior se usó
    print(n)


print("--- Parte 3: el grifo con while (más útil) ---")

# Esto sería imposible con una lista si el límite fuera 1,000,000
def contar_hasta(limite):
    numero = 1
    while numero <= limite:
        yield numero
        numero = numero + 1

# Pedimos solo los primeros 3 usando next() manual
generador = contar_hasta(1000000)  # Nadie guardó un millón de números en memoria
print(next(generador))   # 1  — solo calculó el primero
print(next(generador))   # 2  — solo calculó el segundo
print(next(generador))   # 3  — solo calculó el tercero
# El millón de números restantes nunca se calcularon porque no los pedimos


print("--- Parte 4: generador con filtro ---")

# Un generador puede decidir qué producir con un if
def solo_pares(numeros):
    for n in numeros:
        if n % 2 == 0:      # % es el "resto" de la división (ya lo viste)
            yield n         # Solo produce el número si es par

mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for par in solo_pares(mi_lista):
    print(f"  Número par: {par}")


print("--- Parte 5: el generador se agota (solo lee una vez) ---")

generador_corto = solo_pares([2, 4, 6])

print("Primera vuelta:")
for n in generador_corto:
    print(n)   # Imprime: 2, 4, 6

print("Segunda vuelta (el grifo está vacío):")
for n in generador_corto:
    print(n)   # No imprime NADA — el generador se agotó

print("Fin del programa")
