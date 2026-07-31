import logging

print("--- Iniciando el Sistema ---")
print("Preparando la bitácora silenciosa del programa...")

# 1. PREPARAMOS EL CUADERNO (basicConfig)
# filename: El nombre del archivo de texto.
# level: Queremos guardar desde mensajes de información (INFO) para arriba.
logging.basicConfig(filename="registro_del_sistema.txt", level=logging.INFO)

print("¡Bitácora lista! Ahora el programa trabajará en secreto.")
print("No verás los mensajes en la pantalla, se irán al archivo.")

print("--- Trabajando en Silencio ---")

# 2. ESCRIBIMOS MENSAJES (Estos no salen en la terminal)
# Un mensaje normal
logging.info("El sistema ha arrancado exitosamente.")

# Supongamos que ocurre un evento extraño pero no fatal
logging.warning("Se detectó un usuario sospechoso intentando entrar.")

# Supongamos que algo se rompe
logging.error("¡Fallo catastrófico! El servidor de café se ha desconectado.")

# Un último mensaje normal
logging.info("El sistema se está apagando.")

print("--- Fin del Programa ---")
print("El programa ha terminado. ¡Abre el archivo 'registro_del_sistema.txt' para ver lo que pasó!")
