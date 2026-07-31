# Teoría: Escribiendo Código como un Profesional

Optimizar no siempre significa hacer que el código corra más rápido. Muchas veces significa hacerlo más fácil de leer para los humanos. Menos líneas de código significan menos lugares donde los *bugs* (errores) pueden esconderse.

### Regla 1: Aplanar los nidos (Usar `and`)
Un `if` dentro de otro `if` (lógica anidada) forma una "V" visual que empuja el código hacia la derecha. Si solo quieres hacer algo cuando ambas cosas son ciertas, ¡júntalas!

**Novato:**
```python
if tiene_boleto:
    if es_mayor_de_edad:
        print("Puedes entrar al concierto")
```
**Profesional:**
```python
if tiene_boleto and es_mayor_de_edad:
    print("Puedes entrar al concierto")
```

### Regla 2: Asignación Directa de Booleanos
Este es el truco favorito de los programadores. Si estás usando un `if` solo para guardar `True` o `False` en una variable, ¡puedes guardar el resultado de la comparación directamente!

**Novato:**
```python
puntuacion = 85
if puntuacion > 80:
    paso_el_examen = True
else:
    paso_el_examen = False
```
**Profesional:**
```python
puntuacion = 85
paso_el_examen = puntuacion > 80  # Guarda el resultado de la pregunta (True)
```
*Analogía:* En lugar de decir "Si el cielo es azul, entonces es de día, si no, no lo es", dices "Es de día = el cielo es azul".

### Regla 3: El fantasma del `== True`
Recordando lo que vimos en Truthy/Falsy, un `if` ya está buscando un `True`. Preguntar `if variable == True:` es como preguntar "¿Es verdad que es verdad?".

**Novato:**
```python
if paso_el_examen == True:
```
**Profesional:**
```python
if paso_el_examen:
```

---

## ¿Qué pasa si me equivoco?

**1. Sobre-optimizar y perder claridad**
Si intentas juntar 5 condiciones en una sola línea usando muchísimos `and` y `or`, el código será tan elegante que nadie lo entenderá. La optimización busca **claridad**. Si una línea es demasiado larga, a veces es mejor dejarla como estaba.
