# Reto 83: El Rescate del Inventario

Eres el encargado de sistemas de una zapatería. El sistema de inventario falló y a algunos zapatos se les borró el precio (quedaron como `None`). 

No puedes borrar los zapatos de la base de datos (¡prohibido usar `dropna`!), así que tu jefe te pide que a todos los zapatos que no tengan precio, les pongas temporalmente un precio de `10` dólares para no perderlos en el sistema.

### Pasos a seguir:
1. Trae a Pandas y ponle su apodo `pd`.
2. Tienes el siguiente diccionario, cópialo en tu código:
   ```python
   inventario_sucio = {
       "Zapato": ["Tenis", "Bota", "Sandalia", "Mocasín"],
       "Precio": [50, None, 15, None]
   }
   ```
3. Convierte ese diccionario en una tabla y guárdalo en una variable llamada `tabla_inventario`.
4. Crea una variable llamada `tabla_salvada`.
5. Usa la herramienta adecuada de Pandas para rellenar los huecos de tu `tabla_inventario` con el número `10`, y guarda el resultado en `tabla_salvada`.
6. Imprime `tabla_salvada` en la terminal.

### Reglas estrictas:
- **PERMITIDO:** `import pandas as pd`, `pd.DataFrame()`, `fillna()`, `print()`, usar la palabra `None`.
- **PROHIBIDO:** Usar `dropna()`. Modificar el diccionario a mano para quitar los `None`. ¡Pandas debe hacer el trabajo!

### Resultado esperado en la terminal:
```text
     Zapato  Precio
0     Tenis    50.0
1      Bota    10.0
2  Sandalia    15.0
3   Mocasín    10.0
```
