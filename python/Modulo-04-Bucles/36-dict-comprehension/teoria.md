# Teoría: La Máquina de Cajones

La comprensión de diccionarios funciona casi exactamente igual que la comprensión de listas. La única diferencia es que estamos construyendo un diccionario, así que necesitamos dos cosas nuevas: **las llaves `{}`** y **los dos puntos `:`** para separar el nombre del cajón y lo que va adentro.

## Anatomía de un Dict Comprehension

Fórmula: `{LLAVE : VALOR for VARIABLE in LISTA}`

```python
invitados = ["Ana", "Luis"]

# ¡Magia en una línea!
asistencia = {nombre: "Confirmado" for nombre in invitados}
```

Desmontemos este nuevo hechizo:

- `{` y `}` : En lugar de corchetes, usamos llaves. Le dicen a la computadora: "Prepárate, vamos a construir un diccionario con cajones y etiquetas".
- `nombre: "Confirmado"` : Esta es **La Acción**, pero dividida en dos. 
  - La parte izquierda (`nombre`) es la **etiqueta** del cajón (la llave).
  - Los dos puntos (`:`) separan la etiqueta del contenido.
  - La parte derecha (`"Confirmado"`) es el **contenido** (el valor) que meteremos en ese cajón.
- `for nombre in invitados` : Es nuestro **Motor**. Saca a "Ana" de la lista de invitados, crea el cajón "Ana" y le mete "Confirmado". Luego hace lo mismo con "Luis".

**Cómo lo lee un humano:**
"Crea un cajón con la etiqueta `nombre` y el valor `'Confirmado'`, por cada `nombre` que haya en la lista `invitados`".

## ¿Qué pasa si me equivoco?

El error más común es olvidar los dos puntos `:` o seguir usando los corchetes `[]` por costumbre.

**¿Cómo se ve el error?**
`SyntaxError: invalid syntax` o terminas creando algo que no es un diccionario.

**¿Por qué pasa?**
Si escribes `{nombre "Confirmado" for nombre in invitados}`, la computadora se confunde. Sin los dos puntos, no sabe qué palabra es la etiqueta del cajón y cuál es el contenido. Si usas corchetes `[]`, la computadora intentará hacer una lista y los dos puntos `:` le darán un error.

**¿Cómo lo soluciono?**
Revisa siempre el inicio de tu código. Si usas llaves `{`, DEBE haber unos dos puntos `:` separando tu llave de tu valor antes de escribir la palabra `for`.
