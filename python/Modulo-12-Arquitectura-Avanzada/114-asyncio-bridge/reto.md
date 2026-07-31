# Reto 114: El Portal Interdimensional 🌀

Tu equipo está desarrollando un videojuego web (HTML5) que necesita enviar comandos a un robot real programado en Python con Nerve. 

Los programadores web te han pedido que abras un puente, pero te exigen que uses el puerto "clásico" de desarrollo web (`8080`) en lugar del puerto por defecto de Nerve (`50506`), para que sus páginas web se puedan conectar fácilmente.

### 📝 Instrucciones:

1. Crea un archivo Python desde cero.
2. Asegúrate (en tu terminal) de tener instalados `alenia-nerve` y `websockets`.
3. Importa `NexusHub` y `NerveBridge`.
4. Crea y enciende un `NexusHub` normal.
5. Imprime el mensaje: `🌀 Abriendo portal interdimensional...`
6. Crea un `NerveBridge`. La IP (`host`) debe ser la misma `"127.0.0.1"`, pero el puerto (`port`) DEBE ser el `8080`.
7. Enciende el puente usando `.start()`.

### ⛔ Reglas Estrictas:
* **Permitido**: Importar e instanciar `NexusHub` y `NerveBridge`, usar `.start()`, imprimir texto.
* **Prohibido**: Poner el puerto entre comillas (debe ser un número `8080`, no un texto `"8080"`).
* **Prohibido**: Olvidar encender el Hub principal antes de encender el puente. (El puente necesita tierra firme de ambos lados).

### 🎯 Resultado Esperado en la Terminal:
Deberías ver tus impresiones y luego los mensajes oficiales de la librería indicando que el WebSocket Server está listo en el puerto 8080. Tu terminal se quedará "congelada" esperando conexiones, lo cual significa que has triunfado.

```text
🌀 Abriendo portal interdimensional...
INFO:nerve.bridge:Starting Nerve Bridge WebSocket server on ws://127.0.0.1:8080
```
*(Puedes salir presionando Ctrl+C en tu terminal)*
