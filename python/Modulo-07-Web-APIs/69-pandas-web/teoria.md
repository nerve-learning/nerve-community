# Teoría: La Aspiradora Mágica 🧹

En HTML, las tablas de datos se construyen con una etiqueta especial llamada `<table>`.
Pandas tiene una herramienta construida específicamente para cazar estas etiquetas. No le importa el color de la página, ni las imágenes; solo entra, aspira todas las etiquetas `<table>` y te las entrega listas para usar.

### Anatomía de la Extracción

```python
import pandas as pd

url = "https://mi-sitio.com"

# Usamos el diccionario de cabeceras (Nivel 66) para que no nos bloqueen
mis_opciones = {"User-Agent": "Mozilla/5.0"}

# Le pasamos la url a la aspiradora y le damos nuestras opciones
tablas = pd.read_html(url, storage_options=mis_opciones)

mi_tabla = tablas[0]
print(mi_tabla.head())
```

**Desmontaje Conceptual:**
- `import pandas as pd`: Estamos importando la librería `pandas`, pero usando la palabra mágica `as` le ponemos un **apodo** (alias). Le decimos a la computadora: *"Importa pandas, pero llámalo `pd` para no escribir tanto"*.
- `storage_options`: Es un parámetro interno de pandas donde podemos pasarle diccionarios de cabeceras de red (igual que en `requests`).
- `pd.read_html()`: Es la aspiradora. Lee la página y devuelve una **Lista** normal de Python que contiene todas las tablas que encontró. 
- `tablas[0]`: Como la aspiradora devuelve una lista, usamos los corchetes `[0]` que aprendimos en el Módulo 3 para sacar el primer elemento (la primera tabla).
- `.head()`: Las tablas pueden tener miles de filas. El método `.head()` (cabeza, en inglés) le dice a la tabla: *"Muéstrame solo tus primeras 5 filas (tu cabeza)"* para que la terminal no se sature.

---

## ¿Qué pasa si me equivoco? (El Panel de Errores)

**Error 1: `IndexError: list index out of range` al hacer `tablas[0]`**
- **Por qué pasa:** Le dijiste a Pandas que aspirara la URL, pero Pandas te está gritando: *"¡Oye, la lista está vacía!"*. Esto significa que la página web NO tenía ninguna etiqueta `<table>` real.
- **Solución:** Busca sitios que realmente tengan tablas tradicionales.

**Error 2: `HTTPError: HTTP Error 403: Forbidden`**
- **Por qué pasa:** Olvidaste pasarle el `storage_options` con el `User-Agent`. El sitio web se dio cuenta de que eres un robot (Pandas) y te cerró la puerta en la cara.
