# Teoría: El Dispensador de Turnos

Imagina el dispensador de boletos de una panadería. Llegas, jalas un papelito y te da el número 0. La siguiente persona jala otro y le da el 1. 

La herramienta `range` funciona exactamente así. En inglés, "range" significa "rango". Es una máquina que genera una secuencia de números por la cual podemos iterar (recorrer) usando nuestro viejo amigo, el bucle `for`.

## Anatomía de un `range`

```python
for turno in range(3):
    print("Número de turno:")
    print(turno)
```

Desmontemos lo nuevo:

- `range` : Es el nombre de la herramienta. Le dice a la computadora: "enciende la fábrica de números".
- `()` : Los paréntesis. Son como la ranura de una máquina expendedora. Todo lo que pongas adentro es la *instrucción* de cómo quieres que funcione la máquina.
- `3` : Es el número que metemos en la ranura. Le dice a la máquina: "Quiero exactamente 3 números".
- `turno` : Como vimos en el nivel anterior, es nuestra variable temporal. Guardará el número que la máquina nos vaya escupiendo uno a uno.

**¡El secreto de las computadoras!**
Si le pides a `range(3)` que te dé 3 números, tú como humano esperarías: `1, 2, 3`. 
¡Pero las computadoras siempre empiezan a contar desde el CERO! 
Por lo tanto, la máquina te entregará: `0, 1, 2`. 
Siguen siendo 3 números en total, solo que el conteo empieza en el 0.

## ¿Qué pasa si me equivoco?

El error más común es olvidar los paréntesis de `range` o qué significan los números que escupe.

**¿Qué pasa si espero que llegue al número 3?**
Si usas `range(3)`, el bucle se detendrá **antes** de llegar al 3. Solo imprimirá 0, 1 y 2. Si alguna vez necesitas que el número 3 aparezca en tu programa, tendrás que pedirle a la máquina `range(4)`. 

Recuerda esta regla de oro: `range(N)` genera números desde el `0` hasta un número antes de `N`.

**Error de sintaxis común:**
Escribir `for numero in range[3]:` usando corchetes en lugar de paréntesis. Recuerda: los corchetes `[]` son para **crear** listas manuales. Los paréntesis `()` son para **darle instrucciones** a una herramienta como `range`.
