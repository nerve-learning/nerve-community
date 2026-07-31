# Importamos pandas usando su apodo oficial mundial: pd
import pandas as pd

print("--- 1. Preparando la misión ---")
url_paises = "https://en.wikipedia.org/wiki/List_of_continents_by_population"

# Wikipedia bloquea a las aspiradoras de datos si no se identifican.
# Como vimos en el Nivel 66, nos disfrazamos usando un diccionario:
opciones_de_red = {"User-Agent": "Mozilla/5.0"}


print("\n--- 2. Encendiendo la aspiradora ---")
print("Aspirando las tablas de Wikipedia... (Tomará unos segundos)")

# read_html va a la web y busca todas las etiquetas <table>
# Le pasamos la URL y nuestras opciones de red para que nos dejen entrar
lista_de_tablas = pd.read_html(url_paises, storage_options=opciones_de_red)

# Podemos usar len() que aprendimos en el Módulo 3 para ver cuántas hay
cantidad_tablas = len(lista_de_tablas)
print(f"¡Éxito! Encontramos {cantidad_tablas} tablas diferentes en esta página.")


print("\n--- 3. Inspeccionando el botín ---")
# Extraemos la tabla que nos interesa. En Wikipedia, la tabla principal a veces es la 0,
# pero en esta página en particular es la 1.
tabla_continentes = lista_de_tablas[1]


print("\n--- 4. Mostrando los resultados limpios ---")
# Usamos .head() para no imprimir cientos de líneas en nuestra pantalla
# Solo queremos ver la "cabeza" (las primeras 5 filas) para confirmar que funcionó.
print(tabla_continentes.head())

print("\n¡Mira esa belleza! Filas y columnas perfectamente ordenadas sin usar BeautifulSoup.")
