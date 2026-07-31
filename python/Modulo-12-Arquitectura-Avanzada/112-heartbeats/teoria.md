# El Salvavidas y el Pulso de la Red

Imagina a un salvavidas en una piscina llena de niños. El salvavidas no se queda mirando en silencio. Cada 5 minutos grita: *"¿Están todos bien?"*. Los niños responden: *"¡Sí!"*. 
Si un niño no responde a ese llamado, el salvavidas sabe inmediatamente que algo anda mal y lo saca de su lista de "nadadores activos".

En la arquitectura de Nerve, el **Hub** es el salvavidas y los **Clientes** son los nadadores.
Por defecto, el Hub de Nerve emite un grito (un latido o *ping*) cada **5 segundos** de manera completamente invisible. Si un cliente no responde a ese latido, el Hub dice: *"Este nodo murió repentinamente, lo voy a purgar de mi memoria"*.

Esto mantiene a tu servidor (el Hub) ligero, rápido y libre de "zombies" que consumen memoria RAM.

---

### Anatomía de `heartbeat_interval`

Cuando creas un Hub, puedes decirle cada cuántos segundos quieres que grite *"¿Están todos bien?"*.

```python
hub = NexusHub(heartbeat_interval=3.0)
```

Desarmemos los símbolos:
- `NexusHub`: La clase que crea el servidor central (ya la conoces).
- `()`: Los paréntesis sirven para "construir" el objeto y pasarle configuraciones iniciales.
- `heartbeat_interval=`: Es la etiqueta de configuración. "Heartbeat" significa "latido del corazón" e "interval" significa "intervalo".
- `3.0`: Es un número decimal (float) que representa **segundos**. Le decimos: "haz el chequeo cada 3 segundos exactos".

---

### ¿Qué pasa si me equivoco?

**Error Clásico #1: Ansiedad extrema (Número muy pequeño)**

Si escribes `heartbeat_interval=0.01`, le estás diciendo al Hub que pregunte *"¿Estás bien?"* cien veces por segundo. 
**Consecuencia:** Vas a saturar la red. Los clientes estarán tan ocupados respondiendo "¡Sí!" que no tendrán tiempo para enviar los mensajes reales de tu programa. El internet se pondrá lento.
**Solución:** Usa números sensatos. 5.0 (el defecto), 2.0 o 10.0 suelen ser ideales dependiendo de qué tan rápido necesites detectar una caída.

**Error Clásico #2: Apagar el monitor cardíaco (El número cero)**

Si escribes `heartbeat_interval=0`, le estás diciendo a Nerve: *"No revises el pulso, confío ciegamente"*.
**Consecuencia:** Esto desactiva los latidos por completo. Se usa mucho cuando los programadores están haciendo "tests" (pruebas de código automáticas), pero si lo usas en un programa real, tu Hub se llenará de zombies si se va la luz en las casas de tus clientes.

**Error Clásico #3: Textos en lugar de números**

Si escribes `heartbeat_interval="5"`. ¡Pum! Error en la terminal. El Hub necesita un número (para contar el tiempo), no una palabra o texto rodeado por comillas (`""`). Python no puede usar un cronómetro con palabras.
