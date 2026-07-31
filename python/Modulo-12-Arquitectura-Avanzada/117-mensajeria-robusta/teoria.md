# Acuses de Recibido (ACK) y Escudos de Errores

Para poder usar Nerve, recuerda siempre instalarlo en tu terminal con:
`pip install alenia-nerve`

En Nerve, cuando usas `cliente.send()`, la librería hace un gran trabajo asegurándose de que el mensaje llegue al Hub (incluso se reconecta si se cae el internet de tu lado). PERO, el Hub se lo entrega al otro bot y... ¿qué pasa si el otro bot estaba procesando otra cosa y falla? ¿O si no entendió tu mensaje?

### 1. El Concepto de ACK (Acknowledge)

La palabra "ACK" viene del inglés "Acknowledge" (Reconocer/Confirmar). Es el equivalente digital a decir "¡Recibido y entendido!".

Para implementarlo, necesitamos dos cosas:
1. **Un ID de mensaje:** Como un número de guía de paquetería. Así sabemos *qué* nos están confirmando.
2. **Una respuesta de vuelta:** El bot que recibe el mensaje debe enviar un mensaje de regreso diciendo "El mensaje con ID X fue procesado con éxito".

**Ejemplo mental:**
- Bot A dice: *Petición ID 1: Transfiere $50.*
- Bot B recibe, hace la transferencia y dice: *Bot A, completé la Petición ID 1.*

### 2. El Mensaje Envenenado (Poison Pill)

¿Qué pasa si el Bot A le envía un mensaje al Bot B, pero se equivoca y envía un texto en lugar de un número?
Si el Bot B intenta hacer una suma matemática con un texto, Python lanzará un error y **el Bot B morirá** (se cerrará el programa).

En un sistema distribuido, no puedes permitir que un error de un bot mate a otro bot. Para eso usamos nuestro viejo amigo: el bloque `try / except`.

### Anatomía de la Protección

```python
def escuchar_mensaje(payload):
    try:
        # Intentamos hacer algo peligroso
        dinero = payload["monto"]
        total = dinero + 100
        print(f"Total: {total}")
        
        # Si todo salió bien, enviamos el ACK
        cliente.send(to="bot_origen", payload={"id": payload["id"], "status": "OK"})
        
    except Exception as e:
        # Si algo falla (ej. no venía 'monto', o era un texto), el bot no muere.
        # Capturamos el error y avisamos de vuelta que algo salió mal.
        print(f"Error procesando mensaje: {e}")
        cliente.send(to="bot_origen", payload={"id": payload["id"], "status": "ERROR"})
```

### ¿Qué pasa si me equivoco?

**El Error de la Identidad Confundida:**
Si envías mensajes sin un ID (como `"id": 1`), cuando el otro bot te responda "OK", no sabrás a qué petición original se refiere. ¡Imagina pedir 3 pizzas y que la pizzería te diga "La orden está lista", pero no te dice CUÁL orden! Siempre ponle una "etiqueta" (ID) única a tus mensajes importantes.
