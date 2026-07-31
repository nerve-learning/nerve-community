# Teoría: Dividir y Conquistar (Microservicios)

En los niveles anteriores aprendimos a enviar mensajes a *todos* los nodos usando `.broadcast()`. Eso está bien cuando todos los nodos hacen lo mismo (como un chat). Pero en un sistema de microservicios, cada nodo tiene un nombre, un trabajo específico, y no queremos molestar a todos con información que no necesitan.

## Instalando el sistema nervioso (Nerve)

Nerve es la librería que hace la magia de conectar nuestros programas. Si aún no la tienes, para instalarla debes abrir tu terminal y escribir:

```bash
pip install alenia-nerve
```

Una vez instalada, Nerve necesita un "cerebro central" o "Hub" que dirija el tráfico de mensajes. Piensa en el Hub como el router de tu casa: sin él, tus dispositivos no pueden hablar entre sí.

Para encender este cerebro, puedes abrir una terminal nueva y simplemente dejar corriendo un script cortito que tenga esto:

```python
from nerve import NexusHub
hub = NexusHub()
hub.start()
```
¡O usar directamente la herramienta de terminal si Nerve te lo permite! Mientras el Hub esté encendido, todos tus nodos (microservicios) podrán conectarse a él.

## El método `.send()` (Mensaje Privado)

Si el nodo "mesero" quiere pedirle comida al nodo "chef", no usa `.broadcast()`. Usa `.send()`, que envía un mensaje directo y privado.

### Anatomía del .send()

```python
cliente.send("chef", {"accion": "preparar", "plato": "Pizza"})
```

- **`cliente.send`**: El método para enviar un mensaje directo.
- **`"chef"`**: El nombre exacto del nodo al que le queremos hablar (tiene que estar conectado).
- **`{...}`**: Nuestro Payload (carga útil), el diccionario con las instrucciones.

## ¿Qué pasa si me equivoco?

El error más común es escribir mal el nombre del nodo destino.
`cliente.send("cheff", {...})` (con doble 'f').

**¿Cómo se lee en la terminal?**
Probablemente no veas un error rojo explotando en tu cara, simplemente *el mensaje nunca llegará* porque Nerve buscará a alguien llamado "cheff" y como no existe, descartará el mensaje. Siempre verifica que el nombre en `.connect("nombre")` sea exactamente el mismo que usas en `.send("nombre", ...)`.
