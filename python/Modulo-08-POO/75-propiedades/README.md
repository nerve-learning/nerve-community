# Nivel 75: Propiedades y el Decorador `@` 🎩

En el nivel anterior aprendimos a usar el Encapsulamiento. Escondimos nuestras variables detrás del doble guion bajo (`__`) y creamos funciones (como `leer_secreto()` o `depositar_dinero()`) para interactuar con ellas.

Esto es muy seguro, pero hace que escribir código sea un poco tedioso y repetitivo. A los programadores de Python les gusta que el código se lea de forma natural y limpia. ¿No sería genial si pudieras escribir `mi_cuenta.saldo = 100` (como si fuera una variable pública) pero que en el fondo de forma invisible Python revisara si ese número es válido antes de guardarlo?

¡Para eso existen las **Propiedades**! Nos permiten tener la belleza y simplicidad de las variables públicas, combinada con la seguridad nivel búnker de las variables privadas.

## Ruta de aprendizaje
1. **Teoría (`teoria.md`)**: Conoceremos a los "cadeneros" del club nocturno (los decoradores `@`) y cómo interceptan los datos.
2. **Ejemplo (`ejemplo.py`)**: Programaremos un Termostato inteligente que evita que quememos la casa.
3. **Reto (`reto.md`)**: Programarás la seguridad de la puerta de un Cine. ¡A programar!
