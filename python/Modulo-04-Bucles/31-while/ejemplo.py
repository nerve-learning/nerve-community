# ==========================================
# Archivo: ejemplo.py
# Autor: Kaia / Alenia Studios
# Descripción: Comprendiendo el bucle while
# ==========================================

print("--- Inicio de la Aventura ---")

# Imagina un personaje de un videojuego que tiene 5 puntos de energía.
# Guardamos este valor usando el símbolo '=' (que significa "asigna este valor a este nombre").
energia = 5

print("Energía inicial del jugador:")
print(energia)

print("--- Entrando al Bosque ---")

# Le decimos a la computadora: 
# "Mientras (while) la energía sea mayor que (>) 0, entonces (:) repite lo siguiente:"
while energia > 0:
    
    # Todo lo que tiene espacios al inicio (indentación) se repite.
    print("El jugador da un paso en el bosque...")
    
    # ¡Punto crítico! Si damos un paso, debemos gastar energía.
    # Tomamos el valor actual de 'energia', le restamos 1, 
    # y el resultado lo volvemos a guardar (=) en 'energia'.
    energia = energia - 1
    
    # Mostramos cuánta energía queda después del paso.
    print("Energía restante:")
    print(energia)

# Cuando la energía llega a 0, la condición 'energia > 0' se vuelve falsa.
# La computadora ignora el bloque indentado y continúa con el código de abajo.

print("--- Fin de la Aventura ---")
print("El jugador se ha quedado sin energía y debe descansar.")
