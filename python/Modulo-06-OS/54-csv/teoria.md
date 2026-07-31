# El Módulo `csv`

Imagina una hoja de cálculo. Un archivo CSV es exactamente eso, pero "desnudo": es un simple archivo de texto donde cada renglón es una fila de la tabla, y cada columna está separada por una coma (`,`).

Podríamos leer un CSV usando el `.read()` que aprendimos antes, pero tendríamos que pelear buscando las comas y partiendo el texto a mano. ¡Qué pereza! Mejor traemos una nueva caja de herramientas: el módulo `csv`.

---

### Anatomía de los nuevos símbolos

Para usar estas herramientas mágicas, primero debemos hacer `import csv`. 

#### 1. Sintaxis para Leer Tablas
```python
import csv

with open("empleados.csv", "r") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)
```
* **`import csv`**: Trae la caja de herramientas para manejar tablas.
* **`csv.reader(archivo)`**: Es nuestro trabajador experto. Toma tu archivo recién abierto y lo convierte en un "Lector". Este lector sabe mágicamente dónde están las comas y los renglones.
* **`for fila in lector:`**: Como una tabla tiene muchas filas, usamos nuestro confiable bucle `for` para recorrerlas. Cada vez que da una vuelta, la variable `fila` se convierte en una **Lista de Python** con los datos de esa fila. ¡Súper fácil de usar!

#### 2. Sintaxis para Escribir Tablas
```python
import csv

with open("ventas.csv", "w", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Manzanas", 10])
```
* **`newline=""`**: Es un ajuste de seguridad para el guardián `with`. Si no lo ponemos, algunas computadoras (como Windows) se confunden y agregan renglones vacíos extra entre cada fila de tu tabla. Le dice a Python: *"No agregues saltos de línea extra por tu cuenta"*.
* **`csv.writer(archivo)`**: Es nuestro trabajador experto en escritura. Transforma nuestras listas de Python y les pone las comas en su lugar antes de guardarlas.
* **`.writerow()`**: Significa *Write Row* (Escribir Fila). Toma una lista de Python y la guarda como un renglón en la tabla.

---

### ⚠️ ¿Qué pasa si me equivoco?

**El error del texto desmembrado**
Si al usar `.writerow()` olvidas poner corchetes de lista `[]` e intentas escribir un texto libre así: 
`escritor.writerow("Hola")`

Al abrir tu tabla verás que Python escribió esto:
`H,o,l,a`

**¿Por qué pasa esto?**
El escritor (`csv.writer`) **siempre** espera recibir una caja (una lista de columnas). Si le das una simple palabra, cree que cada letra es una columna distinta y las separa con comas. 
**Solución**: ¡Asegúrate siempre de pasarle listas! Correcto: `escritor.writerow(["Hola"])`.
