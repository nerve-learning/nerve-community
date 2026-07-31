# --- 1. Preparando la mudanza ---
# Traemos la herramienta de mudanzas pesadas
import shutil

print("--- Creando el archivo original ---")
# Usamos lo que ya sabemos para crear un archivo real que podamos mover
with open("original.txt", "w") as archivo:
    archivo.write("Este es un tesoro muy valioso. ¡Cuidalo!\n")

print("Archivo 'original.txt' creado con éxito.")


# --- 2. Haciendo una copia de seguridad ---
print("\n--- Clonando el tesoro ---")

# Usamos shutil.copy(). Le damos el nombre original, y el nombre de la copia.
shutil.copy("original.txt", "respaldo.txt")

print("¡Listo! Ahora tenemos un clon exacto llamado 'respaldo.txt'.")
print("Si miras tu carpeta, ¡habrá dos archivos idénticos!")


# --- 3. Moviendo / Renombrando ---
print("\n--- Renombrando el clon ---")

# Usamos shutil.move(). Tomamos la copia y la escondemos con otro nombre.
# Como no lo estamos mandando a otra carpeta distinta, 
# la computadora simplemente le cambiará el nombre.
shutil.move("respaldo.txt", "super_secreto.txt")

print("¡Magia! 'respaldo.txt' ha desaparecido y ahora se llama 'super_secreto.txt'.")

print("\n--- ¡Operativo de mudanza completado! ---")
