# De la caja bs4, importa solo la herramienta BeautifulSoup
from bs4 import BeautifulSoup

print("--- 1. El periódico desordenado (HTML) ---")
# Esto es lo que verías si miras el código de una página web cruda.
# Está lleno de 'etiquetas' de formato enceradas en símbolos < >.
html_crudo = """
<html>
  <head>
    <title>Mi Gran Página</title>
  </head>
  <body>
    <h1>Noticia de Última Hora</h1>
    <p>Un estudiante de Python aprende a raspar la web.</p>
  </body>
</html>
"""
print("Tenemos el HTML desordenado en nuestra memoria.")


print("\n--- 2. Preparando la Sopa ---")
# Le entregamos el texto sucio a BeautifulSoup.
# 'html.parser' le indica a la herramienta que estamos leyendo reglas web (HTML).
sopa = BeautifulSoup(html_crudo, 'html.parser')
print("Sopa mágica preparada y lista para buscar.")


print("\n--- 3. Recortando etiquetas ---")
# find() busca de arriba a abajo y se detiene en el primer resultado que coincida.
# 'title' suele ser el nombre de la pestaña en el navegador.
recorte_titulo = sopa.find('title')

# 'h1' (Header 1) suele ser el titular gigante de la página.
recorte_h1 = sopa.find('h1')

print("¡Cuidado! Los recortes todavía tienen las feas etiquetas HTML:")
print(recorte_titulo)
print(recorte_h1)


print("\n--- 4. Limpiando la información (.text) ---")
# .text borra toda la basura de los lados < > y nos deja el oro puro.
titulo_limpio = recorte_titulo.text
h1_limpio = recorte_h1.text

print(f"Título de la pestaña: {titulo_limpio}")
print(f"Titular principal: {h1_limpio}")

print("\n--- ¡Magia completada! ---")
