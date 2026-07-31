# Lanzando todo al mismo tiempo

Si usamos `await tarea1()` y luego `await tarea2()`, el Event Loop espera a que termine la 1 para empezar la 2. Es como esperar a que hierva el agua para recién buscar la taza. ¡Un desperdicio de tiempo!

Para hacer ambas cosas al mismo tiempo (concurrentemente), usamos la herramienta: **`asyncio.gather()`**.

### Desmontaje Conceptual: `asyncio.gather()`
- `gather` significa "recolectar" o "agrupar" en inglés.
- **Sintaxis:** `await asyncio.gather(tarea_1(), tarea_2(), tarea_3())`
- **Qué significa para la computadora:** "Aquí tienes un grupo de tareas. Lánzalas TODAS al mismo tiempo. Pausa mi función actual (`await`) y no me despiertes hasta que TODAS las tareas de este grupo hayan terminado".

### ¿Por qué esto es revolucionario?
Si la tarea 1 tarda 3 segundos y la tarea 2 tarda 3 segundos:
- De forma normal: Tardan 6 segundos en total.
- Usando `gather`: Ambas inician juntas y terminan en 3 segundos en total.

### ¿Qué pasa si me equivoco?
Un error común es pasar la función sin los paréntesis: `await asyncio.gather(tarea_1, tarea_2)`. La computadora te dirá `TypeError: An asyncio.Future, a coroutine or an awaitable is required`. 
¡Debes pasar la **ejecución** de la función con los paréntesis `tarea_1()` para que `gather` la capture!
