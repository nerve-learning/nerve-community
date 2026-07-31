# Teoría: Canicas y Palos de Escoba

Imagina que tiras un puñado de canicas al suelo. Las canicas caen un poco desordenadas, pero parece que forman un caminito hacia adelante. Luego, tomas un palo de escoba y tratas de ponerlo en el piso de modo que pase lo más cerca posible de todas las canicas al mismo tiempo.

- Las **canicas sueltas** son tus **datos reales**. En la vida real, los datos tienen un poco de "ruido" y no son perfectos.
- El **palo de escoba** recto es la **Regresión Lineal** (la predicción de la IA).

Para dibujar esto, necesitamos enseñarle a nuestro pintor un truco nuevo.

## Anatomía de la Gráfica

```python
plt.scatter(preguntas, respuestas_reales)
```
- **`scatter`**: Significa "esparcir". A diferencia de `plot` (que une los puntos con una línea), `scatter` solo dibuja puntos sueltos en el lienzo. ¡Estas son nuestras canicas (los datos reales)!

```python
plt.plot(preguntas, respuestas_de_la_ia)
```
- **`plot`**: Aquí usamos nuestro truco conocido. Dibuja una línea continua. ¡Este es el palo de escoba!

## ¿Qué pasa si me equivoco?

### El error de confundir la realidad con la predicción
**El error:** 
Al dibujar la línea de la IA, le entregas las respuestas reales en lugar de las predicciones:
```python
plt.plot(preguntas, respuestas_reales) # ¡MAL!
```
La terminal no te dará un error rojo, pero cuando se abra la gráfica, verás que la línea sube, baja y hace picos extraños uniendo los puntos reales, en lugar de ser una línea recta perfecta.

**¿Por qué?** Porque `plot` simplemente une los puntos que le das. Si le das los datos reales, unirá el desorden de la vida real. La gracia de la Regresión Lineal es que la línea debe ser la idea perfecta y simplificada (la predicción) que hizo la máquina.
**La solución:** A `plt.scatter` le pasas las `respuestas_reales`. Pero a `plt.plot` (la línea), le tienes que pasar las `predicciones` que calculó el modelo con `.predict()`.
