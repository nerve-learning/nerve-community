# El Poder de Pausar: async y await

En Python normal, una vez que una función empieza, no se detiene hasta terminar. 
Para que el Event Loop funcione, necesitamos decirle a Python en qué momentos puede "pausar" una tarea para ir a revisar otra.

### Desmontaje Conceptual: `async def` y `await`

**1. El símbolo `async`**
- **Sintaxis:** `async def mi_funcion():`
- **Qué significa para la computadora:** "Atención, esta no es una función normal. Esta función tiene permiso de ser pausada a la mitad. Es una función asíncrona (también llamada corrutina)".

**2. El símbolo `await`**
- **Sintaxis:** `await una_tarea_lenta()`
- **Qué significa para la computadora:** "Pausa esta función justo aquí. Ve a revisar si hay otra cosa que hacer en el Event Loop. Cuando `una_tarea_lenta` termine, regresa aquí y continúa en la siguiente línea".
- **Analogía:** Es como meter una pizza al horno, poner un cronómetro (`await`) y ponerte a lavar los platos en lugar de quedarte mirando el horno.

### Esperando inteligentemente
En módulos pasados usamos `time.sleep(5)` para pausar el código. Pero `time.sleep` bloquea TODO el programa. El cocinero se queda congelado.
La nueva herramienta es **`asyncio.sleep(5)`**.
Como es una tarea asíncrona que tarda, SIEMPRE debemos ponerle `await` antes:
`await asyncio.sleep(5)`

### ¿Qué pasa si me equivoco?
El error más común es olvidar la palabra `await` antes de llamar a otra función asíncrona. 
Si haces `asyncio.sleep(2)` sin el `await`, la computadora te lanzará una advertencia `RuntimeWarning: coroutine 'sleep' was never awaited` y **no esperará nada de tiempo**. Python dirá: "Me diste la tarea, pero nunca me pediste que me detuviera a esperarla".
