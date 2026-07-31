# --- 1. Preparación ---
# ¡ATENCIÓN! 
# Antes de correr este código, asegúrate de crear un archivo llamado "secreto.txt"
# en esta misma carpeta y escríbele algún texto misterioso adentro.

print("--- Intentando abrir el sobre secreto ---")

# 'with' es nuestro guardián. Cuidará que el archivo se cierre al final.
# 'open' abre el archivo "secreto.txt".
# La "r" significa que solo queremos Leer (Read).
# Le damos el apodo de 'sobre_abierto' para usarlo abajo.
with open("secreto.txt", "r") as sobre_abierto:
    
    print("¡Logré abrir el sobre!")
    print("Extrayendo la carta...\n")
    
    # Usamos la herramienta '.read()' de nuestro sobre abierto.
    # Eso saca TODO el texto y lo guardamos en la variable 'carta'
    carta = sobre_abierto.read()
    
    print("--- Contenido de la carta ---")
    
    # Ahora que lo tenemos en una variable, ¡podemos imprimirlo!
    print(carta)
    print("-----------------------------")
    
# ¿Notas que ya no hay espacios a la izquierda (indentación)?
# Al regresar a este nivel, 'with' automáticamente cerró el archivo por nosotros.
print("\n--- ¡Misión cumplida! El archivo ha sido cerrado de forma segura. ---")
