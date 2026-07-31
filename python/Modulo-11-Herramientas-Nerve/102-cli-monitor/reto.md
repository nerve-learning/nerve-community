# Reto 102: El Maestro de Orquesta 🎼

Es el momento de poner todo a trabajar en conjunto. Tu misión será convertirte en un administrador de red ejecutando la Trinidad de Nerve: El Hub, El Monitor y Tu Programa.

## Instrucciones

1. **Terminal 1**: Activa tu entorno virtual y arranca la red con `nerve start` (esta vez no necesitas `--verbose`).
2. **Terminal 2**: Activa tu entorno virtual y ejecuta la herramienta de observación con `nerve monitor`. Verás una interfaz azul oscura.
3. **Terminal 3**: Crea tu propio archivo llamado `mi_trafico.py`.
   - Dentro, conéctate a Nerve bajo el nombre `"robot_mascota"`.
   - Haz un bucle `for` que envíe 10,000 mensajes sin parar al destino `"caja_de_arena"`.
   - Usa un paquete simple como `{"ping": 1}`.
   - Una vez termine el bucle de 10,000, haz que tu programa duerma (`time.sleep(15)`) para que tengas tiempo de mirar la Terminal 2.
4. Ejecuta `mi_trafico.py` en la Terminal 3 y **observa inmediatamente la Terminal 2**.

### Conceptos Permitidos
- Importar `NexusClient` y `time`.
- Bucles `for` con la función `range()`.
- Diccionarios `{}`.
- Comandos CLI: `nerve start` y `nerve monitor`.

### Conceptos Prohibidos
- Usar clases.
- Ejecutar `nerve monitor` sin que el Hub esté funcionando.

### Resultado Esperado

En la **Terminal 3** no verás casi nada, solo lo que decidas imprimir.

Pero en la **Terminal 2 (nerve monitor)**, verás en vivo cómo aparece `"robot_mascota"`, la barra de mensajes sube a 10,000 instantáneamente, y el contador de Tráfico muestra un pico de datos. A los 15 segundos, cuando el programa Python termine, `"robot_mascota"` desaparecerá de las pantallas de seguridad. ¡Has dominado el panel de control!
