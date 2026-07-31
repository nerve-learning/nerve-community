# ejemplo.py

print("--- La Caja Fuerte del Banco ---")

# Para abrir la bóveda, primero necesitas la tarjeta de acceso.
# Si tienes la tarjeta, pasas a una segunda puerta donde debes poner un PIN numérico.

tiene_tarjeta = True
pin_ingresado = 1234

# PRIMER FILTRO (Puerta exterior)
if tiene_tarjeta == True:
    # --- ZONA INTERMEDIA (4 espacios) ---
    print("Tarjeta aceptada. Pasando a verificación de PIN...")
    
    # SEGUNDO FILTRO (Puerta interior, dentro del primer if)
    if pin_ingresado == 1234:
        # --- ZONA HIPER-SECRETA (8 espacios) ---
        print("PIN correcto. Bóveda abierta. 💰")
    
    # Este else está alineado a 4 espacios. Es el Plan B del SEGUNDO filtro.
    else:
        print("ALERTA: PIN incorrecto. Llamando a la policía. 🚓")

# Este else está pegado a la izquierda. Es el Plan B del PRIMER filtro.
else:
    print("Acceso denegado. No tienes tarjeta.")


print("\n--- La Pizzería ---")

# A veces queremos evaluar cosas distintas dependiendo de la primera decisión.
quiere_pizza = True
tamaño = "familiar"

if quiere_pizza == True:
    print("¡Genial! Vamos a preparar tu pizza.")
    
    if tamaño == "familiar":
        print("Agregando doble queso por ser tamaño familiar.")
    else:
        print("Preparando una pizza normal.")

else:
    print("Oh, no quieres pizza. ¿Tal vez quieres una ensalada?")
