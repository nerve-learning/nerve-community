# Reto 86: El Puesto de Limonadas

Eres dueño de un puesto de limonadas. Has anotado la temperatura que hacía y cuántos vasos vendiste. Quieres enseñarle esto a una IA y luego ver gráficamente si la IA logró trazar una buena línea de predicción.

Tus datos son:
- Temperaturas (grados): `[[15], [20], [25], [30]]`
- Vasos vendidos reales: `[10, 22, 35, 48]`

### Pasos a seguir:
1. Trae a tu cerebro (`LinearRegression`) y a tu pintor (`matplotlib.pyplot` como `plt`).
2. Crea tus variables para las temperaturas (con dobles corchetes) y los vasos vendidos reales.
3. Crea a tu modelo de IA y entrénalo con `.fit()`.
4. Pídele a la IA que haga `.predict()` sobre tus temperaturas para generar las **predicciones perfectas**. Guárdalas en una variable.
5. Usa `plt.scatter()` para dibujar los puntos sueltos de las temperaturas vs los vasos **reales**.
6. Usa `plt.plot()` para dibujar la línea continua de las temperaturas vs las **predicciones perfectas** de la IA.
7. Abre el telón con `plt.show()`.

### Reglas estrictas:
- **PERMITIDO:** Todo lo usado en el ejemplo (`LinearRegression`, `plt.scatter`, `plt.plot`, `plt.show`, `.fit`, `.predict`).
- **PROHIBIDO:** Pasarle los vasos reales al `plt.plot()`. (Recuerda: ¡la línea necesita las predicciones de la IA!).

### Resultado esperado en la terminal:
La computadora abrirá una ventana blanca. Verás 4 puntos azules sueltos que representan tus ventas reales, y una línea recta (usualmente azul o naranja) que atraviesa esos puntos casi por el centro exacto. El programa se quedará en pausa hasta que cierres la ventana.
