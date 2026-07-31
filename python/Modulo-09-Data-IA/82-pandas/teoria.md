# Teoría: De Diccionarios a Tablas de Excel

Al igual que hicimos con Numpy, para usar Pandas necesitamos traer la herramienta a nuestro programa. Por convención, todo el mundo le pone el apodo `pd`.

## Anatomía de Pandas

```python
import pandas as pd
```
- **`import pandas`**: Le dice a la computadora "trae la caja de herramientas de análisis de datos".
- **`as pd`**: Le dice "te llamaré 'pd' para no escribir tu nombre completo cada vez".

Para crear una tabla, Pandas necesita que le demos los datos organizados. La forma más fácil de hacerlo es usando algo que ya conoces: un **Diccionario** de Python, donde las *llaves* (claves) serán los nombres de las columnas, y los *valores* serán listas con los datos.

```python
datos = {
    "Nombre": ["Ana", "Beto", "Carlos"],
    "Edad": [25, 30, 22]
}
mi_tabla = pd.DataFrame(datos)
```

- **`pd.`**: Usa la herramienta 'pd' (Pandas).
- **`DataFrame`**: Es el creador de tablas. Significa literalmente "Marco de Datos". ¡Nota que la `D` y la `F` son mayúsculas!
- **`(datos)`**: Los paréntesis le entregan nuestro diccionario para que lo transforme en una tabla hermosa con filas y columnas.

Una vez que tienes tu tabla, puedes ver una sola columna pidiéndosela por su nombre entre corchetes, igual que en los diccionarios:
```python
columna_edades = mi_tabla["Edad"]
```

## ¿Qué pasa si me equivoco?

### Error 1: Escribir mal DataFrame
**El error:** `pd.Dataframe(datos)` o `pd.dataframe(datos)`
La terminal te gritará:
`AttributeError: module 'pandas' has no attribute 'Dataframe'`
**¿Por qué?** Python diferencia mayúsculas de minúsculas. El comando exacto tiene la `D` y la `F` mayúsculas. 
**La solución:** Escribe `pd.DataFrame(...)`.

### Error 2: Listas de diferente tamaño
**El error:** 
```python
datos = {
    "Nombre": ["Ana", "Beto"], # 2 elementos
    "Edad": [25, 30, 22]       # 3 elementos
}
pd.DataFrame(datos)
```
La terminal explotará con un error larguísimo que termina en:
`ValueError: All arrays must be of the same length`
**¿Por qué?** Piensa en una tabla de Excel. No puedes tener una columna con 2 filas y otra con 3 filas en la misma tabla de datos estructurados. Todas las columnas deben tener exactamente la misma cantidad de datos.
**La solución:** Asegúrate de que todas tus listas dentro del diccionario tengan el mismo número de elementos.
