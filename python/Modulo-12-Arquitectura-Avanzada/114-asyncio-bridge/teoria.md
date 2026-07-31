# El Traductor de las Naciones Unidas

Piensa en Nerve como una reunión exclusiva donde todos hablan español (Python). De repente, llega una página web que solo habla inglés (WebSockets). Si intentan hablar directamente, nadie se entenderá.

El **Nerve Bridge** es como el traductor de las Naciones Unidas. Se sienta en el medio, escucha a la página web en inglés, lo traduce instantáneamente a español y se lo grita al Hub de Nerve. Cuando el Hub responde, el puente hace lo inverso.

### El Secreto del Malabarista (`asyncio`)
Si te preguntas por qué el tema se llama "asyncio-bridge", es porque por debajo, este puente usa una tecnología de Python llamada **Asyncio** (Asynchronous I/O). 

Imagina a un mesero normal: toma la orden de la mesa 1, va a la cocina, *se queda esperando de pie sin hacer nada hasta que la comida está lista*, la entrega, y recién ahí atiende a la mesa 2. Eso es lento.
Un mesero **Asyncio** es un malabarista: toma la orden de la mesa 1, la deja en la cocina, y *mientras se cocina*, corre a atender a las mesas 2, 3 y 4. 

Gracias a `asyncio`, tu puente puede manejar miles de páginas web conectadas al mismo tiempo sin quedarse congelado.

---

### Anatomía del Puente

Para usar el puente, usamos una herramienta especial de Nerve.

```python
from nerve.bridge import NerveBridge

puente = NerveBridge(host="127.0.0.1", port=50506)
puente.start()
```

Desarmemos los símbolos:
- `NerveBridge`: Es la clase traductora. Crea el puente.
- `host="127.0.0.1"`: Es la dirección "Local". Significa que el puente solo aceptará conexiones que vengan desde tu propia computadora (ideal para pruebas).
- `port=50506`: Es el número de la "puerta" de tu computadora por donde dejará entrar a las páginas web.
- `.start()`: Enciende el puente y lo deja funcionando de forma infinita (como un malabarista que no para).

---

### ¿Qué pasa si me equivoco?

**Error Clásico #1: Falta de Materiales (El error websockets)**

Si intentas ejecutar el puente y la terminal te grita un error que dice: *"The 'websockets' package is not installed"*.
**Consecuencia:** El puente se niega a iniciar. Nerve sabe hacer el puente, pero necesita piezas de construcción web que Python no trae por defecto.
**Solución:** Debes instalar la librería de construcción web abriendo tu terminal y escribiendo: `pip install websockets`. (Obviamente, asumiendo que ya tienes `alenia-nerve` instalado).

**Error Clásico #2: Puerta Bloqueada (Port in use)**

Si intentas correr tu puente dos veces al mismo tiempo, Python dirá "Address already in use". 
**Consecuencia:** Solo puedes tener a un portero vigilando la puerta `50506`. Si abres el programa dos veces, el segundo chocará con el primero.
**Solución:** Detén (cierra) la terminal anterior antes de volver a correr tu programa.
