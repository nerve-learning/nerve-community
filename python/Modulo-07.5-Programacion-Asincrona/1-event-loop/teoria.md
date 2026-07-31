# El Jefe de la Cocina (Event Loop)

Hasta ahora, tus programas en Python hacían una cosa a la vez. Como un cocinero novato:
1. Pone la carne en el fuego.
2. Se queda mirando la carne por 10 minutos (sin hacer nada más).
3. Saca la carne.
4. Pone a tostar el pan.

Esto se llama **Programación Síncrona** (o bloqueante). Si algo tarda, todo el programa se congela.

### La Programación Asíncrona
Es la capacidad de decir: "Oye, esto va a tardar. Avísame cuando termine, mientras tanto voy a hacer otra cosa". 

### ¿Qué es el Event Loop?
El **Event Loop** (Bucle de Eventos) es el cerebro que hace esto posible. Imagínalo como el Jefe de Cocina:
- Constantemente está dando vueltas (loop) preguntando: "¿La carne ya está? No. ¿El pan ya está? Sí, sácalo".
- Organiza qué tarea se ejecuta y cuál debe esperar.

### Anatomía del nuevo código
Para usar el Event Loop, Python tiene una herramienta integrada llamada `asyncio` (Asynchronous I/O - Entradas y Salidas Asíncronas).

```python
import asyncio
```

El símbolo clave de hoy es `asyncio.run()`.
- **Qué significa para la computadora:** "Enciende el Bucle de Eventos, ejecuta esta tarea principal, y cuando termines, apaga el Bucle".

### ¿Qué pasa si me equivoco?
El error más común es olvidar importar `asyncio` o intentar ejecutar funciones asíncronas de la manera normal. Si ves un error como `RuntimeWarning: coroutine was never awaited` o `<coroutine object at 0x...>`, significa que olvidaste llamar al Jefe de Cocina (`asyncio.run()`).
