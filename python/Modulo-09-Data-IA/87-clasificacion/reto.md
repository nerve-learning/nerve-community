# Reto 87: El Filtro Anti-Spam

Acabas de conseguir trabajo en una empresa de correo electrónico y tu jefe te pide crear una IA que mueva los correos basura a la carpeta de Spam automáticamente.

Has analizado correos anteriores y descubriste dos pistas clave: 
- ¿Cuántos links tiene el correo? 
- ¿Cuántas palabras en MAYÚSCULAS tiene?

Tus datos históricos son:
- Pistas (X) `[links, MAYUSCULAS]`: 
  `[[0, 2], [1, 5], [10, 50], [15, 80]]`
- Etiquetas (y): 
  `["Normal", "Normal", "Spam", "Spam"]`

De pronto, llega a la bandeja de entrada un correo nuevo que tiene **12 links** y **60 palabras en MAYÚSCULAS** (`[[12, 60]]`).

### Pasos a seguir:
1. Trae a la clase `DecisionTreeClassifier` desde `sklearn.tree`.
2. Crea tus variables para las pistas del pasado (con dobles corchetes) y para las etiquetas de esos correos.
3. Crea tu IA ejecutando `DecisionTreeClassifier()` y guárdala en una variable.
4. Usa `.fit()` para que tu IA estudie las pistas y las etiquetas.
5. Usa `.predict()` para que analice el correo nuevo (`[[12, 60]]`).
6. Imprime el resultado de la predicción en la terminal.

### Reglas estrictas:
- **PERMITIDO:** `DecisionTreeClassifier`, `fit()`, `predict()`, listas `[]`, `print()`.
- **PROHIBIDO:** Usar `LinearRegression`, resolverlo mentalmente sin usar `.predict()`.

### Resultado esperado en la terminal:
*(La IA deberá deducir la etiqueta correcta basándose en los números altos del correo nuevo)*
```text
['Spam']
```
