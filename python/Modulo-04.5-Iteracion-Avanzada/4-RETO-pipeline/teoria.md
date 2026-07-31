# Teoría: La Línea de Ensamble 🏭

Hasta ahora, has construido chefs individuales y grifos independientes. Pero el verdadero poder de los generadores se desata cuando los conectas entre sí, formando lo que en programación se llama un **Pipeline** (tubería o línea de ensamble).

Imagina una fábrica de juguetes:
1.  **Máquina 1:** Toma plástico crudo y moldea la forma (Generador 1).
2.  **Máquina 2:** Pinta el juguete moldeado (Generador 2).
3.  **Máquina 3:** Empaca el juguete pintado (Generador 3).

Si estas máquinas usaran **listas** (cubos), la Máquina 1 tendría que moldear 10,000 juguetes y guardarlos en una bodega gigante antes de que la Máquina 2 pudiera empezar a pintar.

Como usan **generadores** (grifos), la Máquina 1 moldea *un* juguete y se lo pasa a la Máquina 2, que lo pinta y se lo pasa a la Máquina 3. No hay bodegas. El juguete fluye sin interrupciones.

---

## Anatomía de un Pipeline

Un pipeline se forma simplemente pasando un generador como entrada a otro generador.

```python
# 1. Los datos crudos
datos = [1, 2, 3, 4, 5]

# 2. Las "máquinas" (funciones generadoras)
def duplicar(numeros):
    for n in numeros:
        yield n * 2

def restar_uno(numeros):
    for n in numeros:
        yield n - 1

# 3. La conexión del pipeline (de adentro hacia afuera)
# restar_uno toma como entrada lo que escupe duplicar
pipeline = restar_uno(duplicar(datos))

# 4. El encendido
for resultado in pipeline:
    print(resultado)
```

Desmontando la conexión: `restar_uno(duplicar(datos))`
- Primero, `duplicar(datos)` crea un generador, pero no procesa nada todavía.
- Segundo, `restar_uno(...)` recibe ese generador y crea otro generador encima.
- Cuando el `for` pide el primer valor, `restar_uno` le pide un valor a `duplicar`, `duplicar` saca el `1` de la lista, lo duplica a `2`, y se lo pasa a `restar_uno`, que le resta uno y entrega el `1` final.

---

## ¿Qué pasa si me equivoco?

**El error más común: Meter listas donde van generadores**

A veces, por costumbre, los programadores construyen el pipeline mal, rompiendo la cadena de eficiencia:

```python
def duplicar_mal(numeros):
    lista = []
    for n in numeros:
        lista.append(n * 2)
    return lista  # ¡ROTO! Esto es un cubo, no un grifo.

pipeline_roto = restar_uno(duplicar_mal(datos))
```

**¿Por qué pasa?**
Si alguna etapa intermedia usa `return` con una lista completa, o usa una List Comprehension `[...]`, rompes el pipeline. Ese paso obligará a cargar todo en memoria antes de pasarlo al siguiente.

**¿Cómo lo soluciono?**
Asegúrate de que **cada etapa** del proceso use `yield` o una expresión generadora `(...)`. El único lugar donde se permite una lista es en los datos crudos iniciales, o si al final del pipeline decides guardar el resultado final en una lista con `list(pipeline)`.
