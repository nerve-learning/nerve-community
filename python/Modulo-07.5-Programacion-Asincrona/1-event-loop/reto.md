# Reto 01: Tu primer restaurante

Eres el dueño de un nuevo restaurante. Quieres hacer una pequeña simulación de cómo el Jefe de Cocina abre el local.

### 📝 Instrucciones
1. Importa la librería necesaria para usar el Event Loop.
2. Crea una función asíncrona llamada `abrir_restaurante()`.
   - Recuerda: para crearla, usa `async def` en lugar de solo `def`.
3. Dentro de la función, usa `print()` para imprimir tres mensajes:
   - "Encendiendo luces..."
   - "Limpiando mesas..."
   - "¡Restaurante abierto!"
4. Fuera de la función, usa la herramienta del Event Loop para ejecutar tu función (`run`).

### 🚫 Reglas
- **Permitido:** `import asyncio`, `async def`, `print()`, `asyncio.run()`.
- **Prohibido:** Usar funciones normales (`def`) para la tarea principal.

### 🎯 Resultado Esperado en Terminal
```text
Encendiendo luces...
Limpiando mesas...
¡Restaurante abierto!
```
