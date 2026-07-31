# Teoría: La Bolsa de Palabras (Bag of Words)

Imagina que tienes que explicarle el guion de una película a un robot extraterrestre sordo, ciego y que solo entiende de sumas. La única forma de comunicarte con él es entregarle un papel que diga:
- La palabra "Amor" aparece 50 veces.
- La palabra "Muerte" aparece 0 veces.
- La palabra "Feliz" aparece 30 veces.

Con solo ver esos números, el robot deducirá: "Ah, es una película romántica". Esto se llama **Bag of Words**. Rompemos las oraciones en palabras sueltas y simplemente contamos cuántas veces aparece cada una.

Para no hacer esto a mano, Scikit-Learn tiene un traductor experto.

## Anatomía del Traductor

```python
from sklearn.feature_extraction.text import CountVectorizer
```
- Traemos de la caja de herramientas de texto al `CountVectorizer` (El "Vectorizador por Conteo", nuestro traductor estrella).

```python
traductor = CountVectorizer()
```
- **Instanciamos** a nuestro traductor (creamos un objeto nuevo).

```python
numeros = traductor.fit_transform(lista_de_textos)
```
- **`fit_transform`**: Es un súper poder que hace dos cosas al mismo tiempo: 
  1. `fit` (Aprender): Lee todos los textos para descubrir qué palabras existen en tu idioma.
  2. `transform` (Traducir): Reemplaza tus textos originales por números (las cuentas de las palabras).

## ¿Qué pasa si me equivoco?

### El error de la Matriz Comprimida
**El error:**
Imprimes el resultado directamente: `print(numeros)`
En la terminal no verás tus hermosos números, sino algo escalofriante como:
`<3x5 sparse matrix of type '<class 'numpy.int64'>' with 8 stored elements in Compressed Sparse Row format>`

**¿Por qué?** Si le das un diccionario entero a la computadora, el 99% de las palabras tendrán un conteo de `0` en tu oración. Para no desperdiciar memoria RAM guardando millones de ceros inútiles, el traductor "comprime" los resultados.
**La solución:** Cuando quieras ver los números con tus propios ojos humanos, debes pedirle que descomprima la matriz usando `.toarray()` al momento de imprimir:
`print(numeros.toarray())`.
