# Reto 89: El Oráculo del Clima ☁️

Has sido contratado para crear la lógica base de un bot de clima basado en "IA simulada". 
Tu misión es escribir un script que reciba preguntas sobre el clima de diferentes ciudades y devuelva un pronóstico.

## Instrucciones

1. Crea una función llamada `oraculo_clima` que reciba un parámetro llamado `prompt`.
2. Dentro de la función, simula un tiempo de espera de 1 segundo (¡ya sabes cómo!).
3. Si el `prompt` contiene la palabra "madrid", devuelve: `"En Madrid hará sol, 25 grados."`
4. Si el `prompt` contiene "londres", devuelve: `"En Londres lloverá, no olvides tu paraguas."`
5. Si no menciona ninguna de esas ciudades, devuelve: `"Lo siento, mis satélites no llegan ahí aún."`
6. Fuera de la función, haz 3 llamadas a tu oráculo usando 3 `print()` distintos: uno preguntando por Madrid, otro por Londres, y otro por Bogotá.

### Conceptos permitidos:
- Funciones (`def`, `return`)
- Condicionales (`if`, `elif`, `else`)
- Búsqueda en cadenas (`in`)
- `time.sleep()` (del Módulo OS/Utilidades)
- Impresión en consola (`print`)

### Conceptos prohibidos:
- Diccionarios (queremos que practiques la lógica de condicionales con texto)
- APIs reales (manténlo simple simulando la respuesta)

### Resultado esperado en la terminal:
```text
Consultando a los astros por Madrid...
🤖 Oráculo: En Madrid hará sol, 25 grados.

Consultando a los astros por Londres...
🤖 Oráculo: En Londres lloverá, no olvides tu paraguas.

Consultando a los astros por Bogotá...
🤖 Oráculo: Lo siento, mis satélites no llegan ahí aún.
```
