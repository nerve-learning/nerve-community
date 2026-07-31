# Teoría: El Bucle Comprimido

La comprensión de listas asusta a muchos principiantes porque parece que alguien aplastó el código. Pero si lo lees de izquierda a derecha, tiene todo el sentido del mundo. 

Se divide en dos partes: **La Acción** (lo que le vas a hacer al objeto) y **El Motor** (el bucle que saca el objeto). Y todo esto debe vivir dentro de una caja de lista nueva: los corchetes `[]`.

## Anatomía de una Comprensión de Lista

```python
numeros = [1, 2, 3]

# ¡Magia en una línea!
dobles = [numero * 2 for numero in numeros]
```

Desmontemos este hechizo:

- `[` y `]` : Los corchetes exteriores son vitales. Le dicen a la computadora: "Todo lo que pase aquí adentro es para construir una lista completamente nueva".
- `numero * 2` : Esta es **La Acción**. Le estamos diciendo a la computadora qué queremos guardar en la lista nueva. En este caso, el número multiplicado por dos.
- `for numero in numeros` : Este es **El Motor**. Es exactamente el mismo bucle `for` que ya conoces. Se encarga de ir a la lista vieja (`numeros`), sacar un elemento y guardarlo en la variable temporal (`numero`).

**Cómo lo lee un humano:**
"Quiero guardar el `numero * 2` por cada `numero` que haya en la lista `numeros`".

## ¿Qué pasa si me equivoco?

El error más común es escribirlo al revés o olvidar los corchetes.

**¿Cómo se ve el error?**
`SyntaxError: invalid syntax`

**¿Por qué pasa?**
Si escribes `[for numero in numeros numero * 2]`, la computadora colapsa. Espera que le digas primero QUÉ quieres guardar (La Acción), y luego CÓMO lo vas a conseguir (El Motor).

**¿Cómo lo soluciono?**
Recuerda la fórmula: `[` + `ACCIÓN` + `MOTOR` + `]`. Siempre debes empezar escribiendo la variable temporal sola o modificada, y después la palabra `for`. Y nunca olvides envolver todo el hechizo en los corchetes `[]` para que sepa que es una lista.
