print("--- Inicio del Show ---")
print("El acróbata está caminando por el piso (código seguro).")

print("\n--- Subiendo al Trapecio ---")

# Le avisamos a Python que vamos a hacer algo arriesgado
try:
    manzanas = 10
    ninos = 0
    print("Intentando repartir", manzanas, "manzanas entre", ninos, "niños...")
    
    # ¡BOM! Las computadoras odian dividir por cero. Esto causará un error.
    resultado = manzanas / ninos
    
    # Esta línea NUNCA se va a ejecutar, porque el programa saltó 
    # a la red de rescate en el momento exacto en que falló la división.
    print("Cada niño recibe:", resultado)
    
# Aquí está nuestra red de seguridad. Atrapamos el "Error" y lo guardamos en la variable "e"
except Exception as e:
    print("¡Oh no! El acróbata resbaló. Pero cayó en la red de seguridad.")
    print("El reporte médico (el error técnico) dice:", e)

print("\n--- El Show Continúa ---")
print("Como atrapamos el error a tiempo, el programa no explotó.")
print("Podemos seguir trabajando normalmente.")
