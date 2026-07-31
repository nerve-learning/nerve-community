# Teoría: Cajas y Etiquetas

Crear una variable es literalmente tomar una caja vacía, pegarle una etiqueta con un nombre, y meterle algo adentro. 

### Anatomía de la instrucción

Vamos a desmontar esta línea: `mensaje = "Hola"`

*   `mensaje`: Es la **etiqueta** de la caja (el nombre de la variable). La computadora ahora sabe que existe una caja llamada "mensaje".
*   `=`: El **signo de asignación**. ¡OJO AQUÍ! En matemáticas, el `=` significa "estas dos cosas valen lo mismo". En programación, el `=` es una acción: significa *"toma lo que está a la derecha y guárdalo dentro de la caja de la izquierda"*. Piensa que es una flecha apuntando a la izquierda: `mensaje <--- "Hola"`.
*   `"Hola"`: Es el **contenido** (texto) que estamos metiendo dentro de la caja.

Una vez que guardaste algo en la caja `mensaje`, puedes usar `print(mensaje)` para ver qué tiene adentro. Fíjate que al usar la caja en el `print`, **NO** le ponemos comillas, porque no queremos imprimir la palabra literal "mensaje", queremos abrir la caja y ver qué hay dentro.

### Reglas para los nombres (etiquetas)
La computadora es quisquillosa con cómo llamas a tus cajas:
1. No pueden tener espacios (`mi nombre` está mal).
2. Para separar palabras usamos un guion bajo: `mi_nombre`.
3. No pueden empezar con números (`1nombre` está mal).

### ¿Qué pasa si me equivoco?

El error más doloroso al principio es pedirle a la computadora una caja que no has creado, o equivocarte al escribir el nombre.

Si guardas `saludo = "Hola"` y luego escribes `print(saludoo)`, la terminal gritará en rojo:
`NameError: name 'saludoo' is not defined`

**Traducción humana:** "Error de nombre: Me estás pidiendo que busque la caja 'saludoo', pero no tengo ni idea de qué es eso. ¡Nunca fabricaste esa caja!"
