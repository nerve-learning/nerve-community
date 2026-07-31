# Reto 06: Scraper de Datos (El Jefe Final)

Es hora de extraer datos de la API pública de pruebas de Alenia Studios de forma concurrente.

### 📝 Instrucciones
1. Importa `asyncio` y `aiohttp`.
2. Tienes una lista de rutas que debes visitar en el sitio principal:
   ```python
   base_url = "https://nerve.community.aleniastudios.me"
   rutas = ["/laberinto/a1b2/x9.html", "/laberinto/8f4c/k3.html", "/laberinto/tz99/data-401.html"]
   ```
3. Crea una función asíncrona `descargar_ruta(sesion, url)`:
   - Haz la petición `get` usando el bloque `try/except`.
   - Lee el contenido como texto (con `await respuesta.text()`).
   - Imprime un mensaje diciendo cuántos caracteres tiene el texto descargado de esa url. (Ejemplo: `len(texto)` para obtener la cantidad).
   - Si falla, en el except imprime que hubo un error.
4. Crea la función `main()`:
   - Imprime "Iniciando extracción masiva..."
   - Abre la sesión de `aiohttp` (`async with`).
   - Usa un bucle `for` para recorrer las `rutas`, armar la url completa (`base_url + ruta`), y añadir la tarea `descargar_ruta` a una lista de tareas.
   - Ejecuta todas las tareas simultáneamente con `await asyncio.gather(*tareas)`.
   - Al final imprime "Extracción finalizada."
5. Usa `asyncio.run()` para ejecutar `main()`.

### 🚫 Reglas
- **Permitido:** `import asyncio`, `import aiohttp`, `async def`, `await`, `gather`, `try/except`, `ClientSession`, bucles `for`, `print()`, `len()`.
- **Prohibido:** Hacerlo de forma síncrona (hacer un `await` dentro del `for` uno por uno). Debes crear una lista de tareas y usar `gather` al final.

### 🎯 Resultado Esperado en Terminal
*(El orden en el que se imprimen y la cantidad de caracteres puede variar ligeramente si la API se actualiza, lo importante es que todos respondan)*
```text
Iniciando extracción masiva...
URL: https://nerve.community.aleniastudios.me/laberinto/a1b2/x9.html - Descargados 543 caracteres.
URL: https://nerve.community.aleniastudios.me/laberinto/tz99/data-401.html - Descargados 1205 caracteres.
URL: https://nerve.community.aleniastudios.me/laberinto/8f4c/k3.html - Descargados 890 caracteres.
Extracción finalizada.
```
