from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

print("--- 1. Confeccionando el traje de fantasma ---")
# Primero, preparamos las opciones
opciones_fantasma = Options()

# Agregamos la regla de invisibilidad
opciones_fantasma.add_argument("--headless")
print("✅ Traje invisible listo.")


print("\n--- 2. Invocando al navegador ---")
# Creamos el navegador entregándole nuestro traje
print("Abriendo Chrome... (¡No verás que se abra ninguna ventana!)")
navegador = webdriver.Chrome(options=opciones_fantasma)
print("✅ ¡El navegador está ejecutándose en las sombras!")


print("\n--- 3. Viajando por la web ---")
url_destino = "https://www.python.org"
print(f"Viajando silenciosamente a {url_destino}...")

# Hacemos que el navegador visite la página
navegador.get(url_destino)

# Vamos a comprobar que el navegador realmente fue a la página
# extrayendo el título de la pestaña actual.
titulo_leido = navegador.title

print("¡Lectura exitosa!")
print(f"👉 El título de la página oculta es: '{titulo_leido}'")


print("\n--- 4. Desapareciendo ---")
# REGLA DE ORO: Un navegador fantasma que no se cierra,
# se queda comiendo memoria RAM para siempre en tu computadora.
navegador.quit()
print("✅ El navegador fantasma ha abandonado este mundo de forma segura.")
