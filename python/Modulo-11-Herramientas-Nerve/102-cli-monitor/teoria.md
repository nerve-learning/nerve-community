# Teoría: El Panel de Control 🎛️

En el nivel anterior usamos `--verbose` para ver cada mensaje que pasaba por el Hub. Eso es útil cuando estás construyendo y debuggeando un solo programa, pero en sistemas en producción (en la vida real), la información fluye tan rápido que un humano no puede leerla línea por línea.

Para resolver esto, Nerve trae un sub-comando especial llamado `monitor`.

## Anatomía de `nerve monitor`

El comando se escribe así en tu terminal:

```bash
nerve monitor
```

- `nerve`: Llama a nuestra herramienta de red.
- `monitor`: Es el sub-comando que le dice a Nerve: *"No inicies un Hub, simplemente conéctate al Hub que ya existe y muéstrame las estadísticas de forma interactiva"*.

Al presionar Enter, tu terminal se transformará. Ya no será una simple consola de texto que se desplaza hacia abajo. Se convertirá en un **TUI** (Text User Interface o Interfaz de Usuario de Texto). Verás tablas, barras y números que se actualizan mágicamente en el mismo lugar de la pantalla.

El monitor te mostrará:
1. **Nodos conectados**: El nombre de cada programa conectado.
2. **Tiempo de actividad (Uptime)**: Cuánto tiempo lleva vivo cada programa.
3. **Métricas de tráfico**: Cuántos mensajes se están enviando y recibiendo.

## ¿Por qué necesitamos otra terminal?

Un detalle fundamental: `nerve monitor` **NO** es el Hub. El monitor es simplemente otro programa (cliente) que se conecta al Hub para preguntarle cómo van las cosas.

Por lo tanto, la Oficina de Correos (`nerve start`) debe estar trabajando de forma independiente. El monitor es solo el guardia de seguridad mirando las cámaras en otra habitación.

## ¿Qué pasa si me equivoco?

**El error más común:** Ejecutar `nerve monitor` sin haber ejecutado `nerve start` en otra terminal.
**¿Qué verás?** El monitor te arrojará un error de conexión, diciendo algo como que no puede acceder a `/tmp/nerve.sock` (en Linux/Mac) o `127.0.0.1:50505` (en Windows). No puedes monitorear una red que está apagada.

Recuerda el orden de la vida:
1. Nace la red (`nerve start`).
2. Nacen los observadores (`nerve monitor`).
3. Nacen los trabajadores (tu código en Python).
