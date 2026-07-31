# Reto 46: La Calculadora Rápida ⚡

Te han asignado la tarea de hacer unas fórmulas matemáticas para el sistema de un dron topográfico. El problema es que la memoria del dron es diminuta, y tu jefe te ha prohibido usar la palabra `def`. ¡Quiere que todas las funciones ocupen una sola línea de código!

Tendrás que usar `lambda` para crear funciones "de bolsillo".

## 📝 Instrucciones

1. Crea un archivo llamado `reto.py`.
2. Crea una variable llamada `calcular_cuadrado` y asígnale una `lambda` que reciba 1 parámetro (un número) y devuelva ese número multiplicado por sí mismo.
3. Crea una variable llamada `calcular_area_triangulo` y asígnale una `lambda` que reciba 2 parámetros (base, altura). La lambda debe multiplicar la base por la altura, y dividir el resultado entre 2.
4. Fuera de las lambdas, llama a tu primera lambda pasándole el número `5`. Atrapa el resultado e imprímelo en pantalla con un mensaje descriptivo.
5. Llama a tu segunda lambda pasándole `10` de base y `4` de altura. Atrapa el resultado e imprímelo en pantalla con un mensaje descriptivo.

### 🚦 Reglas Estrictas
- **Conceptos permitidos:** `lambda`, variables, `print`, matemáticas (`*`, `/`).
- **Prohibido:** Usar la palabra `def`. Usar la palabra `return`. Que las operaciones de tus lambdas ocupen más de una línea.

## 🎯 Resultado Esperado en Terminal

Cuando ejecutes tu código, la terminal debería mostrar algo exactamente como esto:

```text
El cuadrado de 5 es: 25
El área del triángulo (base 10, altura 4) es: 20.0
```
