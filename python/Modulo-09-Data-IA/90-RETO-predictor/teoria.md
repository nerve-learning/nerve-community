# Teoría: El Ciclo de Vida de la IA

Para construir un "Predictor", no empezamos programando a lo loco. Seguimos una receta de cocina muy estricta de 4 pasos. Piensa en esto como preparar un pastel:

1. **Recolectar los ingredientes (Datos)**: Necesitamos información del pasado. A la IA se le enseña con ejemplos. (Ejemplo: Horas estudiadas y la calificación obtenida).
2. **Limpiar los ingredientes (Limpieza)**: A veces los datos vienen sucios (faltan valores o hay errores). Hay que limpiarlos para que el modelo no se "indigeste".
3. **Hornear el pastel (Entrenamiento)**: Le pasamos los datos limpios a un algoritmo de `scikit-learn` usando la función `.fit()`. Aquí es donde la computadora hace sus cálculos matemáticos y "aprende" los patrones ocultos.
4. **Probar el pastel (Predicción)**: Le damos datos nuevos (que nunca ha visto en su vida) y usamos `.predict()` para que adivine el resultado.

## ¿Qué pasa si me equivoco?

**Error común**: Intentar predecir pasándole al modelo un dato con diferente forma al que usaste para entrenar.
*Síntoma*: La consola explota con un error parecido a `ValueError: Expected 2D array, got 1D array instead`.
*Solución*: Recuerda que `scikit-learn` siempre espera "listas dentro de listas" para las características, ¡incluso si es un solo número! Usa `[[dato]]` en lugar de `[dato]`.
