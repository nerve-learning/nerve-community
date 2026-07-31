# Nivel 96: Sincronización de Estado (El Handshake)

¡Bienvenido al nivel 96!

Hasta ahora, nuestros nodos pueden hablar entre sí y actualizar una variable global. Pero hay un problema grave: **¿Qué pasa si un nodo llega tarde a la fiesta?**

Imagina que el Nodo A está corriendo y cambia el estado a "Modo Oscuro". Cinco minutos después, el Nodo B se conecta. Como el mensaje de cambio ya pasó, el Nodo B empezará con su estado por defecto ("Modo Claro"). Los dos nodos ahora están **desincronizados**.

En el mundo de los sistemas distribuidos, esto se resuelve con algo llamado **Sincronización Inicial** o **Handshake** (Apretón de manos).

En este nivel aprenderás a:
1. Diseñar un sistema de "petición y respuesta" (Request/Response) sin usar servidores.
2. Hacer que un nodo recién conectado pregunte a la red: "¿Cuál es el estado actual?".
3. Hacer que los nodos veteranos respondan con la información.

## Archivos del Nivel

- `teoria.md`: Entenderemos cómo estructurar nuestros mensajes para diferenciar una "orden" de una "pregunta".
- `ejemplo.py`: Construiremos un sistema de chat o estado donde los nuevos nodos obtienen el historial inmediatamente.
- `reto.md`: Tu misión: Crear una lista de tareas (To-Do List) distribuida que nunca pierda la memoria cuando se suma un nuevo miembro.

¡Prepárate para darle memoria a tu red P2P!
