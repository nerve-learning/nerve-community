# Reto 77: El Menú del Restaurante 🍔

Estás diseñando el software para la caja registradora de un restaurante. El cajero necesita poder ver el nombre y el precio de cada platillo en la pantalla de una forma clara y bonita.

## 📝 Instrucciones

1. Crea una clase llamada `Platillo`.
2. Crea el método `__init__`. Debe recibir `self`, el `nombre` del platillo, y su `precio`. Guárdalos en `self.nombre` y `self.precio`.
3. Crea el método dunder `__str__(self)`.
4. Dentro de `__str__`, **devuelve** (`return`) una cadena de texto formateada que se vea exactamente así: `"[nombre] - $[precio]"`.
5. Fuera de tu clase (sin espacios a la izquierda), crea un objeto de la clase `Platillo`. Ponle de nombre `"Pizza Familiar"` y de precio `15`. Guárdalo en una variable llamada `mi_cena`.
6. Haz un simple `print(mi_cena)`.

## ⛔ Reglas estrictas
- **SÍ puedes:** Usar `class`, `__init__`, `__str__`, `return` y cadenas formateadas (`f"..."`).
- **NO puedes:** Usar la palabra `print` adentro de la clase `Platillo`. El único `print` permitido es el del paso 6, por fuera de la clase.

## 🎯 Resultado esperado en la terminal

Cuando ejecutes tu código, deberías ver la magia de Python mostrando exactamente esto:

```text
Pizza Familiar - $15
```

¡Demuestra tu maestría con los métodos mágicos!
