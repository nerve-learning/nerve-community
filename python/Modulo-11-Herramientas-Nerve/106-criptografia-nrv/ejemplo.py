# Importamos la herramienta para hablar con nuestro Sistema Operativo
import os

print("--- 1. El problema de las llaves débiles ---")
# Si usamos una clave como "123", un hacker entrará rápido.
print("Las llaves débiles son como cerrar la puerta de tu casa con cinta adhesiva.")

print("\n--- 2. Forjando una llave estilo 'Robots' (Modo Random) ---")
# Le pedimos a Nerve que cree una clave de letras y símbolos raros.
# Usamos la bandera --mode y la opción random para que sea 100% al azar.
comando_robot = "nerve genpass --mode random"
print(f"Le daremos la orden a la terminal: {comando_robot}")
print("Tu llave generada es:")

# os.system ejecutará la orden y Nerve imprimirá el resultado en tu pantalla automáticamente.
os.system(comando_robot)

print("\n--- 3. Forjando una llave estilo 'Humanos' (Modo Passphrase) ---")
# Los símbolos raros son muy difíciles de memorizar. 
# Podemos pedirle a Nerve una "frase secreta" (passphrase) que junta palabras reales.
comando_humano = "nerve genpass --mode passphrase"
print(f"Le daremos la orden a la terminal: {comando_humano}")
print("Tu frase secreta es:")

os.system(comando_humano)

print("\n--- 4. Conclusión ---")
print("Ahora tienes las herramientas para nunca más usar contraseñas débiles cuando uses 'nerve pack'.")
