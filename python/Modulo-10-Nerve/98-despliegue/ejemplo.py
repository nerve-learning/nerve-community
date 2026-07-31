import time
from nerve import NexusClient

print("--- EL CLUB VIP ---")
print("Este cliente intentará conectarse usando una contraseña directa en el código.")
print("Es útil para aprender, pero recuerda que no es lo más seguro.")

# Le pasamos la llave directamente al cliente
# (Si hubiera un Hub pidiendo contraseña, solo nos dejará entrar si coincide)
cliente_seguro = NexusClient(auth_token="codigo_secreto_777")

print("[*] Tocando la puerta del Hub...")

try:
    # Intentamos conectarnos.
    # Si el Hub tiene una contraseña distinta, esto fallará silenciosamente
    # o la conexión será rechazada.
    cliente_seguro.connect("invitado_vip")
    print("\n[✓] ¡Entramos al club VIP! La conexión fue exitosa.")
    print("Manteniendo la conexión viva. Presiona Ctrl+C para salir.")
    
    while True:
        time.sleep(1)

except Exception as e:
    print(f"\n[!] Error: No pudimos entrar. ¿El Hub está encendido y tiene la misma contraseña?")
    print(f"Detalle técnico: {e}")
