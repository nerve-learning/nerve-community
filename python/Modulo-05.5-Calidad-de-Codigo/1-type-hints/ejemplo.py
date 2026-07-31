print("--- Parte 1: funciones sin etiqueta (el problema) ---")

# Sin type hints: no sabes qué pasar ni qué esperar de vuelta
def calcular_area(base, altura):
    return base * altura

# ¿Funciona con texto? La función no lo dice, así que lo pruebo y puede fallar
print(calcular_area(5, 10))      # 50 — bien
# print(calcular_area("5", 10))  # 50505050... ¡catástrofe silenciosa!


print("--- Parte 2: las mismas funciones CON etiquetas ---")

# Ahora cualquiera que lea esto sabe: pasa dos float, recibirás un float
def calcular_area_v2(base: float, altura: float) -> float:
    return base * altura

print(calcular_area_v2(5.0, 10.0))   # 50.0


print("--- Parte 3: etiquetando con str, int y bool ---")

# -> str : esta función devuelve texto
def crear_saludo(nombre: str, veces: int) -> str:
    saludo = "Hola, " + nombre + "! "
    return saludo * veces   # Repite el texto 'veces' veces

print(crear_saludo("Ana", 3))


# -> bool : esta función devuelve Verdadero o Falso
def puede_votar(edad: int) -> bool:
    return edad >= 18

print(puede_votar(20))   # True
print(puede_votar(15))   # False


print("--- Parte 4: funciones que no devuelven nada usan -> None ---")

# -> None: la función hace algo pero no devuelve ningún valor
def imprimir_lista(elementos: list) -> None:
    for elemento in elementos:
        print("  -", elemento)

imprimir_lista(["Leche", "Pan", "Huevos"])
# Esta función no tiene return, por eso su tipo de retorno es None


print("--- Parte 5: etiquetando parámetros con valor por defecto ---")

# El valor por defecto va DESPUÉS de la etiqueta de tipo
def describir_producto(nombre: str, precio: float, disponible: bool = True) -> str:
    estado = "En stock" if disponible else "Agotado"
    return f"{nombre} — ${precio} — {estado}"

print(describir_producto("Teclado", 450.0))             # usa disponible=True por defecto
print(describir_producto("Monitor", 3200.0, False))     # sobreescribe el default
