import requests
import time

print("--- 1. El programador impaciente ---")
# El servidor httpbin.org tiene una URL especial de pruebas que 
# simula estar enojada siempre, devolviéndonos un error 429.
url_castigo = "https://httpbin.org/status/429"

# Hacemos la petición
respuesta_rapida = requests.get(url_castigo)
print(f"El cantinero responde con el código: {respuesta_rapida.status_code}")

# Comprobamos si nos pasamos de la raya
if respuesta_rapida.status_code == 429:
    print("❌ ¡Demasiadas peticiones! Nos han mandado a la silla de pensar.")


print("\n--- 2. El programador educado ---")
# Ahora usaremos una URL normal que siempre funciona
url_normal = "https://httpbin.org/get"

# Vamos a hacer 3 peticiones en cadena usando un bucle for
for numero_peticion in range(1, 4):
    print(f"\nHaciendo la petición número {numero_peticion}...")
    
    # Hacemos la llamada al servidor
    respuesta = requests.get(url_normal)
    
    if respuesta.status_code == 200:
        print("✅ El servidor nos atendió con una sonrisa.")
    
    # LA REGLA DE ORO DEL SCRAPING:
    # Ser cortés y dormir el programa antes de la siguiente vuelta del bucle.
    print("😴 Durmiendo 2 segundos para no estresar al servidor...")
    time.sleep(2)

print("\n--- ¡Bucle Terminado! ---")
print("Descargamos mucha información y el servidor nunca se molestó.")
