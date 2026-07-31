# Teoría: El Pintor de Gráficas

Matplotlib es una herramienta gigante, pero nosotros solo necesitamos al pintor principal, que vive en un departamento llamado `pyplot`. Como su nombre es muy largo, todo el mundo en programación le dice simplemente `plt`.

## Anatomía del Pintor

```python
import matplotlib.pyplot as plt
```
- **`import matplotlib.pyplot`**: De la gran caja `matplotlib`, saca al pintor `pyplot`.
- **`as plt`**: "Y desde ahora, te llamaremos `plt`".

Para pintar una gráfica de líneas, el pintor necesita dos cosas: 
1. La lista de cosas que van en el suelo (Eje X, horizontal).
2. La lista de alturas de cada cosa (Eje Y, vertical).

```python
plt.plot(x, y)
```
- **`plt.`**: Llamamos a nuestro pintor.
- **`plot`**: Significa "trazar". Aquí el pintor agarra su lápiz, pone puntos en el lienzo y los une con una línea.
- **`(x, y)`**: Le entregamos las listas de posiciones.

**¡OJO!** Aquí viene la parte más importante. El pintor trabaja encerrado en un cuarto oscuro. Cuando hace `plt.plot()`, pinta el cuadro, pero tú no lo puedes ver todavía. Para revelar la obra al público, debes correr la cortina:

```python
plt.show()
```
- **`show()`**: Significa "mostrar". Abre una ventana en tu computadora y te deja ver la gráfica.

## ¿Qué pasa si me equivoco?

### El error más común: Olvidar abrir la cortina
**El error:**
```python
plt.plot(meses, ganancias)
# Se te olvida poner plt.show()
```
La terminal corre, no marca ningún error rojo, pero **no aparece ninguna gráfica** y el programa termina.

**¿Por qué?** Le dijiste al pintor que dibujara, y lo hizo perfectamente en la memoria de la computadora, pero como nunca le dijiste "muéstramelo" (`show`), la computadora simplemente tiró el dibujo a la basura al terminar el programa.
**La solución:** Siempre, SIEMPRE, la última línea de tu código de gráficas debe ser `plt.show()`.
