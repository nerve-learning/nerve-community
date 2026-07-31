print("--- Este archivo muestra cómo usar un Mock (Doble de Acción) ---")
print("Cámbiale el nombre a test_ejemplo.py y ejecuta: pytest test_ejemplo.py en la terminal\n")

print("--- Parte 1: El Código Real ---")

# Actor real: Impredecible
def checar_clima_en_internet() -> str:
    # Imagina que aquí nos conectamos a la NASA
    # Puede devolver "Soleado", "Lluvia", o fallar si no hay internet.
    return "Soleado"

# La función a probar. 
# Si el parámetro 'funcion_clima' no se le pasa nada, usa 'checar_clima_en_internet' por defecto.
# (¡Qué gran truco para no romper el código viejo!)
def decidir_que_ropa_usar(funcion_clima = checar_clima_en_internet) -> str:
    clima = funcion_clima() # Ejecutamos la función que nos pasaron
    
    if clima == "Lluvia":
        return "Lleva paraguas"
    else:
        return "Lleva gafas de sol"


print("\n--- Parte 2: Los Tests con Mocks ---")

def test_cuando_llueve_recomienda_paraguas():
    # 1. Creamos al doble de acción que finge que siempre llueve
    def clima_falso_lluvia():
        return "Lluvia"
        
    # 2. Le pasamos el doble a nuestra función
    recomendacion = decidir_que_ropa_usar(clima_falso_lluvia)
    
    # 3. Exigimos que el resultado sea correcto
    assert recomendacion == "Lleva paraguas"


def test_cuando_hay_sol_recomienda_gafas():
    # 1. Creamos al doble de acción que finge que siempre hay sol
    def clima_falso_sol():
        return "Soleado"
        
    # 2. Le pasamos el doble
    recomendacion = decidir_que_ropa_usar(clima_falso_sol)
    
    # 3. Exigimos que el resultado sea correcto
    assert recomendacion == "Lleva gafas de sol"

# Como puedes ver, gracias a los Mocks, logramos probar TODAS las rutas de 
# nuestro código sin tener que esperar a que el clima real cambie, 
# y sin depender del internet.
