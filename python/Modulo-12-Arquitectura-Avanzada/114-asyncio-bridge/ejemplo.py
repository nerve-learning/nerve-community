# Importante: Para que el puente funcione, necesitas dos cosas instaladas.
# En tu terminal ejecuta: 
# 1. pip install alenia-nerve
# 2. pip install websockets

# Importamos la herramienta del puente desde la sección especial de nerve
from nerve.bridge import NerveBridge
from nerve.core import NexusHub

# --- Título de la sección ---
print("--- 1. ENCENDIENDO EL CEREBRO PRINCIPAL ---")
# El puente no funciona solo, necesita conectarse a un Hub de Nerve.
# Así que primero levantamos nuestro Hub de siempre.
hub_principal = NexusHub()
hub_principal.start()
print("✅ Hub de Nerve encendido.")

# --- Título de la sección ---
print("--- 2. CONSTRUYENDO EL PUENTE WEB ---")
# Creamos el traductor.
# host="127.0.0.1" significa que es privado, solo para tu PC.
# port=50506 es la puerta por donde entrarán los navegadores web.
mi_puente = NerveBridge(host="127.0.0.1", port=50506)

print("🌉 El Puente está construido y esperando a páginas web...")
print("⚠️ (Presiona Ctrl+C en la terminal para detener el puente cuando quieras salir)")

# --- Título de la sección ---
print("--- 3. EL MALABARISTA EN ACCIÓN ---")
# .start() enciende el sistema asyncio por debajo.
# Nota importante: A diferencia de los clientes normales,
# .start() en el puente "atrapa" a tu programa aquí y lo deja corriendo
# infinitamente para poder atender a todas las páginas web.
# ¡Cualquier código que pongas debajo de start() no se ejecutará hasta que cierres el programa!
mi_puente.start()
