# Reto 48: El Oráculo del Destino 🔮

Tu aldea necesita tomar una decisión importante, así que han construido un Oráculo digital. El Oráculo seleccionará aleatoriamente un presagio de una lista secreta para guiar el destino del pueblo.

## 📝 Instrucciones

1. Crea un archivo llamado `reto.py`.
2. En la línea 1, importa **solo la herramienta `choice`** desde la caja `random` usando la estructura `from ... import ...`.
3. Define una función llamada `predecir_futuro`.
4. Dentro de la función, crea una lista (que aprendiste en el módulo de Estructuras) llamada `presagios` que contenga estas 4 frases:
   - `"Lloverá oro mañana."`
   - `"Un dragón atacará al mediodía."`
   - `"Encontrarás la paz en tu interior."`
   - `"No salgas de casa hoy."`
5. Usa la herramienta `choice()` pasándole tu lista `presagios` para obtener un destino al azar, y usa `return` para devolver ese destino hacia afuera.
6. Fuera de la función, usa un bucle `for` que se repita 3 veces (para pedir 3 profecías distintas).
7. En cada repetición del bucle, llama a tu función, atrapa el resultado en una variable, y usa `print` para mostrar: `"El oráculo ha hablado: [resultado]"`.

### 🚦 Reglas Estrictas
- **Conceptos permitidos:** `from`, `import`, `def`, listas (`[]`), `return`, bucles `for` o `while`, `print`.
- **Prohibido:** Crear los presagios fuera de la función. Escribir `import random` (debes importar solo la herramienta `choice` como dice la instrucción 2).

## 🎯 Resultado Esperado en Terminal

Cuando ejecutes tu código, la terminal debería mostrar 3 frases al azar de tu lista (obviamente pueden variar en cada ejecución):

```text
El oráculo ha hablado: Un dragón atacará al mediodía.
El oráculo ha hablado: Lloverá oro mañana.
El oráculo ha hablado: Lloverá oro mañana.
```
*(Nota: Como es azar, es normal si alguna frase se repite).*
