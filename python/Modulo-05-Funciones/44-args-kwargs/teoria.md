# Teoría: Rompiendo las Reglas de la Cantidad 📦

## 1. Llamar por nombre (Keyword Arguments)

Recuerda que Python asigna los valores de izquierda a derecha. Pero, si al llamar a la función le dices **exactamente el nombre de la etiqueta**, a Python ya no le importa el orden.

```python
def registrar(nombre, pais="Desconocido", plan="Gratis"):
    print(nombre, pais, plan)

# Nos saltamos el país y cambiamos solo el plan llamándolo por su etiqueta:
registrar("Carlos", plan="Premium") 
```

## 2. El Asterisco Simple `*` (La caja sin fondo: args)

Si pones un `*` antes de un parámetro al definir tu función, le dices a Python: *"Agarra todos los valores sueltos extra que me envíen, y mételos en una **Tupla** (una lista que no se puede modificar)"*.
Por convención entre programadores, a esa caja le llamamos `args` (de argumentos).

```python
def hacer_jugo(*args):
    # 'args' ahora es una tupla con todas las frutas que manden
    for fruta in args:
        print("Licuando:", fruta)

hacer_jugo("Manzana", "Pera", "Mango") # ¡3 valores a una sola variable!
```

## 3. El Asterisco Doble `**` (El archivero de etiquetas: kwargs)

Si pones `**` antes de un parámetro, le dices a Python: *"Agarra todos los valores **que traigan su propia etiqueta** (Keyword Arguments) extra, y mételos en un **Diccionario**"*.
Por convención, le llamamos `kwargs` (Keyword Arguments).

```python
def mostrar_datos(**kwargs):
    # 'kwargs' ahora es un diccionario
    for etiqueta in kwargs:
        print(etiqueta, "->", kwargs[etiqueta])

mostrar_datos(edad=25, ciudad="Madrid", profesion="Hacker") 
```

## 🧬 La Regla del Orden Supremo

Si vas a usar todo junto, los paréntesis de tu `def` DEBEN seguir este orden estricto:
`def funcion(obligatorios, *args, **kwargs):`

---

## 🚨 ¿Qué pasa si me equivoco?

### Error 1: Positional argument follows keyword argument
**El síntoma en la terminal:** `SyntaxError: positional argument follows keyword argument`
**¿Por qué pasa?** Ocurre al **llamar** a la función. Si le pones etiqueta a un dato (ej. `edad=25`), TODOS los datos que pongas después hacia la derecha también deben tener etiqueta. 
**❌ Mal:** `mostrar_datos(edad=25, "Madrid")`
**✅ Bien:** `mostrar_datos(25, ciudad="Madrid")`

### Error 2: Olvidar los asteriscos al definir
**El síntoma en la terminal:** `TypeError: hacer_jugo() takes 1 positional argument but 3 were given`
**¿Por qué pasa?** Si escribes `def hacer_jugo(args):` (sin el `*`), Python cree que `args` es un parámetro normal que solo puede guardar 1 sola cosa. ¡El que hace la magia de atrapar valores infinitos es el símbolo `*`, no la palabra "args"!
