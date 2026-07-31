# Reto 12: Escáner de Aeropuerto ✈️🧳

Eres el programador encargado del escáner automático de equipaje de una aerolínea. Tienes que crear las variables que comparan el equipaje del pasajero contra las reglas estrictas de la aerolínea, y reportar si todo está en orden o hay problemas.

## Instrucciones

1. Crea tres variables para el equipaje de un pasajero (inviéntate los datos, por ejemplo):
   * `peso_maleta` (un número, ej. `23.5`).
   * `etiqueta_destino` (un texto, ej. `"PARIS"`).
   * `cantidad_liquidos` (un entero, ej. `150`).

2. **Regla de peso (usa `<=`)**: 
   La maleta no debe pesar más de 25 kilos (es decir, debe ser menor o igual a 25). 
   Crea una variable llamada `peso_permitido` que guarde el resultado de comparar el `peso_maleta` con `25`.

3. **Regla de destino (usa `==`)**: 
   El vuelo actual va hacia `"LONDRES"`.
   Crea una variable llamada `destino_correcto` que compare si la `etiqueta_destino` del pasajero es exactamente igual a `"LONDRES"`.

4. **Regla de líquidos (usa `>`)**: 
   Los pasajeros tienen prohibido llevar frascos de líquidos que superen los 100 mililitros.
   Crea una variable llamada `excede_liquidos` que compare si la `cantidad_liquidos` es estrictamente mayor a `100`.

5. Muestra un reporte en la terminal utilizando `f-strings`.

### Conceptos permitidos
- Variables (asignación con `=`).
- Tipos de datos (`int`, `float`, `str`, `bool`).
- Los 6 operadores de comparación (`==`, `!=`, `>`, `<`, `>=`, `<=`).
- Imprimir en pantalla con `print()` y `f-strings`.

### Conceptos prohibidos
- Operadores lógicos (`and`, `or`, `not`). Vamos a probar solo los comparadores puros en este nivel.
- Condicionales (`if`, `else`, `elif`).
- Funciones `def`.

### Resultado esperado en terminal
Si usaste `peso_maleta = 23.5`, `etiqueta_destino = "PARIS"` y `cantidad_liquidos = 150`, tu terminal debe verse exactamente así:

```text
--- REPORTE DE ESCÁNER DE EQUIPAJE ---
¿El peso de la maleta está permitido?: True
¿La maleta va al destino correcto (LONDRES)?: False
¿El pasajero excede el límite de líquidos?: True
```
