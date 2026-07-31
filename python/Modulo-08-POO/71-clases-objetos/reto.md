# Reto 71: La Fábrica de Monstruos 🧟

¡Es hora de que construyas tu propia fábrica! Vas a crear un molde para hacer monstruos y luego le darás vida a un par de ellos.

## 📝 Instrucciones

1. Crea una clase llamada `Monstruo`.
2. Escribe su constructor (la función especial `__init__`). Debe recibir `self`, el `nombre` del monstruo y una variable booleana llamada `asustador` (`True` o `False`).
3. Guarda esos dos valores dentro de tu objeto usando `self.nombre` y `self.asustador`.
4. Crea una función dentro de la clase llamada `rugir(self)`.
   - Dentro de esa función, usa un bloque `if`/`else` que verifique si `self.asustador` es `True`.
   - Si es `True`, haz un `print` que diga: `"¡ROAAAR! Soy [su nombre] y doy mucho miedo."`
   - Si es `False`, haz un `print` que diga: `"Grrr... Soy [su nombre] pero soy amigable."`
5. Fuera de tu clase (sin espacios a la izquierda), crea dos monstruos:
   - El primer monstruo se llamará `"Sulley"` y será asustador (`True`).
   - El segundo monstruo se llamará `"Mike"` y no será asustador (`False`).
6. Haz que ambos monstruos llamen a su función `rugir()`.

## ⛔ Reglas estrictas
- **SÍ puedes:** Usar `class`, `def`, `__init__`, `self`, `if`, `else`, variables booleanas y `print()`. 
- **NO puedes:** Usar diccionarios, bucles `for`, o crear funciones por fuera de la clase. Todo debe vivir dentro de la anatomía que acabamos de aprender.

## 🎯 Resultado esperado en la terminal

Cuando ejecutes tu código, deberías ver exactamente esto en tu pantalla:

```text
¡ROAAAR! Soy Sulley y doy mucho miedo.
Grrr... Soy Mike pero soy amigable.
```

¡Tú puedes! Si te equivocas y Python te grita un error rojo, vuelve a leer la sección de *¿Qué pasa si me equivoco?* en el archivo `teoria.md`.
