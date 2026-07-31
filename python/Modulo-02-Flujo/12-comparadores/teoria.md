# Teoría: La balanza de Python

Imagina que tienes una balanza antigua de dos platos. Pones un dato en el plato izquierdo y otro en el derecho. Los **Operadores de Comparación** (o comparadores) son los símbolos que le dicen a Python cómo mirar esa balanza. 

La respuesta de Python al usar estos símbolos **siempre** será un valor Booleano: `True` (Verdad) si la comparación es correcta, o `False` (Mentira) si es incorrecta.

### El error más trágico del mundo: `=` vs `==`
Antes de ver la lista, debemos aclarar la confusión más grande de todo programador novato.
En matemáticas, usamos `=` para decir que dos cosas son iguales. **En Python NO es así.**

* **Un solo igual (`=`)**: Significa "GUARDAR". Toma lo de la derecha y mételo en la caja de la izquierda. 
  Ejemplo: `edad = 18` (Guarda el 18 en la caja edad).
* **Doble igual (`==`)**: Significa "COMPARAR". Le pregunta a Python: "¿Lo de la izquierda es exactamente igual a lo de la derecha?".
  Ejemplo: `edad == 18` (¿La caja edad tiene un 18 adentro? Responderá `True` o `False`).

### Los 6 Detectives (Símbolos de comparación)

1. **Igualdad (`==`)**: ¿Son idénticos? 
   `5 == 5` -> `True`
2. **Desigualdad (`!=`)**: ¿Son diferentes? (El signo de exclamación `!` significa "no").
   `"rojo" != "azul"` -> `True`
3. **Mayor que (`>`)**: ¿El de la izquierda es más grande?
   `10 > 5` -> `True`
4. **Menor que (`<`)**: ¿El de la izquierda es más pequeño?
   `2 < 1` -> `False`
5. **Mayor o igual (`>=`)**: ¿Es más grande o al menos es idéntico?
   `18 >= 18` -> `True`
6. **Menor o igual (`<=`)**: ¿Es más pequeño o al menos es idéntico?
   `10 <= 20` -> `True`

---

## Anatomía (Sintaxis)

```python
dato_izquierdo == dato_derecho
```
* `dato_izquierdo`: Puede ser una variable (ej. `precio`) o un valor directo (ej. `100`).
* `==`: El símbolo del detective. (Puede ser cualquiera de los 6: `>`, `<`, `>=`, `<=`, `!=`, `==`).
* `dato_derecho`: El otro valor con el que estamos comparando.

---

## ¿Qué pasa si me equivoco?

**El temido "SyntaxError" por usar `=` en lugar de `==`**
Si intentas comparar dos cosas así:
`mi_numero = 10 = 10` o a veces en condicionales futuros pones `if edad = 18:` 

Python te lanzará un error que dice `SyntaxError: invalid syntax` o `cannot assign to literal`. 
¿Por qué? Porque Python intentará agarrar el número de la derecha y guardarlo dentro del número de la izquierda. Como un número no es una caja (variable), la computadora se rinde y "explota". 
**Solución:** Recuerda que para comparar, los iguales siempre van en pareja: `==`.
