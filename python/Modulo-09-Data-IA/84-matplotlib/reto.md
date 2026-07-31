# Reto 84: El Crecimiento del Cachorro

Acabas de adoptar un perrito y eres muy ordenado. Durante 4 meses has anotado su peso para asegurarte de que está creciendo sano y fuerte. Quieres ver una gráfica para emocionarte con su crecimiento.

### Pasos a seguir:
1. Trae a tu pintor `matplotlib.pyplot` y ponle el apodo `plt`.
2. Crea una variable llamada `meses` que sea una lista con los textos: `"Enero"`, `"Febrero"`, `"Marzo"`, `"Abril"`.
3. Crea otra variable llamada `pesos` que sea una lista con los números: `2`, `4`, `7`, `11`.
4. Pídele a `plt` que trace (`plot`) la gráfica usando los `meses` como base y los `pesos` como altura.
5. Pídele a `plt` que muestre (`show`) la gráfica en la pantalla.

### Reglas estrictas:
- **PERMITIDO:** `import matplotlib.pyplot as plt`, crear listas `[]`, usar `plt.plot()`, `plt.show()`.
- **PROHIBIDO:** Usar Numpy o Pandas (hoy solo usaremos listas simples para mantenerlo fácil). Olvidar el `show()`.

### Resultado esperado en la terminal:
La terminal no imprimirá texto, pero tu computadora debe abrir una ventana blanca mostrando una línea ascendente que va desde el 2 en Enero hasta el 11 en Abril. El programa debe quedarse "pausado" hasta que cierres esa ventana manualmente.
