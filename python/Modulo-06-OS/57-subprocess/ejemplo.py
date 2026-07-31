import subprocess

print("--- Inicio del Programa Maestro ---")
print("Soy el programa principal. Voy a despertar a un ayudante.\n")

# Preparamos las instrucciones para el ayudante en forma de lista
# Queremos que el sistema ejecute a Python y le pregunte su versión.
instrucciones = ["python", "--version"]

print("Enviando orden al ayudante...")
# Lanzamos el subproceso.
# capture_output=True: Guardamos lo que diga.
# text=True: Lo queremos como texto normal.
expediente = subprocess.run(instrucciones, capture_output=True, text=True)

print("El ayudante ha terminado su tarea.\n")

print("--- Revisando los Resultados ---")
# .stdout contiene el texto que el otro programa imprimió
print("El ayudante nos dijo:")
print(expediente.stdout)

print("--- Fin del Programa Maestro ---")
