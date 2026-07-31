# Teoría: Hablando con la máquina

Imagina que la computadora es un asistente muy trabajador pero que no tiene sentido común. Si le dices "di hola", podría buscar un archivo llamado "hola" o entrar en pánico. Tienes que ser extremadamente específico.

Para hacer que la computadora muestre un texto en la pantalla, usamos nuestra primera herramienta: `print()`.

### Anatomía de la instrucción

Vamos a desmontar esta línea: `print("Hola")`

*   `print`: Es la **orden** (o función). En inglés significa "imprimir". Le dice a la computadora: *"Prepárate para mostrar algo en la pantalla"*.
*   `()`: Los **paréntesis** son como los brazos de la orden. Todo lo que pongas dentro de estos brazos es lo que la orden va a abrazar y procesar. Si `print` es la acción de "entregar una caja", los paréntesis son la caja misma.
*   `""`: Las **comillas** (dobles o simples) son cruciales. Le dicen a la computadora: *"Lo que está aquí adentro es texto para humanos. No intentes leerlo como si fuera una orden secreta, no intentes calcularlo, solo muéstralo tal cual"*. Sin comillas, la computadora intentará ejecutar la palabra "Hola" como si fuera otra orden y fallará.

### ¿Qué pasa si me equivoco?

El error más común de un estudiante que empieza es olvidar cerrar un paréntesis o una comilla. 

Si escribes `print("Hola)` (nota que falta la comilla final), la computadora se quedará esperando a que termines de escribir el texto para siempre. Al intentar correr el programa, la terminal te mostrará un error en rojo que dice algo como:
`SyntaxError: unterminated string literal`

**Traducción humana:** "Error de sintaxis: empezaste un texto con una comilla pero nunca lo terminaste. ¡Me quedé esperando el final!"
