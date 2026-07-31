import os

print("--- El Generador de Caos ---")
print("Hola. Yo no soy el organizador, ¡soy el niño travieso!")
print("Voy a crear un 'cuarto_desordenado' lleno de archivos de prueba.\n")

# 1. Definimos el nombre del cuarto
carpeta_caos = "cuarto_desordenado"

# 2. Si el cuarto no existe, lo construimos
if not os.path.exists(carpeta_caos):
    os.makedirs(carpeta_caos)

# 3. Lista de basura falsa para tirar en el cuarto
basura = [
    "gato_gracioso.jpg",
    "receta_pastel.txt",
    "paisaje.jpg",
    "contraseñas_no_leer.txt",
    "meme.jpg"
]

print("--- Tirando cosas al piso ---")
# 4. Soltamos cada archivo en la carpeta
for nombre in basura:
    # Pegamos la ruta: cuarto_desordenado + / + nombre
    ruta = os.path.join(carpeta_caos, nombre)
    
    # Creamos un archivo vacío solo para hacer bulto
    with open(ruta, "w") as archivo:
        archivo.write("Este es un archivo de prueba. No tiene nada útil.")
    
    print("Se ha tirado el archivo:", nombre)

print("\n--- Caos Terminado ---")
print("Si miras en tus carpetas, verás un 'cuarto_desordenado'.")
print("Tu reto será programar al robot limpiador en 'reto.py'. ¡Suerte!")
