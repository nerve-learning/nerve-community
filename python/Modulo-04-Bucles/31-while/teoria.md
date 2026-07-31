# Teoría: La Máquina de Repetición

Hasta ahora, nuestro código se ejecutaba de arriba hacia abajo, una sola vez. Con `if`, podíamos elegir si ejecutar un bloque de código o no. Pero, ¿qué pasa si queremos ejecutar ese bloque **muchas veces**?

Aquí entra `while`. La palabra `while` en inglés significa "mientras". 
Funciona como un guardia de seguridad muy estricto que hace una pregunta antes de dejarte pasar. Si la respuesta es sí (Verdadero), pasas y haces la acción. Cuando terminas, el guardia te vuelve a hacer la misma pregunta. Solo te dejará salir del ciclo cuando la respuesta sea no (Falso).

## Anatomía de un `while`

```python
galletas = 3

while galletas > 0:
    print("¡Me como una galleta!")
    galletas = galletas - 1
```

Desmontemos cada símbolo nuevo y palabra:

- `while` : Es la orden mágica. Le dice a la computadora: "Prepárate para repetir algo".
- `galletas > 0` : Es la **condición**. La computadora evalúa esto igual que en un `if`. ¿Es verdadero o falso?
- `:` : Los dos puntos. Significa "entonces haz lo siguiente". Obliga a que la siguiente línea tenga un espacio en blanco al inicio (indentación).
- La indentación (espacios al inicio de la línea) : Todo el código que esté empujado hacia la derecha es lo que se va a repetir. 
- `galletas = galletas - 1` : ¡Esto es vital! Estamos actualizando la variable. Si no restamos las galletas, el número siempre será 3. La condición `3 > 0` siempre será verdadera y el bucle nunca terminará.

## ¿Qué pasa si me equivoco?

El error más común de todo aprendiz (¡y de muchos profesionales!) es crear un **bucle infinito**. 

**¿Cómo se ve el error?**
Tu terminal empezará a imprimir el mismo mensaje a una velocidad increíble y nunca se detendrá. Tu computadora podría empezar a sonar como un avión despegando porque está trabajando sin descanso.

**¿Por qué pasa?**
Porque olvidaste cambiar el valor de la variable dentro de la indentación. Si la condición siempre es verdadera, el `while` nunca se detiene.

**¿Cómo lo soluciono?**
Si te quedas atrapado en un bucle infinito en tu terminal, no entres en pánico. Presiona las teclas `Ctrl` y la letra `C` al mismo tiempo (`Ctrl + C`). Esto fuerza a la computadora a detener el programa de inmediato. Luego, revisa tu código y asegúrate de estar alterando la variable para que, en algún momento, la condición sea falsa.
