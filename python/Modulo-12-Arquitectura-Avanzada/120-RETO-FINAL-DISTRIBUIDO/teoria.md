# Teoría: La Sinfonía de los Microservicios 🎻

Imagina un restaurante. No hay una sola persona que reciba a los clientes, tome la orden, cocine, lave los platos y cobre. Si esa persona se tropieza, el restaurante quiebra ese día. 
En su lugar, tienes **roles separados**:
- El **Mesero** (toma la orden y la grita).
- El **Chef** (escucha la orden, la procesa y grita "¡Listo!").
- El **Repartidor** (escucha "¡Listo!" y lo lleva a la mesa).
- Y el **Tablero de Comandas** (El lugar donde todos ponen y leen los mensajes).

### Instalando nuestro Tablero de Comandas (Nerve)

Para construir sistemas de este calibre en tu propia computadora, necesitas las herramientas correctas instaladas en tu sistema operativo, no solo en tu script de Python. 

**Paso 1: Instalar Alenia Nerve**
Abre la terminal (tu línea de comandos, fuera de Python) y escribe:
`pip install alenia-nerve`

*(Nota de pedagogo: `pip` es el "instalador de paquetes de Python", le dice a internet "tráeme esta herramienta a mi compu").*

**Paso 2: Encender el Cerebro Central (Hub)**
Abre una terminal nueva y ejecuta:
`nerve start`

Verás que el Hub cobra vida. Este es tu "Tablero de Comandas". A partir de este momento, **no cierres esta terminal**. Déjala corriendo de fondo.

**Paso 3: Levantar tus Mini-Programas**
Ahora puedes crear 2, 3 o 10 scripts de Python distintos. Cada uno tendrá un `NexusClient()`.
Al correrlos (ej. `python mesero.py`, luego `python chef.py` en terminales separadas), todos se conectarán mágicamente al Hub que dejaste encendido en el Paso 2.

---

### Anatomía de la Arquitectura Distribuida

1. **Terminal 1 (`nerve start`)**: Orquesta todo. Conoce quién está conectado pero no hace el trabajo duro.
2. **Terminal 2 (`sensor.py`)**: Script dedicado *únicamente* a enviar datos (`cliente.send(...)`). No sabe quién los recibe.
3. **Terminal 3 (`pantalla.py`)**: Script dedicado *únicamente* a escuchar (`cliente.listen(...)`). No sabe de dónde vienen.

### ¿Qué pasa si me equivoco?

**El Error:** Cierras la terminal de `nerve start` por accidente, o se te olvida correrlo antes que tus scripts.
**La Terminal dice:** `ConnectionRefusedError: [Errno 111] Connection refused`
**El Significado Humano:** Tu `NexusClient` intentó entrar al restaurante, pero encontró la puerta con candado. El Tablero de Comandas (el Hub) no está encendido. ¡Enciéndelo primero!

**El Error:** Al correr `nerve start`, la terminal dice `OSError: [Errno 98] Address already in use`.
**El Significado Humano:** ¡Ya tienes un Hub corriendo escondido en otra ventana! Solo puede haber un cerebro principal escuchando en ese "puerto". Encuentra la terminal que lo está usando y ciérrala, o usa la ventana que ya está abierta.
