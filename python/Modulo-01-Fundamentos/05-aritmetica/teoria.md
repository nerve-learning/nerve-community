# Teoría: Los Símbolos Matemáticos

Para hacer cálculos en programación, no usamos la "x" para multiplicar ni los dos puntos para dividir. La computadora usa símbolos específicos del teclado.

### Los Operadores Básicos

1.  **Suma (`+`)**: Funciona igual que en la escuela.
2.  **Resta (`-`)**: También es idéntico a la escuela.
3.  **Multiplicación (`*`)**: ¡Ojo aquí! Usamos el asterisco. No uses la letra "x" ni "X", porque la computadora pensará que es una caja (variable) o un texto.
4.  **División (`/`)**: Usamos la barra oblicua. 

### ¿Cómo guardar un cálculo?

Recuerda que el símbolo `=` significa "toma lo de la derecha y guárdalo en la caja de la izquierda".
Si escribimos:
`total = 5 + 5`
La computadora primero resuelve la suma mentalmente (`10`) y luego guarda ese `10` dentro de la caja `total`.

También podemos sumar cajas directamente:
`manzanas = 3`
`peras = 2`
`frutas = manzanas + peras`

### ¿Qué pasa si me equivoco?

El error que rompe sistemas mundiales es intentar aplicar matemáticas a cosas que no son números.

Si tienes un texto (String) y un número (Integer/Float) e intentas sumarlos:
`resultado = "Hola" + 5`

La computadora te mostrará un error fulminante:
`TypeError: can only concatenate str (not "int") to str`

**Traducción humana:** "Error de Tipo: Solo puedo pegar un Texto con otro Texto, no puedo pegar un Texto con un Número Entero (int). ¿Cómo sumo la letra H con el número 5? ¡No tiene sentido!"
