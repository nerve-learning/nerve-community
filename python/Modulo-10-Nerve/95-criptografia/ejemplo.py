import os
# Paso 1: Importamos las herramientas de criptografía
from nerve import pack_nrv, unpack_nrv

print("--- 1. Creando nuestro documento ultrasecreto ---")
# Vamos a crear un archivo normal, como lo vimos en el Módulo 06.
nombre_archivo = "planos_secretos.txt"

# Usamos 'open' con la 'w' (write) para escribir texto.
with open(nombre_archivo, "w") as archivo:
    archivo.write("El tesoro está enterrado debajo de la palmera gigante.")

print(f"Documento '{nombre_archivo}' creado. Cualquiera puede leerlo ahora mismo.")


print("\n--- 2. Empaquetando en la Caja Fuerte (Encriptación) ---")
# Inventamos nuestra contraseña maestra
password_maestra = "AbreteSesamo2024"
caja_fuerte = "tesoro.nrv"

print("Llamando a los cerrajeros matemáticos de Nerve...")
# ¡MAGIA! Convertimos el archivo de texto en una caja fuerte .nrv
pack_nrv(nombre_archivo, caja_fuerte, password_maestra)

print(f"¡Éxito! Hemos creado la caja fuerte: {caja_fuerte}")

# Ahora, borraremos el archivo original para que nadie lo pueda leer
os.remove(nombre_archivo)
print("Hemos destruido el documento original. Solo sobrevive la caja fuerte.")


print("\n--- 3. Desempaquetando la Caja Fuerte (Desencriptación) ---")
print("Intento de abrir la caja fuerte...")

# Elegimos una carpeta donde queremos que se extraigan los archivos
carpeta_salida = "extraccion"

# Usamos la misma contraseña para abrirla
unpack_nrv(caja_fuerte, carpeta_salida, password_maestra)

print(f"¡Caja abierta! Revisa la carpeta '{carpeta_salida}'.")
print("--- Fin del Ejemplo ---")
