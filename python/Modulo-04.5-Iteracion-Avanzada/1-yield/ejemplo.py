print("--- Parte 1: return vs yield ---")

# Con return: la función termina y devuelve TODO de golpe
def tres_con_return():
    return "Uno"   # La función muere aquí. Nunca llega a los siguientes return.
    return "Dos"   # Esto NUNCA se ejecuta
    return "Tres"  # Esto NUNCA se ejecuta

resultado = tres_con_return()
print(resultado)   # Solo muestra: Uno


print("--- Parte 2: yield pausa en vez de terminar ---")

# Con yield: la función se pausa y recuerda dónde estaba
def tres_con_yield():
    yield "Uno"    # Pausa 1: entrega "Uno" y se congela
    yield "Dos"    # Pausa 2: cuando la pidan de nuevo, entrega "Dos"
    yield "Tres"   # Pausa 3: y por último "Tres"

# Llamar a la función NO la ejecuta. Crea el "chef en espera"
mi_generador = tres_con_yield()

# next() activa el chef: ejecuta hasta el primer yield
print(next(mi_generador))   # Uno
print(next(mi_generador))   # Dos   (continuó desde donde pausó)
print(next(mi_generador))   # Tres


print("--- Parte 3: la forma elegante es usar for ---")

# El bucle for llama a next() por nosotros y para solo cuando se acaba
for valor in tres_con_yield():
    print(valor)
# Imprime: Uno, Dos, Tres (en 3 líneas)


print("--- Parte 4: yield dentro de un bucle ---")

# La función puede tener su propio bucle interno con yield adentro
def contar_hasta(limite):
    numero = 1
    while numero <= limite:
        yield numero       # Pausa aquí y entrega el número actual
        numero = numero + 1  # Cuando la reanuden, suma 1 y continúa el while

# Pedimos los números de uno en uno
for n in contar_hasta(5):
    print(f"El chef entregó: {n}")


print("--- Parte 5: yield recuerda las variables internas ---")

# La variable "acumulado" sobrevive entre cada pausa
def suma_acumulada(numeros):
    acumulado = 0
    for n in numeros:
        acumulado = acumulado + n
        yield acumulado  # Entrega el total parcial en cada paso

mis_numeros = [10, 5, 20, 3]
for total_parcial in suma_acumulada(mis_numeros):
    print(f"Suma hasta ahora: {total_parcial}")
# Muestra: 10 → 15 → 35 → 38
