# Reto 45: El Contador de Monedas 🪙

Estás programando la billetera de un personaje en un juego. El personaje puede encontrar cofres que le dan monedas, y puede comprar objetos que le restan monedas.

Como el oro del jugador tiene que mantenerse guardado a través de todo el juego, la cantidad de monedas debe ser una variable global.

## 📝 Instrucciones

1. Crea un archivo llamado `reto.py`.
2. En la línea 1 (sin espacios a la izquierda), crea una variable global llamada `monedas_totales` y asígnale el valor `0`.
3. Define una función llamada `encontrar_cofre` que reciba 1 parámetro: `cantidad`.
4. Dentro de `encontrar_cofre`, usa la palabra mágica para avisar que vas a modificar `monedas_totales`. Luego, súmale la `cantidad` a las monedas totales e imprime `"¡Encontraste [cantidad] monedas!"`.
5. Define otra función llamada `comprar_pocion` que reciba 1 parámetro: `costo`.
6. Dentro de `comprar_pocion`, vuelve a avisar que usarás la variable global. Usa un `if` para revisar:
   - Si `monedas_totales` es mayor o igual al `costo`: réstale el costo a las monedas totales e imprime `"Poción comprada por [costo] monedas."`.
   - Si no (`else`): imprime `"No tienes suficiente oro para la poción."`.
7. Fuera de las funciones, realiza esta secuencia de comandos:
   - Llama a `encontrar_cofre` y pásale `50`.
   - Llama a `comprar_pocion` y pásale `20`.
   - Llama a `comprar_pocion` y pásale `40`.
   - Imprime el estado final del oro: `"Oro restante: [monedas_totales]"`.

### 🚦 Reglas Estrictas
- **Conceptos permitidos:** `def`, variables globales, `global`, parámetros, `if/else`, operaciones matemáticas (`+`, `-`).
- **Prohibido:** Crear variables locales dentro de las funciones para llevar la cuenta del dinero. Todo debe modificar la única variable global `monedas_totales`.

## 🎯 Resultado Esperado en Terminal

Cuando ejecutes tu código, la terminal debería mostrar algo exactamente como esto:

```text
¡Encontraste 50 monedas!
Poción comprada por 20 monedas.
No tienes suficiente oro para la poción.
Oro restante: 30
```
