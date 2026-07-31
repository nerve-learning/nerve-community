# Glosario: Redes y Sockets

Conceptos de redes y comunicación que usa Nerve para conectar scripts entre sí. Se explican desde cero.

---

## Conceptos Fundamentales de Redes

| Término | Qué es | Para qué sirve | Ejemplo |
| :--- | :--- | :--- | :--- |
| **Red (Network)** | Sistema de conexión entre computadoras | Permite que diferentes programas o máquinas se comuniquen e intercambien datos. Internet es una red de redes. | Tu WiFi conecta tu celular con el router |
| **Protocolo** | Reglas de comunicación acordadas | Un idioma en común que dos partes usan para entenderse. Como las reglas del correo postal. | TCP, UDP, HTTP, WebSocket |
| **Puerto (Port)** | Número que identifica un servicio en una máquina | Un número (0–65535) que identifica un servicio específico dentro de una computadora. Como el número de apartamento dentro de un edificio. | Puerto 80 → HTTP, Puerto 443 → HTTPS |
| **IP (Dirección IP)** | Identificador de una computadora en la red | Un número único que identifica cada dispositivo en una red. Como la dirección de un edificio. | `127.0.0.1` = tu propia computadora |
| **localhost / 127.0.0.1** | Tu propia máquina | Cuando un programa se conecta a "localhost", se conecta a sí mismo. Usado para probar servidores sin internet. | `http://localhost:8080` |
| **TCP** | Protocolo de comunicación confiable | Garantiza que los datos lleguen completos y en orden. Si se pierde algo, lo reenvía. Nerve lo usa en Windows. | Transferencias de archivos, navegación web |
| **UDP** | Protocolo rápido sin garantías | Envía datos sin verificar que lleguen. Más rápido que TCP pero puede perder paquetes. | Streaming de video, juegos online |

---

## Sockets e IPC (Lo que hace Nerve)

| Término | Qué es | Para qué sirve | Ejemplo |
| :--- | :--- | :--- | :--- |
| **Socket** | Punto de conexión entre procesos | Como un "enchufe" que dos programas usan para mandarse mensajes. Tiene dos lados: quien envía y quien recibe. | `import socket` en Python |
| **IPC (Inter-Process Communication)** | Comunicación entre procesos | Forma en que dos programas corriendo simultáneamente se mandan mensajes. Es el concepto central de Nerve. | Un script Python le habla a un script Go a través de Nerve |
| **Unix Socket** | Socket de archivo en Linux/macOS | Usa un archivo del sistema (en vez de TCP) para comunicación local. Más rápido que TCP en Linux/macOS. Nerve los usa en Linux/macOS. | `/tmp/nerve.sock` |
| **Socket TCP** | Socket de red usando TCP | Usa el protocolo TCP con IP + puerto para comunicarse. Funciona entre máquinas distintas. Nerve lo usa en Windows. | `socket.connect(("127.0.0.1", 7878))` |
| **Servidor (Server)** | El que escucha y responde | Está siempre corriendo y espera que los clientes se conecten. | El proceso de Nerve que escucha conexiones |
| **Cliente (Client)** | El que inicia la conexión | Se conecta al servidor para enviarle datos o pedirle algo. | Tu script Python que se conecta a Nerve |
| **bind()** | Asignar dirección al socket del servidor | El servidor ata su socket a una dirección y puerto para que los clientes sepan dónde conectarse. | `server.bind(("127.0.0.1", 7878))` |
| **listen()** | Poner el socket a escuchar | El servidor entra en modo de espera, listo para aceptar conexiones entrantes. | `server.listen(5)` |
| **accept()** | Aceptar una conexión entrante | El servidor acepta la conexión de un cliente. Devuelve un nuevo socket para hablar con ese cliente. | `conn, addr = server.accept()` |
| **connect()** | Conectarse al servidor desde el cliente | El cliente llama a la puerta del servidor. | `client.connect(("127.0.0.1", 7878))` |
| **send() / recv()** | Enviar y recibir datos | Las funciones básicas para mandarse bytes a través del socket. | `socket.send(b"Hola!")` / `data = socket.recv(1024)` |

---

## Conceptos de HTTP y APIs

| Término | Qué es | Para qué sirve | Ejemplo |
| :--- | :--- | :--- | :--- |
| **HTTP** | Protocolo de la Web | El protocolo que usan los navegadores para pedir páginas web. | `http://` al inicio de una URL |
| **HTTPS** | HTTP con cifrado | Versión cifrada de HTTP. Tus datos viajan encriptados. | `https://github.com` |
| **API** | Interfaz para comunicar programas | Un conjunto de reglas para que dos programas se hablen. Una API web te permite pedir datos sin interfaz visual. | API de OpenWeatherMap para obtener el clima |
| **REST API** | Tipo de API que usa HTTP | El estilo más común de APIs web. Usa URLs y métodos HTTP (GET, POST, etc.) para hacer operaciones. | `requests.get("https://api.ejemplo.com/datos")` |
| **GET** | Solicitar datos sin modificar nada | El método HTTP para pedir información a un servidor. | `requests.get("https://api.clima.com/ciudad/monterrey")` |
| **POST** | Enviar datos al servidor | El método HTTP para enviar datos nuevos (crear algo). | `requests.post(url, json={"nombre": "Ana"})` |
| **WebSocket** | Conexión bidireccional persistente | Mantiene la conexión abierta para que ambos lados puedan hablar cuando quieran. A diferencia de HTTP, no es pregunta-respuesta. | Chat en tiempo real |
| **Endpoint** | Dirección de un recurso en una API | La URL específica de un recurso. Cada endpoint sirve para una operación distinta. | `GET /api/clima` o `POST /api/usuarios` |
| **timeout** | Límite de tiempo de espera | El tiempo máximo que tu programa esperará una respuesta antes de rendirse y reportar error. | `requests.get(url, timeout=5)` |

---

## Conceptos de Concurrencia

| Término | Qué es | Para qué sirve | Ejemplo |
| :--- | :--- | :--- | :--- |
| **Proceso** | Programa en ejecución | Una instancia de tu programa corriendo. Tiene su propia memoria independiente. | Tu script de Python = un proceso |
| **Hilo (Thread)** | Unidad de ejecución dentro de un proceso | Un proceso puede tener varios hilos corriendo. Comparten memoria. | `import threading` en Python |
| **Concurrencia** | Manejar varias tareas a la vez | La capacidad de avanzar en varias tareas al mismo tiempo, aunque no sea literalmente simultáneo. | El servidor Nerve atendiendo a 10 clientes a la vez |
| **Carga (Load)** | Nivel de trabajo de un servidor | Cuántas peticiones está manejando un servidor en un momento dado. | 1000 peticiones por segundo = alta carga |

---

> Nerve abstrae toda esta complejidad. No necesitas saber de sockets para usar Nerve, pero entender cómo funcionan te ayuda a comprender por qué Nerve existe y qué problema resuelve. Los módulos avanzados sí requieren estos conceptos.

---

← [Volver al Índice del Glosario](README.md)
