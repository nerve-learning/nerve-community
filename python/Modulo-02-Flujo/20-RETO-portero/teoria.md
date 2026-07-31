# Teoría: Tu Cinturón de Herramientas (Repaso del Módulo 02)

Antes de enfrentar al Jefe Final, repasemos las armas que has conseguido. Cada una tiene un propósito específico. ¡Úsalas sabiamente!

### 1. Comparadores (`>`, `<`, `==`, `!=`)
Sirven para hacer preguntas matemáticas o de identidad.
*¿Es mayor? ¿Son exactamente iguales?*

### 2. Operadores Lógicos (`and`, `or`, `not`)
Sirven para combinar preguntas.
* `and`: El exigente. TODO tiene que ser cierto.
* `or`: El relajado. Con UNA sola cosa cierta, es suficiente.
* `not`: El rebelde. Voltea la verdad al revés.

### 3. La trinidad del Flujo (`if`, `elif`, `else`)
* `if`: "Si pasa esto..." (Siempre empieza la evaluación).
* `elif`: "Si no pasó lo de arriba, pero pasa esto..." (Puedes usar todos los que quieras).
* `else`: "Si nada de lo anterior pasó, haz esto por defecto" (La red de seguridad).

### 4. Lógica Anidada (El Inception)
Poner un `if` dentro de otro `if`. Útil cuando la primera pregunta "abre la puerta" para hacer más preguntas (Ej. Si tienes boleto -> ¿Es boleto VIP o Regular?).

### 5. `match-case` (El Cartero)
La mejor herramienta cuando vas a evaluar el **valor exacto** de una sola variable contra muchas opciones, como un menú o los días de la semana.

### 6. Truthy / Falsy
Recordar que las variables numéricas valen Falso si son `0`, y los textos valen Falso si están vacíos `""`.

### 7. Optimización y Depuración
Recuerda usar `print()` para espiar tus variables si el código hace cosas raras, y evita preguntar `if condicion == True:` (solo escribe `if condicion:`).
