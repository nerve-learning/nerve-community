# Teoría: La Boca y los Oídos

Si `print()` es la boca de la computadora (sirve para hablar hacia afuera), entonces `input()` son sus oídos (sirve para escuchar lo que viene de afuera).

### Anatomía de la instrucción

Vamos a desmontar esta línea: `nombre = input("¿Cómo te llamas? ")`

*   `input`: Es la orden de **escuchar**. Cuando la computadora lee esto, **congela el tiempo**. El programa se detiene completamente hasta que el humano escribe algo en el teclado y presiona la tecla `Enter`.
*   `("¿Cómo te llamas? ")`: Lo que pongas entre los paréntesis (siempre entre comillas) es la pista o pregunta que la computadora mostrará *antes* de quedarse esperando. Si lo dejas vacío `input()`, la computadora se quedará congelada en negro y el usuario no sabrá qué hacer.
*   `nombre =`: Recuerda el Nivel 02 (las variables). Si la computadora escucha algo pero no lo guarda en ningún lado, se le olvida al instante. Por eso usamos el `=` para atrapar la respuesta del humano y guardarla en la caja `nombre`.

### La Gran Trampa del Input

Hay una regla de oro que debes tatuarte: **TODO lo que entra por `input()` se convierte en Texto (String)**. 
*   Si el usuario escribe `Alex`, se guarda como `"Alex"`.
*   Si el usuario escribe `5`, se guarda como `"5"` (¡con comillas!). 

Si intentas sumar ese `"5"` con un `2` real, la computadora estallará con el error que vimos en el nivel anterior:
`TypeError: can only concatenate str (not "int") to str`

Más adelante aprenderemos cómo convertir esos textos en números reales, pero por ahora, limitémonos a pedir palabras.
