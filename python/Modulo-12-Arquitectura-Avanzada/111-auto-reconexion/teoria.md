# La Magia Oculta de Nerve: Resiliencia

Imagina que eres un piloto de avión y el Hub de Nerve es tu Torre de Control.
Estás volando, recibiendo y enviando mensajes. De repente, ¡pum!, la Torre de Control se queda sin energía y se apaga.
¿Qué haces? ¿Apagas los motores de tu avión y te dejas caer? ¡Por supuesto que no!

Sigues volando (tu programa sigue en ejecución), tomas tu radio, y empiezas a llamar: *"Torre, aquí vuelo 111, ¿me escuchan?"*. Lo repites cada par de segundos hasta que la Torre vuelve a encenderse y te responde.

Esa es exactamente la magia de la **Auto-Reconexión** en Nerve. El `NexusClient` tiene un escudo de protección. Si el Hub se cae, el cliente no lanza un error rojo fatal que cierra tu programa. En lugar de eso, entra en un "modo de supervivencia", intentando reconectarse periódicamente de manera invisible.

Pero, a veces, como programador, **necesitas saber exactamente en qué momento regresó la conexión**. Quizás durante el apagón te perdiste de algo importante, o necesitas avisar a los usuarios de tu programa que "¡Ya volvimos a estar en línea!".

Para eso, Nerve nos da un parámetro especial llamado `on_reconnect`.

---

### Anatomía de `on_reconnect`

En el módulo anterior aprendiste a "escuchar" usando `client.listen()`. Ahora le agregaremos un compañero.

```python
# Así lo hacíamos antes (solo nos importa cuando llega un mensaje)
client.listen(on_payload=mi_funcion_para_mensajes)

# Así lo hacemos ahora (queremos saber también cuándo revivió la conexión)
client.listen(on_payload=mi_funcion_para_mensajes, on_reconnect=mi_funcion_de_reconexion)
```

Desarmemos los símbolos:
- `on_payload=`: Es el "conector" que vincula la llegada de un mensaje con tu función. Ya lo conoces.
- `,`: La coma separa parámetros. Le dice a Python: "Espera, todavía quiero darle más instrucciones a esta función".
- `on_reconnect=`: Es el nuevo "conector". Le dice a Nerve: "Oye, si alguna vez te desconectas y logras volver a conectarte con éxito al Hub, quiero que dispares esta función que te estoy pasando".
- `mi_funcion_de_reconexion`: Es el nombre de la función tuya que se va a ejecutar (nota que va **sin** paréntesis `()`, porque no la estás ejecutando tú, se la estás entregando a Nerve para que él la ejecute en el futuro).

> **Nota:** La función que conectes a `on_reconnect` NO recibe ningún parámetro (como sí lo hace la de `on_payload` que recibe el mensaje). Debe ser una función que no pida nada, simplemente definida como `def funcion():`.

---

### ¿Qué pasa si me equivoco?

**Error Clásico #1: Ejecutar la función en lugar de entregarla.**

Si escribes esto:
`client.listen(..., on_reconnect=mi_funcion_de_reconexion())`
*(¡Con paréntesis al final!)*

**Lo que la computadora entiende:**
Python dirá: "Ah, el humano quiere que yo ejecute `mi_funcion_de_reconexion()` AHORA MISMO, y luego el resultado de esa función se lo paso a `on_reconnect`".
Esto provocará que tu función de reconexión se dispare al instante (incluso si no ha habido ninguna desconexión) y, lo que es peor, Nerve se enojará porque le diste el *resultado* de la función (generalmente `None`) en lugar de darle la *función en sí misma* para usarla como herramienta más tarde.

**La solución:** Siempre pasa el **nombre** de la función sin los paréntesis `()`. Piensa en los paréntesis como el botón de encendido de la licuadora. Tú quieres darle la licuadora a Nerve para que él la encienda cuando la necesite, no encenderla tú y darle el batido.
