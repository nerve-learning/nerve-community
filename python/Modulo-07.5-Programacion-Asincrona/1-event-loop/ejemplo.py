import asyncio

# Esta es una función "especial" que el Event Loop puede controlar.
# Más adelante veremos qué significa exactamente 'async def', 
# por ahora, piensa que es una receta para el Jefe de Cocina.
async def tarea_principal():
    print("--- Inicio de la Tarea ---")
    print("1. El Jefe de Cocina entra al restaurante.")
    print("2. El Jefe revisa que todo esté en orden.")
    print("--- Fin de la Tarea ---")

# Código normal (síncrono)
print("--- Programa Normal ---")
print("Hola, estoy fuera del Event Loop.")

# Encendemos el Event Loop.
# Le decimos: "Jefe, por favor ejecute la tarea_principal"
print("\n--- Encendiendo el Event Loop ---")
asyncio.run(tarea_principal())

print("\n--- Apagando el programa ---")
print("El restaurante ha cerrado por hoy.")
