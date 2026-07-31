# Teoría: La Topología Estrella y el Hub Central 🌟

## ¿Qué es una Topología de Red?

La palabra **Topología** (del griego *topos*, que significa "lugar") se refiere a la forma en que los diferentes nodos (computadoras o programas) están conectados entre sí. 

Imagina que tienes a 5 amigos en una habitación (nodos). Hay varias formas en las que pueden comunicarse:
1. **Topología de Anillo**: Cada uno solo le puede hablar al que tiene a su derecha.
2. **Topología de Malla**: Todos pueden hablar directamente con todos (esto requiere muchas "líneas" de conexión).
3. **Topología Estrella**: Todos le hablan a una persona en el centro (un moderador), y esta persona se encarga de entregar los mensajes al destinatario correcto.

## La Arquitectura de Nerve: Hub y Clientes

**Nerve** utiliza estrictamente una **Topología Estrella**. 

1. **NexusHub (El Centro)**: Cuando ejecutas el comando `nerve start` en tu terminal, estás creando el nodo central de la estrella. Este es el enrutador. No hace nada de trabajo pesado por sí solo, solo recibe y envía mensajes usando los delimitadores `\n` (salto de línea).
2. **NexusClient (Las Puntas)**: Son tus programas en Python (o Rust, Go, JavaScript) que se conectan al Hub. Cada uno se identifica con un nombre único (ej. `mi_herramienta_python`).

### ¿Por qué una estrella?

Si tuviéramos 100 microservicios y usáramos una malla, cada microservicio tendría que conectarse a los otros 99. Serían miles de conexiones cruzadas (caos total). Al usar el `NexusHub`, cada microservicio solo hace **UNA** conexión (hacia el Hub), y el Hub se encarga de retransmitir los mensajes a la velocidad de la luz.

## Visualizando la Estrella: `nerve dashboard`

Como todos los datos pasan por el Hub, ¡el Hub sabe exactamente quién está conectado! Nerve incluye un comando llamado `nerve dashboard`. 

Al ejecutarlo en una nueva terminal, levanta una interfaz web (normalmente en `http://localhost:8080`) donde dibuja en tiempo real el mapa exacto de tu topología. Puedes ver todos los nodos conectados como bolitas alrededor del Hub, sus tiempos de actividad y cuántos mensajes han enviado.

### Símbolo a entender
- `nerve dashboard`: Es un comando que invocas en la terminal de tu sistema operativo (como hiciste con `pip install` o `python`). No se escribe dentro del código de Python. Levanta un servidor web interno para que veas la red en tu navegador.

¡Vayamos al ejemplo para poblar nuestra estrella!
