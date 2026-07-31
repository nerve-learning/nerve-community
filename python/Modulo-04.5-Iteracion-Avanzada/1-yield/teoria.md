# Teoría: La Pausa Mágica ⏸️

Recuerda el dispensador de pañuelos del módulo de iteradores. Cuando jalabas `next()`, la máquina te daba el siguiente elemento y **recordaba** dónde se había quedado.

Hasta ahora, esa máquina la creabas con `iter()` sobre una lista que ya existía. Pero, ¿y si quisieras **tú mismo** ser el que decide cuándo viene cada valor y qué valor dar?

Imagina que eres chef en un restaurante. Hay dos formas de servir el menú:

- **Forma A (el `return` normal):** Te encierras en la cocina, cocinas los 500 platos de golpe, los apilas en una torre gigante y solo entonces sales. Nadie come hasta que terminas todo.
- **Forma B (el `yield`):** Cocinas **un plato**, lo llevas a la mesa, la función se **pausa**, y cuando el comensal pide el siguiente, vuelves a la cocina exactamente donde lo dejaste y preparas el siguiente.

`yield` es el chef que cocina bajo demanda.

---

## Anatomía del `yield`

```python
def semaforo():
    yield "🔴 Rojo"      # Pausa 1: entrega "🔴 Rojo" y se congela
    yield "🟡 Amarillo"  # Pausa 2: cuando la reanuden, entrega esto
    yield "🟢 Verde"     # Pausa 3: y finalmente esto

mi_semaforo = semaforo()      # NO ejecuta nada todavía. Solo crea el "chef"
print(next(mi_semaforo))      # Reactiva la función → llega a yield → devuelve "🔴 Rojo" → se pausa
print(next(mi_semaforo))      # Reactiva de nuevo → llega al siguiente yield → "🟡 Amarillo"
print(next(mi_semaforo))      # Reactiva de nuevo → "🟢 Verde"
```

**Desmontando cada símbolo nuevo:**

- `yield "🔴 Rojo"` — La palabra `yield` hace **dos cosas al mismo tiempo**: entrega el valor que está a su derecha (como un `return`), y congela la función en esa línea exacta.
- `semaforo()` — Llamar a la función **no la ejecuta**. Devuelve un objeto especial llamado **generador**. Es como contratar al chef, no como pedirle que cocine.
- `next(mi_semaforo)` — Ya conoces `next()` de los iteradores. Aquí hace lo mismo: "chef, cocina el siguiente". Reactiva la función hasta el próximo `yield`.

---

## ¿Qué pasa si me equivoco?

**El error más común: llamar `next()` una vez de más**

Si tu función tiene 3 `yield` y llamas `next()` cuatro veces, la terminal te gritará:

```
StopIteration
```

Ya lo conoces del módulo de iteradores. Significa que el dispensador está vacío: jalaste la palanca y no quedaban pañuelos. La función llegó al final sin encontrar más `yield`.

**¿Cómo lo evito?**
Usa un bucle `for` en vez de `next()` manual. El `for` detecta automáticamente cuándo se acabaron los valores y para solo:

```python
for estado in semaforo():   # El for se encarga de llamar next() por ti
    print(estado)           # Y para solo cuando ya no hay más yield
```
