# Importamos nuestra vieja amiga, la caja de herramientas del OS
import os

print("--- 1. Atrapando la llave en el aire ---")
print("Vamos a pedirle a Nerve que invente una frase secreta.")
print("Pero esta vez, en lugar de os.system, usaremos os.popen para atraparla.")

# Abrimos el túnel, leemos la respuesta y recortamos los bordes
mi_super_llave = os.popen("nerve genpass --mode passphrase").read().strip()

print("\n¡La atrapamos! Nerve no la imprimió en pantalla directamente.")
print("Ahora Python la tiene guardada en su cerebro. Mírala:")
print(f"--> {mi_super_llave} <--")


print("\n--- 2. Automatizando la Seguridad ---")
# Vamos a crear una caja rápida para guardar cosas.
os.system("mkdir -p boveda_auto")
os.system('echo "Dinero virtual" > boveda_auto/cuentas.txt')

print("Empacando la bóveda usando la llave atrapada...")
# Armamos el comando de empaquetado usando nuestra variable 'mi_super_llave'
# ¡Todo se hace solo, sin interacción humana!
comando_proteger = f'NERVE_NRV_PASSWORD="{mi_super_llave}" nerve pack boveda_auto caja_fuerte.nrv'
os.system(comando_proteger)

print("\n¡Misión cumplida!")
print("Has logrado que tu programa cree su propia llave segura y proteja sus propios archivos automáticamente.")
