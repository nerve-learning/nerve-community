from bs4 import BeautifulSoup

print("--- 1. Entrando a la Tienda Mágica (HTML) ---")
# Observa detenidamente este HTML.
# Tiene 'id' para cosas únicas, y 'class' para cosas repetidas.
html_tienda = """
<html>
  <body>
    <h1 id="bienvenida">Bienvenidos a la Tienda de Hechicería</h1>
    
    <div class="producto">
      <h2>Poción de Vida</h2>
      <p class="precio">$50</p>
    </div>
    
    <div class="producto">
      <h2>Espada de Madera</h2>
      <p class="precio">$15</p>
    </div>
    
    <div class="producto">
      <h2>Escudo de Hierro</h2>
      <p class="precio">$120</p>
    </div>
  </body>
</html>
"""
sopa = BeautifulSoup(html_tienda, 'html.parser')
print("Página procesada con éxito.")


print("\n--- 2. Buscando algo ÚNICO (id) ---")
# Usamos id para encontrar la etiqueta con el mensaje de bienvenida.
# Sabemos que solo hay uno en toda la página.
letrero = sopa.find('h1', id='bienvenida')
print(f"El letrero dice: {letrero.text}")


print("\n--- 3. El problema de buscar sin cuidado ---")
# Si solo buscamos un 'p', nos dará el primero que encuentre (la poción).
# ¡Ignorará el resto de la tienda!
primer_precio = sopa.find('p', class_='precio')
print(f"Búsqueda simple solo encontró un precio: {primer_precio.text}")


print("\n--- 4. Saqueando toda la tienda (find_all) ---")
# Usamos find_all() para atrapar TODOS los párrafos con clase 'precio'.
# Esto nos devuelve una LISTA de etiquetas.
lista_precios = sopa.find_all('p', class_='precio')

print(f"¡Atrapamos {len(lista_precios)} precios en total!")
print("Revisando el carrito:")

# Como 'lista_precios' es una lista, usamos nuestro viejo amigo el bucle 'for'
for etiqueta_precio in lista_precios:
    # A cada etiqueta individual SÍ le podemos sacar el texto
    print(f"- Cuesta: {etiqueta_precio.text}")

print("\n--- ¡Misión Cumplida! ---")
