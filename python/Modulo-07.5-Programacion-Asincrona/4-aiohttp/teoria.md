# aiohttp: Internet sin esperas

Para usar el internet asíncrono, necesitamos una librería externa especial.
Debes abrir tu terminal y escribir: `pip install aiohttp`

### ¿Por qué no usar `requests`?
Si usas `requests.get()` dentro de una función asíncrona, tu Event Loop quedará **congelado** esperando al servidor. Es como si el Jefe de Cocina se quedara hablando por teléfono con el proveedor y no dejara trabajar a nadie más. `aiohttp` le permite al Jefe colgar, ir a cocinar, y que el teléfono suene cuando el proveedor tenga la respuesta.

### Desmontaje Conceptual: `ClientSession` y `async with`

En `aiohttp`, hacemos peticiones abriendo una "Sesión" que mantiene la conexión abierta de forma eficiente. Usamos una estructura que aprendimos con los archivos (`with open(...)`), pero ahora en su versión asíncrona: `async with`.

**Sintaxis:**
```python
async with aiohttp.ClientSession() as sesion:
    async with sesion.get("https://api.com/datos") as respuesta:
        texto = await respuesta.text()
```

- **`async with`:** Le dice a la computadora: "Abre este recurso (la sesión o la conexión). Puede que abrirlo tome tiempo, así que pausa (`async`) si es necesario. Cuando termine de usar el bloque indentado, ciérralo automáticamente".
- **`await respuesta.text()`:** Extraer el texto de internet tarda (hay que descargar los datos). Por eso, *siempre* usamos `await` para leer el contenido. (Si fueran datos en formato JSON, usaríamos `await respuesta.json()`).

### ¿Qué pasa si me equivoco?
Si intentas leer el texto con `respuesta.text()` sin usar `await`, la computadora no te dará un string con el contenido, te dará un objeto extraño `<coroutine object ...>`. ¡Recuerda que todo lo que toma tiempo en red necesita un `await`!
