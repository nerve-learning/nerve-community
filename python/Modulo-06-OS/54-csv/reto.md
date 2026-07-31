# Reto 54: El Analista de Datos 📈

¡Felicidades, conseguiste tu primer empleo en un cine! Tu jefe te pide que guardes un registro de las mejores películas y su calificación, y luego necesitas poder leerlo de vuelta para comprobar que no hubo errores.

### Instrucciones paso a paso:

1. Importa la caja de herramientas correcta en la primera línea.
2. Crea una variable llamada `peliculas` que contenga una **lista de listas**. Adentro debe tener 3 listas más pequeñas, cada una con el nombre de una película y su calificación (un número). 
   *(Ejemplo: `[["Shrek", 10], ["Titanic", 8], ["Matrix", 9]]`)*.
3. Crea una función (con `def`) llamada `guardar_peliculas(lista_peliculas)` que reciba esa lista.
4. Dentro de la función, abre un archivo `"mis_peliculas.csv"` en modo `"w"`. ¡No olvides poner `newline=""`!
5. Crea a tu trabajador experto (`csv.writer()`).
6. Usa `.writerow()` para escribir primero los encabezados: `["Titulo", "Calificacion"]`.
7. Usa un bucle `for` para recorrer tu lista `lista_peliculas`, y dentro del bucle usa `.writerow()` para guardar cada película en el archivo.
8. Afuera de la función, llámala pasándole tu lista `peliculas` original.
9. Ahora, crea **otra** función llamada `leer_peliculas()` que no reciba ningún parámetro.
10. Adentro de esta nueva función, abre tu archivo `"mis_peliculas.csv"` en modo lectura `"r"`.
11. Crea a tu trabajador experto (`csv.reader()`).
12. Usa un bucle `for` para imprimir cada fila del archivo.
13. Llama a tu segunda función para verificar que los datos se guardaron y leyeron bien.

---

### 🟢 Conceptos Permitidos (Lo único que puedes usar)
* `import csv`
* Trabajadores (`csv.reader(archivo)` y `csv.writer(archivo)`)
* Escribir fila (`.writerow(lista)`)
* Apertura de archivos (`with open(...)`) y parámetro `newline=""`
* Listas y bucles (`for fila in tabla:`)
* Funciones (`def`) y llamadas a funciones.
* Imprimir a la terminal (`print()`)

### 🔴 Prohibido
* Usar `.read()` crudo (hoy queremos usar el lector de tablas).
* Usar librerías externas avanzadas como `pandas`.
* Copiar y pegar código de internet.

---

### 🎯 Resultado esperado en la terminal
*(Nota: Cuando Python lee de vuelta un CSV, convierte todo a texto. Es normal que tus números de calificación salgan con comillas `'10'` en la terminal, porque para el archivo de texto, ¡todo es texto!)*

```text
['Titulo', 'Calificacion']
['Shrek', '10']
['Titanic', '8']
['Matrix', '9']
```

¡Demuestra que la magia de los datos no tiene secretos para ti!
