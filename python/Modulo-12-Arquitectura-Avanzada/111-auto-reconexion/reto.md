# Reto 111: El Soldado que Nunca se Rinde 🪖

¡Tu misión es programar un cliente de Nerve que sea imposible de silenciar por una desconexión!

Has sido asignado para monitorear las comunicaciones del Escuadrón Alpha. Tu programa recibirá los mensajes normales del escuadrón, pero la red en el campo de batalla es pésima. Cuando el Hub de comunicaciones se caiga y se vuelva a conectar, tu programa DEBE detectar el momento exacto en que la red regresó y enviar una alerta de "Red Restablecida" a la terminal.

### 📝 Instrucciones:

1. Escribe un archivo Python desde cero.
2. Crea una función llamada `leer_transmision` que reciba el `payload` y lo imprima con el texto: `[COMUNICADO]: <aqui_el_payload>`.
3. Crea una función llamada `alerta_red_restablecida` que imprima EXACTAMENTE: `⚠️ ENLACE DE COMUNICACIONES RESTABLECIDO ⚠️`.
4. Crea un cliente `NexusClient`, conéctalo con el nombre `"monitor_alpha"`.
5. Ponlo a escuchar (`listen`), conectando tus dos funciones correctamente.

### ⛔ Reglas Estrictas:
* **Permitido**: Crear funciones `def`, usar `print()`, importar y usar `NexusClient`, y usar los parámetros `on_payload` y `on_reconnect` en `listen()`.
* **Prohibido**: Ejecutar las funciones con `()` dentro de los parámetros de `listen`. ¡Entrégalas como herramientas!
* **Prohibido**: Escribir bucles infinitos `while True` para reconectar manualmente. (¡Nerve ya lo hace por ti!).

### 🎯 Resultado Esperado en la Terminal:
Si inicias tu cliente, apagas el Hub y lo vuelves a encender un segundo después (o simplemente confías en la magia si logramos simular el corte de energía), la terminal mostrará exactamente esto:

```text
[COMUNICADO]: Avanzando a la zona de extraccion
⚠️ ENLACE DE COMUNICACIONES RESTABLECIDO ⚠️
[COMUNICADO]: Mision cumplida, regresando a la base
```
