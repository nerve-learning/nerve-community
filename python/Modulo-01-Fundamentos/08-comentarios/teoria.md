# Teoría: El Símbolo de Invisibilidad

Para escribir un comentario en Python, usamos el símbolo de numeral o "hashtag": `#`.

### Anatomía de la instrucción

Vamos a desmontar esta línea: `# Esto es un cálculo de impuestos`

*   `#`: Todo lo que se escriba a la derecha de este símbolo, en esa misma línea, se vuelve invisible para la computadora. Cuando el sistema lee tu código y encuentra un `#`, dice: *"Ah, esto es para humanos, salto a la siguiente línea"*.

Puedes usar comentarios de dos maneras principales:
1. **Línea completa:** Para explicar una sección entera de código.
2. **Al final de la línea:** Para explicar una variable específica justo al lado de ella. Ej: `oxigeno = 100  # Porcentaje restante`

También tienen un superpoder oculto: **Desactivar código**. Si escribes una orden como `print("Hola")` pero le pones un `#` al principio, la máquina lo ignorará. Los programadores hacen esto todo el tiempo para probar cosas sin borrar su código.

### ¿Qué pasa si me equivoco?

El error ocurre cuando olvidas poner el `#`. Si escribes texto humano normal en tu archivo:

`calculamos el total de la nave`
`total = 50 + 20`

La computadora intentará ejecutar la primera línea como si fueran órdenes oficiales, y al no entender qué significa la palabra "calculamos", explotará lanzando:
`SyntaxError: invalid syntax`

**Traducción humana:** "Error de sintaxis: No entiendo este lenguaje. Si querías dejarme una nota, ¡ponle un # primero!"
