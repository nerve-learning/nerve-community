# Nivel 112: El Pulso del Sistema (Heartbeats) 🫀

¿Alguna vez estabas en una llamada por internet, se cortó la luz en la casa de tu amigo, pero su foto siguió apareciendo en la pantalla por varios segundos como si aún estuviera ahí? 

Eso se conoce como una "conexión zombie". Cuando una computadora se apaga de golpe, no tiene tiempo de enviar un mensaje diciendo "¡Adiós, me desconecto!". El servidor central piensa que sigue ahí, ocupando memoria y recursos.

En sistemas distribuidos reales, si mil computadoras se apagan de golpe, el servidor colapsará intentando enviarles mensajes a "fantasmas". 

En este nivel aprenderás cómo **Nerve** soluciona esto usando "Latidos" (Heartbeats), una técnica que permite al Hub detectar quién está vivo y quién es un zombie, para limpiar la red automáticamente.

### Ruta de aprendizaje

1. **Teoría (`teoria.md`)**: Entenderemos la técnica del "salvavidas" y descubriremos el parámetro `heartbeat_interval`.
2. **Ejemplo (`ejemplo.py`)**: Configuraremos un Hub que revise el pulso de sus clientes de forma acelerada.
3. **Reto (`reto.md`)**: Construirás el "Hospital de Androides", un Hub estricto con sus revisiones.
