# Teoría: El Buzón Mágico y el Recepcionista

Imagina que estás en tu oficina y has instalado el tubo neumático de Nerve. Para poder recibir paquetes, no puedes estar mirando el tubo las 24 horas del día sin hacer nada más. 

Lo que haces es **contratar a un recepcionista**. Le dices: *"Oye, voy a seguir trabajando en mis cosas. Si llega un paquete por el tubo, ábrelo, lee lo que dice y avísame"*. 

En programación, a este "recepcionista" se le llama **Callback** (función de devolución de llamada).

## Anatomía de la Escucha

Para que nuestro nodo pueda escuchar, necesitamos dos cosas: la receta (el recepcionista) y el contrato (decirle a Nerve que lo use).

```python
def mi_recepcionista(paquete):
    print("¡Llegó algo nuevo!")
    print(paquete)
```
* **Qué hace:** (Módulo 05) Creamos una función simple. Nota que DEBE recibir un parámetro (`paquete`). Nerve inyectará automáticamente los datos que lleguen dentro de esa variable.

```python
cliente.listen(mi_recepcionista)
```
* **Qué hace:** Le entregamos la receta a Nerve. **¡OJO!** Nota que pasamos `mi_recepcionista` SIN paréntesis `()`. Si pones paréntesis, estarías ejecutando la función en ese mismo instante. Al no ponerlos, le estás dando el manual de instrucciones a Nerve para que él lo ejecute *en el futuro* cuando llegue un mensaje.

```python
input("Presiona ENTER para apagar el nodo...\n")
```
* **Qué hace:** Nerve escucha en segundo plano (como un trabajador invisible). Si nuestro programa principal llega a la última línea de código, Python dice "terminé mi trabajo" y cierra todo, apagando también al recepcionista. Para evitarlo, usamos un `input()` (o un bucle infinito) que pausa el programa para siempre, manteniéndolo vivo y con las orejas abiertas.

---

## ¿Qué pasa si me equivoco?

El error más común es escribir:
`cliente.listen(mi_recepcionista())`  <-- ¡ERROR DE PARÉNTESIS!

**¿Qué pasa si lo haces?**
Python intentará ejecutar tu función inmediatamente antes de que llegue ningún mensaje. Como la función necesita un `paquete` (que aún no existe), el programa explotará diciendo:
`TypeError: mi_recepcionista() missing 1 required positional argument: 'paquete'`

**La Regla de Oro:**
Al asignar un recepcionista, dale la *tarjeta con su nombre*, no le des una orden inmediata. **Sin paréntesis**.
