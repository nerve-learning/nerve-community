# Teoría: La Etiqueta Oculta de los Datos

Cada vez que guardas algo en una variable, la computadora le pone una etiqueta invisible secreta que dice **qué tipo de cosa es**. Hoy conoceremos a los dos reyes de los datos: Los Textos y Los Enteros.

### 1. El Texto (String)
En programación, a los textos los llamamos **Strings** (cadenas, porque son una cadena de letras).
*   **¿Cómo se escriben?** Siempre van rodeados de comillas `""`.
*   **Analogía:** Piensa en un String como una pintura de un número. Si escribes `"5"`, no tienes 5 manzanas reales, tienes un cuadro pintado con el número 5. Si tratas de comerte el cuadro, te vas a romper los dientes. No puedes hacer matemáticas reales con Strings.

### 2. El Entero (Integer)
A los números sin decimales los llamamos **Integers** (enteros).
*   **¿Cómo se escriben?** Se escriben "desnudos", sin absolutamente NADA alrededor. 
*   **Analogía:** Un Integer es una cantidad real. Si escribes `5`, tienes 5 manzanas de verdad en tus manos.

### Resumen Visual

`edad = 25` <-- Integer (¡Bien! 25 manzanas reales)
`edad = "25"` <-- String (¡Cuidado! Es solo una foto del número 25)

### ¿Qué pasa si me equivoco?

El error más común es mezclar peras con manzanas. Aunque aún no haremos sumas complejas, si más adelante intentas sumar el número real `2` con el texto `"2"`, la computadora sufrirá un colapso y mostrará un error como este:
`TypeError: unsupported operand type(s) for +: 'int' and 'str'`

**Traducción humana:** "Error de Tipo: ¡Me estás pidiendo que mezcle un Integer (int) con un String (str)! No puedo sumar manzanas reales con fotos de manzanas."
