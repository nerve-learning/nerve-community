# Reto 104: El Recepcionista en Acción 🤖

Ya sabemos que `nerve bridge` funciona como un puente que conecta el mundo exterior (como una página web vía WebSockets en el puerto `50506`) con el mundo interno de Nerve (el Hub local en `50505`).

Tu misión en este nivel es crear el script trabajador que recibirá esos mensajes traducidos y procesará la información.

## 📝 Instrucciones

Crea un archivo llamado `reto.py` en esta misma carpeta y escribe código que haga lo siguiente:

1. Importa las herramientas necesarias de `nerve` (`NexusClient`) y `time`.
2. Crea una instancia de `NexusClient` llamada `trabajador`.
3. Conecta al trabajador a la red de Nerve bajo el nombre `"procesador_web"`.
4. Define una función callback llamada `procesar_datos` que acepte un parámetro (los datos del mensaje). Dentro de la función:
   - Imprime el mensaje: `"¡Mensaje recibido del puente web!"`.
   - Imprime el contenido de los datos.
5. Registra el callback llamando a `.listen(procesar_datos)` en tu cliente `trabajador`.
6. Crea un bucle infinito que mantenga el script en ejecución para que el trabajador no se retire antes de recibir trabajo (utiliza `time.sleep(1)`).

## 🛑 Reglas Estrictas
- El archivo DEBE llamarse `reto.py`.
- Debes conectarte a la red bajo el nombre `"procesador_web"`.
- Debes usar la función `.listen(procesar_datos)`.

## 🎯 Resultado Esperado en Terminal
Al arrancar el Hub (`nerve start`), el puente (`nerve bridge`) y ejecutar tu `reto.py`, cuando un cliente web envíe un mensaje a la red, tu terminal del reto debería imprimir:
```text
¡Mensaje recibido del puente web!
Contenido: ...
```
