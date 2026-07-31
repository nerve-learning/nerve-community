# Reto Nivel 99: El Sensor Inteligente 🌡️

Imagina que estás construyendo un nodo sensor que lee la temperatura y se la envía al Hub. Quieres enviar los datos súper rápido, pero te acaban de informar que el administrador del Hub ha activado los límites de velocidad.

## Instrucciones

1. Crea o modifica tu archivo `nerve.config` para que contenga **exclusivamente**:
   `rate_limit_messages_per_sec=2`
2. Escribe un script llamado `hub_estricto.py`. Simplemente importa `NexusHub`, instáncialo y arráncalo con `.start()`.
3. Escribe tu script `sensor.py`:
   - Conéctalo a la red como `"sensor_temp"`.
   - Crea un bucle `while True:` infinito.
   - Adentro del bucle, haz que imprima "Enviando temperatura..." y transmita un mensaje: `.broadcast({"temp": 25})`.
   - **SIN PONER PAUSAS**, ejecuta el sensor y mira cómo el Hub lo patea y el programa se rompe con un error rojo.
4. **La solución:** Modifica tu bucle `while True:` en el sensor agregando un `time.sleep(1)` al final. 
5. Ejecuta nuevamente el sensor y observa cómo ahora convive pacíficamente con las estrictas reglas de la red.

## Reglas Estrictas

- **Permitido:** `while True`, `.broadcast()`, `time.sleep()`, configuración por `nerve.config`.
- **Prohibido:** Tratar de enviar mensajes múltiples seguidos sin pausas para "engañar" al sistema.

## El Escenario de Prueba

Cuando no tienes `time.sleep()`, tu terminal arrojará algo como:
`ConnectionAbortedError: [WinError 10053] Se ha anulado una conexión...` (o `BrokenPipeError` en Mac/Linux).

Cuando arregles tu código, la terminal será un río de paz:

```text
[NERVE] Connected to hub as 'sensor_temp'.
Enviando temperatura...
Enviando temperatura...
Enviando temperatura...
```
¡Felicidades! Acabas de entender cómo se escalan y protegen las redes profesionales.
