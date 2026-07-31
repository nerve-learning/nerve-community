# Teoría: Únicos y Desordenados

Para crear un Set (Conjunto), usamos **las llaves `{` y `}`**, ¡igual que los diccionarios! 
¿Cómo sabe Python cuál es cuál? Fácil: los diccionarios tienen el símbolo de dos puntos `:` (clave: valor), mientras que los Sets solo tienen elementos sueltos separados por comas, como una lista, pero con llaves.

## Anatomía

```python
invitados = {"Ana", "Beto", "Carlos"}
```

Desmontemos la sintaxis:
- `invitados`: El nombre de la variable.
- `=`: Símbolo de asignación.
- `{`: Abre el club exclusivo (el Set).
- `"Ana", "Beto", "Carlos"`: Los elementos separados por comas. **NO** hay dos puntos `:`.
- `}`: Cierra el club.

## Las Dos Reglas de Oro de los Sets

1. **Anti-Clones (Valores Únicos):** Si intentas meter dos cosas iguales, el Set destruirá el clon en silencio.
   ```python
   numeros = {1, 1, 1, 2, 3}
   # La computadora solo guarda: {1, 2, 3}
   ```
2. **Sin Asientos Fijos (Desordenados):** Los Sets no tienen posiciones. **NO** puedes hacer `invitados[0]`. Si lo intentas, habrá un error. Cuando los imprimes en la terminal, los elementos pueden salir en un orden distinto al que los escribiste.

## ¿Qué pasa si me equivoco?

**El error más común:** Intentar buscar por posición (`[0]`).
Si escribes:
```python
mi_set = {"Rojo", "Azul"}
print(mi_set[0])
```
La terminal mostrará: `TypeError: 'set' object is not subscriptable`.
Significa: "Los Sets no tienen orden, así que no existe 'el primer elemento'. ¡No puedes usar corchetes aquí!".

**Otro error común:** Usar el comando equivocado para agregar cosas.
Acuérdate que para las Listas usábamos `.append()`. Para los Sets, ese botón no existe. Si quieres agregar algo a un Set, debes usar el botón **`.add()`** (que significa "añadir").
```python
mi_set.add("Verde")
```
