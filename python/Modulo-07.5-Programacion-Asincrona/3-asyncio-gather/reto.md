# Reto 03: Carrera Concurrente

Vamos a hacer que dos "corredores" corran al mismo tiempo.

### 📝 Instrucciones
1. Importa `asyncio`.
2. Crea una función asíncrona `corredor(nombre, tiempo_tardanza)`:
   - Imprime que el `nombre` empezó a correr.
   - Haz que espere (con `await asyncio.sleep`) el `tiempo_tardanza`.
   - Imprime que el `nombre` llegó a la meta.
3. Crea la función asíncrona `carrera()`:
   - Usa `await asyncio.gather()` para lanzar a dos corredores a la vez:
     - El corredor "Rayo" que tarda 1 segundo en llegar.
     - El corredor "Tortuga" que tarda 3 segundos en llegar.
   - Al final de `gather`, imprime "¡La carrera ha terminado!".
4. Usa `asyncio.run()` para iniciar la `carrera()`.

### 🚫 Reglas
- **Permitido:** `import asyncio`, `async def`, `await`, `asyncio.sleep()`, `asyncio.gather()`, `asyncio.run()`, `print()`.
- **Prohibido:** Usar `await corredor(...)` de forma aislada. Debes usar `asyncio.gather()` para que arranquen juntos.

### 🎯 Resultado Esperado en Terminal
*(Ambos empezarán al mismo tiempo, Rayo llegará primero, luego de una pausa llegará Tortuga)*
```text
Rayo empezó a correr.
Tortuga empezó a correr.
Rayo llegó a la meta.
Tortuga llegó a la meta.
¡La carrera ha terminado!
```
