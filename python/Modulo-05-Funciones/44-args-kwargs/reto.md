# Reto 44: El Inventario Infinito 🎒

En tu juego RPG, el aventurero puede recoger cualquier cantidad de objetos en su aventura. A veces recoge 2 objetos, a veces recoge 50. Además, el aventurero tiene estadísticas mágicas que pueden variar (algunas veces tiene `fuerza`, otras veces tiene `suerte` y `carisma`).

Tu trabajo es crear una función maestra capaz de recibir TODO esto sin importar la cantidad.

## 📝 Instrucciones

1. Crea un archivo llamado `reto.py`.
2. Define una función llamada `guardar_progreso`.
3. Tu función debe recibir, en este estricto orden:
   - Un parámetro obligatorio llamado `personaje`.
   - La caja infinita para objetos sueltos `*objetos` (args).
   - El archivero de etiquetas para estadísticas `**estadisticas` (kwargs).
4. Dentro de la función, usa `print` para mostrar el nombre del `personaje`.
5. Usa un bucle `for` para recorrer la tupla `objetos` e imprimir cada uno.
6. Usa otro bucle `for` para recorrer el diccionario `estadisticas` e imprimir el nombre de la estadística y su valor (ej: `fuerza : 99`).
7. Fuera de la función, llama a tu función pasándole los siguientes datos en una sola línea:
   - Nombre: `"Geralt"`
   - Objetos sueltos: `"Espada de Plata"`, `"Poción Curativa"`, `"Cabeza de Grifo"`.
   - Estadísticas con etiqueta: `fuerza=150`, `magia=50`, `agilidad=80`.

### 🚦 Reglas Estrictas
- **Conceptos permitidos:** `def`, `*args`, `**kwargs`, bucles `for`, `print`.
- **Prohibido:** Modificar los valores de las tuplas o diccionarios dentro de la función. Solo debes recorrerlos y mostrarlos.

## 🎯 Resultado Esperado en Terminal

Cuando ejecutes tu código, la terminal debería mostrar algo exactamente como esto:

```text
Guardando progreso de: Geralt
--- Objetos en la mochila ---
- Espada de Plata
- Poción Curativa
- Cabeza de Grifo
--- Estadísticas ---
fuerza : 150
magia : 50
agilidad : 80
```
*(Nota: Asegúrate de añadir los `print("--- Objetos en la mochila ---")` y similares en tu código para que quede ordenado).*
