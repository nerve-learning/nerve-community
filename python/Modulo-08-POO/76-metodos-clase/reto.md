# Reto 76: La Pizzería 🍕

Eres el administrador de la mejor Pizzería de la ciudad. Necesitas un sistema que no solo prepare las pizzas, sino que lleve la cuenta exacta de cuántas pizzas se han vendido en total durante el día para el reporte financiero.

## 📝 Instrucciones

1. Crea una clase llamada `Pizzeria`.
2. Crea una variable de clase llamada `pizzas_vendidas` y ponla en `0`. (Recuerda: va debajo del nombre de la clase, pero fuera de cualquier función).
3. Escribe el `__init__`. Debe recibir `self` y el `sabor` de la pizza.
   - Guarda el sabor en `self.sabor`.
   - Luego, súmale `1` a la variable de clase `Pizzeria.pizzas_vendidas`.
4. Crea un método de clase usando `@classmethod` llamado `reporte_ventas(cls)`.
   - Dentro de esta función, haz un `print` que diga: `"¡Hemos vendido [cantidad] pizzas en total!"` (usando `cls.pizzas_vendidas`).
5. Fuera de tu clase, hornea (crea) 3 pizzas distintas (ej. `"Pepperoni"`, `"Hawaiana"`, `"Queso"`).
6. Finalmente, llama a la función de reporte de ventas a través de la clase (es decir, `Pizzeria.reporte_ventas()`).

## ⛔ Reglas estrictas
- **SÍ puedes:** Usar `class`, `@classmethod`, `cls`, variables de clase y `__init__`.
- **NO puedes:** Intentar guardar el total de pizzas dentro del `self` de una pizza. ¡Una pizza no debería tener el registro financiero del restaurante!
- **NO puedes:** Pasar `self` como parámetro a la función `reporte_ventas`. ¡Debe recibir `cls`!

## 🎯 Resultado esperado en la terminal

Cuando ejecutes tu código, deberías ver exactamente esto (aunque tus pizzas tengan otros sabores):

```text
¡Hemos vendido 3 pizzas en total!
```

¡Es hora de ponerte el delantal de gerente y organizar esas ventas!
