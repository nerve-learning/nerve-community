# Teoría: El Supermercado HTML 🛒

Imagina que BeautifulSoup es un robot al que envías a un supermercado (la página web).
Si le dices: *"Tráeme un producto (`div`)"*, el robot traerá lo primero que vea en la entrada. Para ser precisos, usamos dos tipos de etiquetas:

### 1. El código de barras único: `id`
En HTML, un `id` es un identificador que **solo puede existir una vez** en toda la página. Es como el código de barras de un boleto ganador.
```python
# "Tráeme la etiqueta h1 que tenga el código de barras 'titulo-principal'"
unico = sopa.find('h1', id='titulo-principal')
```

### 2. La marca o categoría: `class` (clase)
Una `class` es una etiqueta que muchos elementos pueden compartir (ej. todos los productos en oferta tienen la clase "oferta").
```python
# "Tráeme la PRIMERA etiqueta p que pertenezca a la categoría 'precio'"
# ¡OJO! Fíjate que class lleva un guion bajo al final (class_)
primero = sopa.find('p', class_='precio')
```
*¿Por qué el guion bajo?* La palabra `class` es una palabra prohibida (reservada) en el lenguaje interno de Python. Si la escribimos sola, Python se confunde. Por eso, los creadores de BeautifulSoup inventaron `class_` con guion bajo.

### 3. Traerse todo el pasillo: `.find_all()`
¿Qué pasa si queremos **todos** los precios de la tienda? Usamos `find_all()` (encontrar todos).
Esta función es especial porque no te devuelve un solo recorte de texto... ¡Te devuelve una **Lista de Python** con todos los recortes adentro!

```python
# Esto nos da una Lista entera
carrito = sopa.find_all('p', class_='precio')

# Como aprendimos en el Módulo 4, recorremos la lista con un bucle for:
for producto in carrito:
    print(producto.text)
```

---

## ¿Qué pasa si me equivoco? (El Panel de Errores)

**Error 1: `AttributeError: 'ResultSet' object has no attribute 'text'`**
- **Por qué pasa:** Usaste `find_all()`, lo que te devolvió una Lista completa (un carrito de supermercado). Luego intentaste hacer `carrito.text`. ¡No puedes pedirle a un carrito entero de metal que te dé un texto! Tienes que sacar los productos uno por uno con un `for` y pedirle el `.text` a cada uno.
- **Solución:** Usa un bucle `for` siempre que uses `find_all()`.

**Error 2: `SyntaxError: invalid syntax` en tu `class="precio"`**
- **Por qué pasa:** Olvidaste el guion bajo. Escribiste `class="precio"` en vez de `class_="precio"`.
- **Solución:** Agrega el guion bajo al final de la palabra `class_`.
