# Reto 05: El Explorador Blindado

Vas a intentar obtener datos de 2 APIs, pero una de ellas tiene una URL completamente inventada. Tu programa no debe morir.

### 📝 Instrucciones
1. Importa `asyncio` y `aiohttp`.
2. Crea `explorar(sesion, url)` que intente hacer un `.get(url)` usando el `sesion`.
3. Dentro de `explorar`, usa un bloque `try / except Exception as e:`. 
   - En el bloque `try`, haz la petición, y retorna el string `"Exito"`.
   - En el bloque `except`, imprime `"Ocurrió un error al conectar"` y retorna el string `"Fallo"`.
4. En tu `main()`, abre la sesión (`async with aiohttp.ClientSession() as sesion:`).
5. Usa `gather` para lanzar dos exploraciones al mismo tiempo:
   - Una a `"https://nerve.community.aleniastudios.me/laberinto/a1b2/x9.html"`
   - Otra a `"https://nerve.community.aleniastudios.me/laberinto/falsa-123.html"`
6. Guarda lo que retorna `gather` en una variable llamada `resultados`.
7. Imprime `resultados`.
8. Ejecuta `main()` con `asyncio.run()`.

### 🚫 Reglas
- **Permitido:** `import asyncio`, `import aiohttp`, `async def`, `try/except`, `await`, `gather`, `ClientSession`.
- **Obligatorio:** Usar `try` y `except` en la función `explorar`.

### 🎯 Resultado Esperado en Terminal
*(El orden de la lista final puede variar, pero debe sobrevivir e imprimir el error)*
```text
Ocurrió un error al conectar
Resultados: ['Exito', 'Fallo']
```
