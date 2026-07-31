# Reto 113: La Invasión Espacial 🛸

Imagina que eres el comandante de una base de defensa. Detectas dos naves enemigas gigantes.
Tu cañón láser necesita "cargar energía" durante 4 segundos para disparar.
Si disparas a una y luego cargas para la otra, pasarán 8 segundos y la base será destruida.
¡Necesitas clonar al operador del cañón para disparar a ambas naves al mismo tiempo!

### 📝 Instrucciones:

1. Crea un archivo Python desde cero.
2. Importa la librería `multiprocessing` y la librería `time`.
3. Crea una función llamada `cargar_y_disparar`. Dentro de ella:
   - Imprime: `"Cargando cañon laser..."`
   - Usa `time.sleep(4)` para simular la carga.
   - Imprime: `"💥 ¡BOOM! Nave destruida."`
4. Escribe el "Escudo Anti-Rebelión" (`if __name__ == '__main__':`).
5. DENTRO del escudo (indentado), crea dos clones usando `multiprocessing.Process` que tengan como `target` tu función de disparo.
6. Enciende ambos clones con `.start()`.
7. Obliga a tu programa principal a esperarlos a ambos usando `.join()`.
8. Imprime al final: `"🏆 Base salvada, buen trabajo comandante."`

### ⛔ Reglas Estrictas:
* **Permitido**: Crear funciones, importar `multiprocessing` y `time`, usar `Process`, `start`, `join`, y el condicional `if __name__ == '__main__':`.
* **Prohibido**: Ejecutar `cargar_y_disparar()` con paréntesis adentro del `target`.
* **Prohibido**: No usar el escudo `if __name__ == '__main__':`. (¡No queremos que tu PC explote!).

### 🎯 Resultado Esperado en la Terminal:
Deberías ver que los dos "Cargando..." aparecen inmediatamente al mismo tiempo, y 4 segundos después, ambas explosiones ocurren casi a la vez.

```text
Cargando cañon laser...
Cargando cañon laser...
💥 ¡BOOM! Nave destruida.
💥 ¡BOOM! Nave destruida.
🏆 Base salvada, buen trabajo comandante.
```
