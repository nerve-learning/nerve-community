# Teoría: El Arte de Anidar

Cuando metemos una lista dentro de otra lista, o un diccionario dentro de una lista, la estructura crece "hacia adentro". Para acceder a los datos, tenemos que ir abriendo las cajas paso a paso, de afuera hacia adentro.

## 1. Listas dentro de Listas
Imagina un edificio: primero eliges el piso, y luego la habitación.

```python
edificio = [
    ["Ana", "Beto"],     # Piso 0 (Índice 0)
    ["Carlos", "Diana"]  # Piso 1 (Índice 1)
]
```
Si queremos llegar hasta "Diana":
1. Primero entramos al piso 1: `edificio[1]`. Eso nos da la lista `["Carlos", "Diana"]`.
2. Ahora, de esa nueva lista, queremos el elemento en la posición 1: `[1]`.
3. Juntamos todo: `edificio[1][1]`. 

¡Son dos corchetes pegados! El primero abre la caja grande, el segundo abre la caja pequeña.

## 2. Diccionarios dentro de Listas
Es el formato más usado en el mundo real. Imagina una lista de perfiles de usuarios.

```python
usuarios = [
    {"nombre": "Goku", "poder": 9000},
    {"nombre": "Vegeta", "poder": 8500}
]
```
Para ver el poder de Vegeta:
1. Buscamos a Vegeta en la lista (posición 1): `usuarios[1]`. Esto nos da el diccionario `{"nombre": "Vegeta", "poder": 8500}`.
2. Ahora, a ese diccionario le pedimos la clave `"poder"`: `["poder"]`.
3. Todo junto: `usuarios[1]["poder"]`.

## ¿Qué pasa si me equivoco?

**El error más común:** Perderse en el laberinto y usar el símbolo equivocado.
Si tienes una lista de diccionarios e intentas buscar por clave directamente en la lista:
```python
print(usuarios["nombre"])
```
¡Boom! `TypeError: list indices must be integers or slices, not str`. 
Traducción: "Oye, `usuarios` es una Lista. Las Listas solo entienden de números (0, 1, 2...), no entienden de etiquetas como 'nombre'. ¡Primero tienes que entrar a la posición numérica!".
