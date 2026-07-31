# Nivel 111: Auto-Reconexión Inquebrantable 🔌

En el mundo real, el WiFi parpadea, los cables se desconectan y los servidores (incluso nuestro Hub de Nerve) a veces necesitan reiniciarse. Si tu programa depende de una conexión perfecta que nunca falle, tu programa es de cristal y se romperá.

En este nivel aprenderás a escribir programas con "resiliencia". Veremos cómo Nerve detecta automáticamente si el servidor central desapareció y cómo se queda en un ciclo paciente intentando reconectarse hasta lograrlo, sin que tu programa "explote" (crash). Además, aprenderás a usar un "detector" para saber exactamente en qué momento la conexión volvió a la vida.

### Ruta de aprendizaje

1. **Teoría (`teoria.md`)**: Entenderemos cómo Nerve maneja las desconexiones usando la analogía de la "Radio del Avión" y aprenderemos el parámetro `on_reconnect`.
2. **Ejemplo (`ejemplo.py`)**: Veremos el código de un nodo de Nerve que es imposible de matar por caídas de red.
3. **Reto (`reto.md`)**: Escribirás tu propio nodo persistente capaz de detectar cuándo el servidor regresa.
