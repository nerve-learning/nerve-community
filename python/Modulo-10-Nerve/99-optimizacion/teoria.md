# Teoría: Límites de Velocidad (Rate Limiting)

En Nerve, el Hub tiene defensas automáticas que podemos activar usando nuestro viejo amigo, el archivo `nerve.config` (o pasándolo directamente al instanciar `NexusHub()`).

Hay dos configuraciones principales para proteger nuestra red:

### 1. Límite de mensajes por segundo (`rate_limit_messages_per_sec`)
Esto define cuántos mensajes puede enviar un solo nodo en el transcurso de un segundo. Si un nodo envía más rápido que este límite, el Hub lo considera "Spam" y **lo desconecta inmediatamente** sin previo aviso. ¡Expulsado de la fiesta!

### 2. Máximo de conexiones (`max_connections`)
Esto define cuántos nodos pueden estar conectados al Hub al mismo tiempo. Si el límite es 5 y llega un sexto nodo, la puerta estará cerrada y la conexión fallará.

## Anatomía en el archivo `nerve.config`

Para activar estas protecciones, simplemente las agregas a tu archivo de configuración:

```text
# Solo permitimos 10 nodos en total
max_connections=10

# Ningún nodo puede enviar más de 5 mensajes por segundo
rate_limit_messages_per_sec=5
```

## ¿Qué pasa si me equivoco?

El error más común es olvidar poner una pausa (`time.sleep()`) dentro de un bucle `while True:` infinito.

Si haces esto:
```python
while True:
    cliente.broadcast({"accion": "hola"})
    # ¡Olvidamos el time.sleep!
```

Tu computadora enviará miles de mensajes en una fracción de segundo. 
**¿Cómo se lee en la terminal?**
El programa cliente lanzará un error de conexión rota (`ConnectionAbortedError` o similar) porque el Hub literalmente le cerró la puerta en la cara (Drop connection) por pasarse del límite de velocidad.
