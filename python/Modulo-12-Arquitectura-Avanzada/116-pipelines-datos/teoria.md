# Nodos Especializados y Cadenas de Montaje

Hasta ahora, tus bots de Nerve recibían un mensaje, hacían algo (como imprimir en pantalla) y terminaban. 
En un **Pipeline de Datos**, el bot hace su pequeño trabajo, pero su última acción NO es terminar, sino usar `client.send()` para pasarle el paquete modificado al siguiente bot.

Por ejemplo:
1. **El Extractor (Nodo A):** Lee un sensor de temperatura y envía `{"temp": 20}` al Nodo B.
2. **El Transformador (Nodo B):** Recibe el `20`, lo convierte a Fahrenheit `{"temp": 68}`, y se lo envía al Nodo C.
3. **El Cargador (Nodo C):** Recibe el `68` y lo guarda en la base de datos.

A esto se le conoce en la industria como arquitectura **ETL** (Extract, Transform, Load).

### Anatomía del Salto

En tu código, esto se ve simplemente como enviar un mensaje *dentro* de la función de escucha:

```python
def trabajo_del_nodo_b(payload):
    # 1. Hace su trabajo
    payload["temp"] = payload["temp"] * 2 
    
    # 2. Se lo pasa al siguiente en la cadena
    cliente_b.send(to="nodo_c", payload=payload)
```

---

### ¿Qué pasa si me equivoco?

**Error Clásico #1: El Bucle Infinito (Ping-Pong de la Muerte) 🏓**

Imagina que el `nodo_b` le envía el mensaje al `nodo_c`. Pero por un error de tipeo en el código del `nodo_c`, en lugar de enviarlo a un `nodo_d`, se lo devuelve al `nodo_b`.
**Consecuencia:** El `nodo_b` lo procesa y se lo lanza a `c`. `c` lo procesa y se lo lanza a `b`... A la velocidad de la luz. En cuestión de segundos, procesarán el mensaje millones de veces. Tu computadora empezará a sonar como una turbina de avión y el programa colapsará.
**Solución:** Siempre diseña tus pipelines en un pedazo de papel antes de programarlos. Las flechas solo deben ir hacia adelante. `A -> B -> C`. Nunca hacia atrás.

**Error Clásico #2: El Callejón sin Salida (Dead End)**

**Consecuencia:** El `nodo_b` hace un cálculo matemático increíble, pero al final de su función... te olvidas de escribir el `cliente.send()` hacia el `nodo_c`. El pipeline se corta a la mitad y los datos nunca llegan a su destino. El `nodo_c` se quedará esperando para siempre.
**Solución:** Revisa siempre que el último paso de tus nodos intermedios sea un envío al siguiente eslabón.
