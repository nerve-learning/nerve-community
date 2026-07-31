# Teoría: La Lista Ligera 🪶

Ya conoces las comprensiones de lista del Módulo 04:

```python
numeros = [1, 2, 3, 4, 5]
dobles = [n * 2 for n in numeros]   # Construye la lista [2, 4, 6, 8, 10] completa
```

Y ahora conoces los generadores: en vez de guardar todo, producen un valor a la vez.

¿Qué tal si pudiéramos combinar los dos? Escribir un generador en una sola línea, sin necesitar `def` ni `yield`. Ese es exactamente el poder de la **expresión generadora**.

---

## Anatomía: La única diferencia es `[]` vs `()`

```python
# LIST COMPREHENSION — usa corchetes [ ]
# Crea y guarda TODOS los valores en memoria ahora mismo
lista = [n * 2 for n in numeros]

# EXPRESIÓN GENERADORA — usa paréntesis ( )
# Solo guarda la "receta". Produce los valores uno a uno cuando se los pidas
generador = (n * 2 for n in numeros)
```

La estructura interna es idéntica: `valor_a_producir for variable in iterable`.
La única diferencia visual: los `[` `]` hacen una lista, los `(` `)` hacen un generador.

**Desmontando los símbolos:**
- `(` `)` — los paréntesis exteriores le dicen a Python: "esto no es una lista, es un generador en una línea"
- `n * 2` — esto es lo que se producirá (la acción, igual que en list comprehension)
- `for n in numeros` — el motor del bucle, exactamente igual que en list comprehension
- `if condicion` — opcional, para filtrar (exactamente igual que en list comprehension)

---

## Con filtro: el `if` al final

```python
edades = [15, 23, 17, 31, 14, 28, 19]

# Solo los adultos, sin crear lista
adultos = (edad for edad in edades if edad >= 18)

for a in adultos:
    print(a)   # 23, 31, 28, 19
```

---

## El uso más poderoso: directo dentro de `sum()`, `max()`, `min()`

`sum()`, `max()` y `min()` ya los conoces. Funcionan con cualquier colección de números. Y aceptan generadores directamente:

```python
precios = [120, 45, 890, 12, 340]

# Suma de todos los precios — sin crear lista intermedia
total = sum(precio for precio in precios)

# Precio máximo entre los que cuestan más de 100
maximo_caro = max(precio for precio in precios if precio > 100)
```

Cuando el generador va directamente **dentro** de `sum()` o `max()`, no necesitas el paréntesis extra: `sum(precio for precio in precios)` — los paréntesis de `sum()` cuentan.

---

## ¿Qué pasa si me equivoco?

**Error: intentar medir la longitud de un generador**

```python
gen = (n for n in [1, 2, 3])
print(len(gen))   # TypeError: object of type 'generator' has no len()
```

**¿Por qué pasa?**
El generador no sabe cuántos valores producirá hasta que los produzca todos (podría ser infinito). Es como preguntarle al grifo "¿cuánta agua tienes?" antes de abrir la llave: no lo sabe.

**¿Cómo lo soluciono?**
Si necesitas el tamaño, convierte a lista primero: `len(list(gen))`. Pero recuerda: esto consume el generador completo y guarda todo en memoria, así que pierdes la ventaja del grifo.
