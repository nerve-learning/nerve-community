print("--- 1. Scope Local (El Secreto) ---")

def planear_sorpresa():
    regalo = "Un viaje a la luna"
    print("Dentro de la función, el regalo es:", regalo)

# Llamamos a la función
planear_sorpresa()

# Si descomentas la línea de abajo, el programa EXPLOTARÁ con NameError
# porque 'regalo' ya no existe aquí afuera.
# print(regalo) 


print("\n--- 2. Leer Variables Globales ---")

# Esta variable vive en el pasillo principal. Todos la ven.
juego_actual = "Zelda"

def mostrar_juego():
    # La función simplemente se asoma al pasillo y lee el valor.
    print("Estamos jugando:", juego_actual)

mostrar_juego()


print("\n--- 3. Modificar Variables Globales (La palabra mágica) ---")

# Nuestro jugador empieza con 3 vidas (Global)
vidas_jugador = 3

def recibir_golpe():
    # Le avisamos a Python que NO queremos crear una variable local nueva.
    # Queremos afectar a la variable 'vidas_jugador' que ya existe afuera.
    global vidas_jugador 
    
    # Ahora sí podemos modificarla
    vidas_jugador = vidas_jugador - 1
    print("¡Ouch! Recibiste un golpe.")

print("Vidas al iniciar:", vidas_jugador)

# Recibimos dos golpes
recibir_golpe()
recibir_golpe()

# Como usamos 'global', el cambio es permanente para todo el programa.
print("Vidas después del combate:", vidas_jugador)
