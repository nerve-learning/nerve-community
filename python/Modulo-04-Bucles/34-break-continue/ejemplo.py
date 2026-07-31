# ==========================================
# Archivo: ejemplo.py
# Autor: Kaia / Alenia Studios
# Descripción: Comprendiendo el freno break
# ==========================================

print("--- El Cofre del Tesoro ---")

# Tenemos una lista con las cosas que hay dentro del cofre.
cofre = ["telaraña", "polvo", "diamante", "hueso", "piedra"]

print("El pirata empieza a sacar cosas del cofre...")

# Recorremos la lista usando nuestro bucle for.
for cosa in cofre:
    
    # Imprimimos lo que acabamos de sacar.
    print("El pirata saca:")
    print(cosa)
    
    # Ahora verificamos: ¿Es esto lo que buscábamos?
    if cosa == "diamante":
        
        # Si es el diamante, celebramos.
        print("¡Encontramos el tesoro!")
        
        # ¡Jalamos el freno de emergencia!
        # Como ya encontramos el diamante, no tiene sentido 
        # seguir sacando los huesos y las piedras.
        break

print("--- Fin de la Búsqueda ---")
print("El pirata cierra el cofre y se va a casa feliz.")

# Si corres este código, notarás que "hueso" y "piedra" 
# NUNCA se imprimen, porque el bucle fue destruido por el 'break'.
