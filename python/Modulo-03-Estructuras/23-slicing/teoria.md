# Teoría: Las Computadoras Cuentan desde Cero

Para pedirle a una lista un elemento específico, usamos de nuevo los **corchetes `[]`**, pero esta vez los pegamos al nombre de la lista, y adentro ponemos un número (la posición).

**LA REGLA DE ORO:** ¡Las computadoras empiezan a contar desde el `0`, no desde el `1`!
- El 1er elemento es el `0`.
- El 2do elemento es el `1`.
- El 3er elemento es el `2`.

## 1. Acceso por Índice (Posición)
```python
amigos = ["Ana", "Beto", "Carlos"]
primer_amigo = amigos[0]
```
- `amigos`: La lista.
- `[0]`: Significa "dame el elemento en la posición 0" (el primero, que es "Ana").

## 2. Rebanado (Slicing) con `:`
Si queremos más de un elemento, usamos el símbolo de **dos puntos `:`** dentro de los corchetes. Significa "desde aquí HASTA aquí".

```python
grupo = amigos[0:2]
```
- `[0:2]`: Significa "córtame la lista empezando en la posición `0` y detente ANTES de llegar a la posición `2`".
- Por lo tanto, nos dará el `0` ("Ana") y el `1` ("Beto"), pero NO el `2`. Es como decir "hasta la puerta del 2, pero sin entrar".

## ¿Qué pasa si me equivoco?

**El error más común:** Pedir una posición que no existe.
Si tu lista tiene 3 cosas, las posiciones son `0`, `1` y `2`. Si pides la posición `3`:
```python
amigos = ["Ana", "Beto", "Carlos"]
print(amigos[3])
```
La terminal explotará con un error: `IndexError: list index out of range` (Índice de lista fuera de rango). Significa: "¡Tu caja no tiene un compartimento número 3!".
