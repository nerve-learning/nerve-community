# Aquí estamos definiendo nuestra primera "receta" (función).
# Usamos 'def' para avisar a Python que vamos a inventar un comando.
# Le llamamos 'imprimir_separador'
def imprimir_separador():
    # Todo lo que tiene espacios a la izquierda pertenece a esta receta.
    print("====================================")
    print("          🌟🌟🌟🌟🌟🌟          ")
    print("====================================")

# Definamos una segunda función para mostrar información
def mostrar_perfil():
    print("Nombre: Jugador 1")
    print("Nivel: 41")
    print("Estado: Aprendiendo funciones")


print("--- Iniciando el programa ---")

# ¡ATENCIÓN! Si corres el código hasta aquí (ignorando lo de abajo), 
# no verás los "========" ni la información del jugador. 
# ¿Por qué? Porque 'def' solo GUARDA los pasos, no los ejecuta.

print("\n--- Llamando a nuestras funciones ---")

# Ahora sí, le damos la orden a Python: "Ve a buscar la receta imprimir_separador y cocínala"
imprimir_separador()

# Ahora le decimos que muestre el perfil
mostrar_perfil()

# Y podemos reutilizar nuestro separador tantas veces como queramos.
# ¡Esa es la magia! Nos ahorramos escribir todos esos prints de nuevo.
imprimir_separador()

print("\n--- Fin del programa ---")
