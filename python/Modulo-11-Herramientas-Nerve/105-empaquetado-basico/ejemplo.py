# Importamos la caja de herramientas del Sistema Operativo que ya conoces
import os

print("--- 1. Preparando nuestros secretos ---")
# Imagina que tenemos una carpeta llamada "documentos_secretos". 
# Usaremos comandos de terminal para crearla y poner un texto dentro.
# mkdir crea la carpeta. echo escribe un texto en un archivo.
os.system("mkdir -p documentos_secretos")
os.system('echo "La receta del cangrejo es..." > documentos_secretos/receta.txt')
print("Carpeta 'documentos_secretos' creada con éxito con nuestra receta dentro.")

print("\n--- 2. Guardando en la caja fuerte (.nrv) ---")
# Ahora, le diremos a la terminal que use Nerve para empacar nuestra carpeta.
# Usamos una variable de entorno temporal para pasar la clave de forma segura.
clave = "alenia_123"
origen = "documentos_secretos"
caja_fuerte = "boveda.nrv"

# Armamos el comando juntando las palabras. ¡Cuidado con los espacios!
# La f antes de las comillas (f-string) nos permite meter variables directamente en el texto usando {}.
comando_pack = f'NERVE_NRV_PASSWORD="{clave}" nerve pack {origen} {caja_fuerte}'

print(f"Ejecutando orden: {comando_pack}")
os.system(comando_pack)
print("¡Listo! Ahora tienes un archivo irrompible llamado 'boveda.nrv'.")

print("\n--- 3. Desempacando la caja fuerte en otro lugar ---")
# Queremos abrir la bóveda y poner su contenido en una carpeta nueva llamada "secretos_revelados"
destino = "secretos_revelados"

comando_unpack = f'NERVE_NRV_PASSWORD="{clave}" nerve unpack {caja_fuerte} {destino}'

print(f"Ejecutando orden: {comando_unpack}")
os.system(comando_unpack)
print("¡Mágia pura! El archivo fue abierto en la carpeta 'secretos_revelados'.")
print("Puedes revisar las carpetas de tu computadora para ver los archivos reales creados.")
