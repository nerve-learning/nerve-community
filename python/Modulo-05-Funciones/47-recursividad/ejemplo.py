print("--- 1. Cuenta Regresiva (Sin Bucles) ---")

def lanzar_cohete(segundos):
    # CASO BASE (El Freno)
    if segundos <= 0:
        print("🚀 ¡Fuego!")
        # Con return, decimos "no más llamadas, salte de aquí"
        return
    
    # ACCIÓN
    print("Faltan", segundos, "segundos...")
    
    # LLAMADA RECURSIVA (El Espejo)
    # Reducimos el problema restando 1
    lanzar_cohete(segundos - 1)

lanzar_cohete(3)


print("\n--- 2. Sumando números hacia atrás ---")

# Esta función suma un número con todos sus anteriores
# Ejemplo: si pasas 4, suma 4 + 3 + 2 + 1
def suma_total(numero):
    # CASO BASE: Si llegamos a 1, el total es simplemente 1. Freno de mano.
    if numero == 1:
        return 1
    
    # LLAMADA RECURSIVA Y RETORNO
    # Aquí es más complejo: el resultado es el número actual MÁS 
    # el resultado de llamar a la función con el número anterior.
    return numero + suma_total(numero - 1)

# ¿Cómo piensa Python al ejecutar suma_total(3)?
# 1. 3 + suma_total(2)
# 2. 3 + (2 + suma_total(1))
# 3. 3 + (2 + 1) -> Porque suma_total(1) chocó con el freno y devolvió 1.
# 4. Total: 6.

resultado = suma_total(3)
print("La suma de 3 + 2 + 1 es:", resultado)


print("\n--- 3. El peligro del Espejo Infinito ---")

def agujero_negro(energia):
    # Aquí NO HAY FRENO (No hay un 'if' que haga return)
    print("Absorbiendo energía...", energia)
    # agujero_negro(energia - 1) 
    
    # Si descomentas la línea de arriba y corres esto, 
    # Python intentará crear la función tantas veces que 
    # gritará 'RecursionError' y se apagará para proteger tu PC.
    pass

agujero_negro(10)
print("El agujero negro está desactivado por seguridad.")
