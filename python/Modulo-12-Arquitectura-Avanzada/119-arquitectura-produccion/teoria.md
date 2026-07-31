# El Cerebro Independiente

La librería que instalas con `pip install alenia-nerve` no solo contiene herramientas para tus archivos de código `.py`. También instala un **programa de terminal** que puedes invocar desde cualquier lado.

### 1. El Comando de Arranque (CLI)

En lugar de escribir `hub = NexusHub()` y `hub.start()` en tu código, la forma madura de hacerlo es abrir una terminal (consola) y escribir:

`nerve start`

Esto levantará el Servidor Central directamente en tu computadora. Tu terminal se quedará "bloqueada" mostrando una pantalla de inicio y mensajes de red. Ese es ahora el corazón de tu sistema. ¡Déjalo latiendo ahí y abre una nueva terminal para correr tus bots!

### 2. El Archivo de Configuración (`nerve.config`)

Si no inicias el Hub en Python, ¿cómo le dices en qué puerto (puerta lógica de red) quieres que se abra? 
Para eso usamos los archivos de configuración. Son simples archivos de texto donde escribes variables que Nerve lee automáticamente por arte de magia.

Simplemente creas un archivo de texto llamado `nerve.config` en tu carpeta y escribes:
`port=9000`

Tanto cuando corras `nerve start` en la terminal, como cuando corras un `NexusClient()` en tu código, ambos buscarán silenciosamente ese archivo en la carpeta. Si lo encuentran, el Hub se abrirá en el puerto 9000, y el cliente sabrá que debe conectarse a ese mismo puerto sin que tengas que programarlo a mano.

### ¿Qué pasa si me equivoco?

**El Error del Puerto Ocupado (Address already in use):**
Este error en rojo ocurre si intentas correr `nerve start` dos veces, o si tienes un `NexusHub()` encendido dentro de tu código de Python Y ADEMÁS intentas correr `nerve start` en la terminal. Solo puede haber un jefe ocupando la puerta al mismo tiempo. Cierra una de las terminales.

**El Error de la Conexión Rechazada (Connection Refused):**
Ocurre si ejecutas tu archivo de bots `ejemplo.py` (que intenta conectarse con el Hub) ANTES de correr `nerve start`. ¡Los clientes intentarán tocar la puerta del Hub a toda velocidad, pero nadie les abrirá y el programa fallará! Siempre arranca tu Hub externo primero.
