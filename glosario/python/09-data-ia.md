# 09 - Data e IA

### `numpy`

**¿Qué es?**
Librería fundamental de Python para cálculo numérico que permite manejar arrays (arreglos) y matrices grandes y multidimensionales de forma muy eficiente.

**¿Para qué se usa?**
Para hacer operaciones matemáticas complejas o procesar grandes cantidades de números mucho más rápido que usando listas estándar de Python.

**Ejemplo:**
```python
import numpy as np
numeros = np.array([1, 2, 3, 4, 5])
print(numeros * 2) # Multiplica todo el array de golpe sin bucles
```

**Errores comunes de principiante:**
- Confundir una lista de Python con un array de numpy.
- No importar la librería con el alias estándar `np`.

**Términos relacionados:** [`pandas`](#pandas--dataframe--series)

### `pandas` / `DataFrame` / `Series`

**¿Qué es?**
Pandas es una librería para análisis y manipulación de datos. Una `Series` es una columna de datos (1D), y un `DataFrame` es una tabla completa de datos (2D), similar a una hoja de cálculo de Excel.

**¿Para qué se usa?**
Para cargar, limpiar, transformar y analizar tablas de datos estructurados de forma rápida y sencilla.

**Ejemplo:**
```python
import pandas as pd
datos = pd.DataFrame({'Nombre': ['Ana', 'Luis'], 'Edad': [25, 30]})
print(datos)
```

**Errores comunes de principiante:**
- Intentar usar bucles `for` para modificar un DataFrame, lo cual es muy lento (es mejor usar operaciones vectorizadas).
- Olvidarse de manejar los valores nulos o vacíos antes de analizar los datos.

**Términos relacionados:** [`CSV`](#csv), [`numpy`](#numpy)

### `matplotlib`

**¿Qué es?**
Es la librería principal de Python para crear gráficos y visualizaciones de datos estáticas, animadas o interactivas.

**¿Para qué se usa?**
Para visualizar datos gráficamente (ej: gráficos de líneas, barras, dispersión) y entender mejor las tendencias o resultados de un modelo.

**Ejemplo:**
```python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 2])
plt.show()
```

**Errores comunes de principiante:**
- Olvidar llamar a `plt.show()` y preguntarse por qué no aparece el gráfico.

**Términos relacionados:** [`pandas`](#pandas--dataframe--series)

### `scikit-learn`

**¿Qué es?**
Una librería de Machine Learning que proporciona herramientas simples y eficientes para minería de datos y análisis de datos. Incluye algoritmos como regresión, clasificación y agrupamiento.

**¿Para qué se usa?**
Para entrenar modelos de Inteligencia Artificial tradicionales (no redes neuronales complejas) que aprenden patrones a partir de los datos.

**Ejemplo:**
```python
from sklearn.linear_model import LinearRegression
modelo = LinearRegression()
# modelo.fit(X, y) # Entrena el modelo
# predicciones = modelo.predict(nuevos_X)
```

**Errores comunes de principiante:**
- Pasar datos al modelo sin haberlos limpiado (con valores nulos o texto sin convertir a números).
- No dividir los datos en conjuntos de entrenamiento y prueba.

**Términos relacionados:** [`regresión lineal`](#regresión-lineal-vs-clasificación)

### `regresión lineal` vs `clasificación`

**¿Qué es?**
Son dos tipos principales de problemas en Machine Learning predictivo. La regresión predice un valor numérico continuo (ej: el precio de una casa). La clasificación predice una categoría (ej: si un correo es spam o no).

**¿Para qué se usa?**
Para decidir qué tipo de algoritmo de IA necesitas usar según lo que quieras adivinar o predecir en tu programa.

**Ejemplo:**
```python
# Regresión: predecir un precio (ej. 1500.50)
# Clasificación: predecir una etiqueta (ej. "Aprobado" o "Reprobado")
```

**Errores comunes de principiante:**
- Usar un algoritmo de clasificación cuando se quiere predecir un número (regresión), o viceversa.

**Términos relacionados:** [`scikit-learn`](#scikit-learn)

### `CSV`

**¿Qué es?**
Comma-Separated Values (Valores Separados por Comas). Es un formato de archivo de texto muy simple para guardar datos tabulares, donde cada línea es una fila y las columnas se separan por comas.

**¿Para qué se usa?**
Es el formato universal y más ligero para compartir datos (datasets) entre distintos programas, bases de datos y algoritmos de IA.

**Ejemplo:**
```csv
nombre,edad,ciudad
Ana,25,Madrid
Luis,30,Bogotá
```

**Errores comunes de principiante:**
- Usar comas dentro de los valores (ej: "Ana, María") sin entrecomillar el texto, rompiendo la estructura de columnas del archivo.

**Términos relacionados:** [`pandas`](#pandas--dataframe--series)

### `correlación` y `feature`

**¿Qué es?**
Una `feature` (característica) es cada variable o columna de información que usas para hacer una predicción (ej: la edad o los ingresos). La `correlación` mide qué tan fuerte es la relación matemática entre dos cosas (ej: a más altura, mayor peso).

**¿Para qué se usa?**
Para saber qué columnas de datos son realmente útiles (buenas "features") para entrenar a nuestro modelo de IA y cuáles deberíamos descartar.

**Ejemplo:**
```python
# Un DataFrame tiene múltiples columnas (features)
# datos.corr() mostraría la correlación entre ellas
```

**Errores comunes de principiante:**
- Creer que correlación implica causalidad (que si dos cosas suben a la vez, una causa a la otra, lo cual es falso).
- Meter todas las columnas (features) posibles al modelo sin pensar si realmente tienen sentido o correlación con lo que se quiere predecir.

**Términos relacionados:** [`scikit-learn`](#scikit-learn), [`pandas`](#pandas--dataframe--series)
