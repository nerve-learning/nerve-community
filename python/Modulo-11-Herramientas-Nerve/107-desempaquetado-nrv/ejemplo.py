# Importamos la herramienta para hablar con nuestro Sistema Operativo
import os

print("--- 1. Enseñándole a tu computadora ---")
# Le decimos a Nerve que asocie los archivos .nrv a su propio programa.
comando_asociar = "nerve associate"
print(f"Ejecutando: {comando_asociar}")
os.system(comando_asociar)
print("¡Tu sistema ahora reconoce a Nerve! Si ves un .nrv en tus carpetas, tendrá un ícono.")

print("\n--- 2. Creando un cofre de prueba ---")
# Creamos algo rápido para probar
os.system("mkdir -p sorpresa")
os.system('echo "¡Aparecí!" > sorpresa/magia.txt')

# Lo empacamos de la forma tradicional que ya aprendimos
clave = "abracadabra"
print(f"Guardando el secreto en 'misterio.nrv' con la clave: {clave}")
os.system(f'NERVE_NRV_PASSWORD="{clave}" nerve pack sorpresa misterio.nrv')

print("\n--- 3. Abriendo el cofre como un humano ---")
# Usaremos 'nerve open'. 
# ¡ATENCIÓN! Tu código de Python se va a PAUSAR en la siguiente línea.
# Nerve tomará el control y esperará a que el humano (tú) escriba la contraseña.
comando_abrir = "nerve open misterio.nrv"
print("👇 ¡Mira abajo! El programa se pausará. Escribe 'abracadabra' y presiona Enter.")

# Al ejecutar esto, interactuarás directamente con Nerve
os.system(comando_abrir)

print("\n¡Desempaquetado exitoso!")
print("Como ves, 'nerve open' es genial para cuando tu programa necesita interactuar con el usuario.")
