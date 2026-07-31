# Teoría: Llamando al Restaurante de Internet ☎️🍕

Imagina que quieres pedir una pizza. No puedes mágicamente hacer que la pizza aparezca en tu mesa. Necesitas:
1. Un teléfono.
2. El número del restaurante (la dirección).
3. Hacer la llamada pidiendo el menú.
4. Escuchar la respuesta del restaurante.

En Python, hacer que tu programa pida datos a Internet es exactamente igual.

### 1. El Teléfono: `requests`
Python no trae el teléfono activado por defecto. Tenemos que importarlo. Usamos una librería llamada `requests` (que significa "peticiones").

### 2. El Número del Restaurante: `URL`
Las direcciones en Internet se llaman URLs (ej: `https://pokeapi.co/...`). Es el número al que vamos a llamar.

### 3. Haciendo la llamada: `.get()`
Para llamar, usamos `requests.get(url)`.  
La palabra `get` significa "obtener". Le estamos diciendo a Python: "Ve a esta dirección y **obtén** lo que tengan ahí".

### 4. Escuchando la respuesta: `.json()`
Cuando el servidor responde, a menudo nos manda los datos en un formato universal llamado **JSON** (es como el idioma internacional de Internet). 
Pero nosotros en Python trabajamos con **Diccionarios** (¿recuerdas las listas con llaves y valores?).
Usamos el método `.json()` para decirle a Python: *"Traduce lo que nos mandaron en JSON y conviértelo en un Diccionario de Python para poder usarlo"*.

---

## Anatomía de la Petición

```python
import requests  # 1. Traemos el teléfono

url = "https://api.clima.com/hoy" # 2. Anotamos el número a llamar

respuesta = requests.get(url) # 3. Hacemos la llamada y guardamos lo que nos contestan en 'respuesta'

diccionario = respuesta.json() # 4. Traducimos la respuesta a un diccionario de Python
```

### Los Símbolos Nuevos:
- `requests.get()`: El punto `.` significa "del módulo requests, usa la herramienta get".
- `.json()`: Los paréntesis `()` al final significan "ejecuta la acción de traducir ahora mismo". Si olvidas los paréntesis, Python no hará la traducción.

---

## ¿Qué pasa si me equivoco? (El Panel de Errores)

**Error 1: `requests.exceptions.MissingSchema: Invalid URL`**
- **Por qué pasa:** Olvidaste poner `http://` o `https://` al principio de tu URL. Python no sabe si estás intentando abrir un archivo local o llamando a Internet.
- **Solución:** Asegúrate de que tu URL empiece con `https://`.

**Error 2: `json.decoder.JSONDecodeError`**
- **Por qué pasa:** Llamaste a `.json()` en una página web normal (como `https://google.com`), que te devuelve código de página web (HTML), no datos en formato JSON.
- **Solución:** Asegúrate de que la URL a la que llamas está diseñada para devolver datos (lo que llamamos una "API").

**Error 3: `NameError: name 'requests' is not defined`**
- **Por qué pasa:** Olvidaste poner `import requests` al principio del archivo. Python no sabe qué es ese "teléfono" que intentas usar.
- **Solución:** Importa siempre el módulo arriba del todo.
