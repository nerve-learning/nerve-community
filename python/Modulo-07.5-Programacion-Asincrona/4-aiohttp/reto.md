# Reto 04: Petición Concurrente al Espacio

Vamos a preguntar cuántas personas hay en el espacio usando una API pública.

### 📝 Instrucciones
1. Abre tu terminal y asegúrate de tener `aiohttp` instalado (`pip install aiohttp`).
2. Importa `asyncio` y `aiohttp`.
3. Crea una función asíncrona `obtener_astronautas()`.
4. Adentro, usa `async with aiohttp.ClientSession() as sesion:`
5. Luego, haz una petición GET a la url: `"http://api.open-notify.org/astros.json"` usando `async with sesion.get(url) as respuesta:`
6. Usa `await respuesta.json()` para extraer los datos y guárdalos en una variable llamada `datos`.
7. Imprime el valor de la clave `"number"` del diccionario `datos`. (Ejemplo: `print(f"Hay {datos['number']} astronautas en el espacio.")`).
8. Crea la función `main()` y llama a tu función usando `await`. Ejecuta `main()` con `asyncio.run()`.

### 🚫 Reglas
- **Permitido:** `import asyncio`, `import aiohttp`, `async def`, `async with`, `await`, `asyncio.run()`.
- **Prohibido:** Usar `requests`.
- **Obligatorio:** Usar `async with` para la sesión y para la petición.

### 🎯 Resultado Esperado en Terminal
*(El número exacto puede variar dependiendo del día)*
```text
Hay 10 astronautas en el espacio.
```
