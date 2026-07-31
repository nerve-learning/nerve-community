# --- 1. Escribiendo desde cero (Modo "w") ---
print("--- Creando nuestro primer archivo ---")

# 'with' es el guardián.
# 'open' intentará abrir "nuevo_secreto.txt". Como no existe, ¡lo creará por ti!
# La "w" significa Write (Escribir). ¡Cuidado, borra todo si ya existía!
with open("nuevo_secreto.txt", "w") as archivo_nuevo:
    
    print("El archivo está abierto y el lápiz está listo.")
    
    # Usamos .write() para poner texto.
    archivo_nuevo.write("Esta es la primera linea del archivo.\n")
    
    # Recuerda poner \n al final de tu texto si quieres que la 
    # siguiente frase vaya en el renglón de abajo.
    archivo_nuevo.write("Esta es la segunda linea. ¡Mira qué bonito!\n")

# Al quitar la sangría (indentación), 'with' guarda y cierra el archivo.
print("Python guardó el archivo y cerró la caja.\n")


# --- 2. Agregando texto al final (Modo "a") ---
print("--- Agregando sin borrar ---")

# Ahora usamos la letra "a" de Append (Agregar o Anexar).
# Esto abrirá el mismo archivo que acabamos de crear, pero nos
# pondrá el lápiz al final de todo el texto que ya tiene.
with open("nuevo_secreto.txt", "a") as archivo_existente:
    
    print("Abriendo el archivo en modo agregar...")
    
    # Si olvidamos el \n, esto se pegaría justo después del signo '!' de arriba.
    archivo_existente.write("¡P.D: Acabo de agregar esta línea al final!\n")

print("--- ¡Revisa la carpeta de tu computadora! ---")
print("Deberías ver un archivo llamado 'nuevo_secreto.txt'. Ábrelo y mira adentro.")
