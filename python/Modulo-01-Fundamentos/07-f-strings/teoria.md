# Teoría: El Texto con Huecos

Imagina un formulario de "rellene los espacios en blanco" como:
`Mi nombre es _______ y tengo _______ años.`
Los F-Strings hacen exactamente esto.

### Anatomía de la instrucción

Vamos a desmontar esta línea: `print(f"Hola, mi nombre es {piloto}")`

*   `f`: (Justo antes de abrir la comilla). Significa "Formato". Es el botón de encendido mágico. Le avisa a la computadora: *"¡Ojo! Este texto tiene agujeros adentro, prepárate para rellenarlos"*.
*   `" "`: Las comillas de siempre para indicar que es un texto.
*   `{ }`: Son las llaves (los "huecos"). Todo lo que metas aquí adentro, la computadora lo buscará en sus cajas (variables) y pegará su contenido justo en ese lugar del texto.
*   `piloto`: El nombre de la caja que queremos usar para rellenar ese hueco.

### ¿Qué pasa si me equivoco?

1. **Olvidar la letra `f`**:
   Si escribes `print("Hola {piloto}")` (sin la 'f' al principio), la magia no se activa. La computadora tomará las llaves literalmente y en pantalla verás exactamente:
   `Hola {piloto}` (en lugar de "Hola Alex").

2. **Olvidar las llaves `{}`**:
   Si pones la `f` pero te olvidas de las llaves: `print(f"Hola piloto")`, imprimirá "Hola piloto" porque no le dijiste qué palabra era un hueco a rellenar con una variable.

3. **Escribir mal el nombre de la variable dentro de las llaves**:
   Si tu variable se llama `piloto` y pones `{pilotoo}`, el programa estallará con el clásico `NameError: name 'pilotoo' is not defined`.
