# Reto 47: El Eco de la Caverna 🗣️

Has entrado en una caverna mágica. Cuando gritas una palabra, la caverna la repite varias veces, pero cada vez que lo hace, el sonido es más débil hasta que desaparece.

¡Vamos a simular esto SIN usar bucles `for` ni `while`! Vas a usar la técnica del espejo infinito (recursividad).

## 📝 Instrucciones

1. Crea un archivo llamado `reto.py`.
2. Define una función llamada `hacer_eco` que reciba dos parámetros: `palabra` y `veces`.
3. Lo primero que debe hacer tu función es el **Caso Base (el freno)**: usa un `if` para revisar si `veces` es igual a `0`. Si lo es, imprime `"..."` (el silencio final) y usa `return` para salirte de la función.
4. Si no entró al `if`, la función debe hacer su acción normal: imprimir la `palabra`.
5. Después del `print`, viene la **Llamada Recursiva (el espejo)**. Haz que la función se llame a sí misma (`hacer_eco(...)`), pasándole la *misma* `palabra`, pero el problema debe ser más pequeño: así que pásale `veces - 1`.
6. Fuera de tu función (en el pasillo principal del programa), llama a tu función así: `hacer_eco("¡Hola!", 3)`.

### 🚦 Reglas Estrictas
- **Conceptos permitidos:** `def`, parámetros, `if`, `return`, `print`, y llamar a la función desde sí misma.
- **Prohibido:** Usar `while` o `for`. El eco debe generarse 100% mediante recursividad. Olvidar el `if` (tu computadora se quejará con un error).

## 🎯 Resultado Esperado en Terminal

Cuando ejecutes tu código, la terminal debería mostrar algo exactamente como esto:

```text
¡Hola!
¡Hola!
¡Hola!
...
```
*(Fíjate que la palabra sale 3 veces, y luego el "..." indica que el eco chocó con el freno y terminó).*
