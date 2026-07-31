# Teoría: El Grifo vs El Cubo 🚿🪣

En el nivel anterior aprendiste que `yield` pausa una función y entrega un valor. Cuando llamas a esa función, obtienes algo especial. Vamos a entender exactamente qué es.

Imagina que necesitas agua en tu cocina. Tienes dos opciones:

- **El cubo 🪣:** Vas al jardín, llenas el cubo **completo** con toda el agua que podrías necesitar hoy, lo cargas pesado hasta la cocina, y lo pones en el piso. Ahora sí puedes usarla. El problema: si el cubo es enorme, tu brazo sufrió cargando todo ese peso aunque solo uses un vaso.
- **El grifo 🚿:** Abres la llave y el agua llega **exactamente cuando la necesitas**, en la cantidad exacta que necesitas. Sin cargar nada. El grifo no "guarda" el agua; la produce en el momento.

Las **listas** son cubos: guardan todos los elementos en memoria desde el primer momento.
Los **generadores** son grifos: producen los valores uno a uno, solo cuando los pides.

---

## ¿Qué es exactamente un generador?

Cuando llamas a una función que tiene `yield`, Python no la ejecuta. En cambio, te devuelve un **objeto generador**: un grifo listo para dar agua, pero que todavía no ha abierto la llave.

```python
def mi_grifo():
    yield "agua 1"
    yield "agua 2"
    yield "agua 3"

# Llamar a la función NO produce nada. Solo crea el grifo.
grifo = mi_grifo()

# El for abre la llave, saca un valor a la vez, y la cierra cuando se acaba
for agua in grifo:
    print(agua)
```

---

## Anatomía: La diferencia en la práctica

```python
# CUBO: crea toda la lista de golpe, ocupa espacio en memoria ahora mismo
cubo = ["turno-1", "turno-2", "turno-3", "turno-4", "turno-5"]

# GRIFO: solo sabe "cómo producir el siguiente cuando me lo pidan"
def grifo_turnos():
    numero = 1
    while numero <= 5:
        yield "turno-" + str(numero)  # str() convierte el número a texto
        numero = numero + 1

# Ambos se pueden recorrer con for, pero el grifo usa casi cero memoria
for t in cubo:
    print(t)

for t in grifo_turnos():
    print(t)
```

**La clave:** Los dos `for` producen exactamente la misma salida. La diferencia es invisible para el ojo, pero real para la computadora: el cubo cargó los 5 elementos desde el inicio; el grifo produjo uno, lo entregó, produjo otro, lo entregó...

---

## ¿Qué pasa si me equivoco?

**El error más común: intentar usar el generador dos veces**

```python
def grifo():
    yield 1
    yield 2

mi_grifo = grifo()

for n in mi_grifo:
    print(n)       # Imprime: 1, 2

for n in mi_grifo:
    print(n)       # No imprime NADA — el grifo ya se vació
```

**¿Por qué pasa?**
Un generador es como un rollo de papel de baño: una vez que jalaste todo el papel, el rollo queda vacío. No se recarga solo.

**¿Cómo lo soluciono?**
Si necesitas recorrer los valores varias veces, tienes dos opciones:
1. Crea el generador de nuevo: `mi_grifo = grifo()` antes de cada `for`.
2. Guarda los resultados en una lista la primera vez: `resultados = [n for n in grifo()]`.
