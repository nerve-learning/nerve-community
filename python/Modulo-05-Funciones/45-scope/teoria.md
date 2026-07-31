# Teoría: La Regla de Las Vegas 🎰

## 1. Scope Local (Variables Privadas)

Toda variable que tú crees **dentro** de una función (con espacios a la izquierda), está atrapada en esa función.

```python
def guardar_secreto():
    mensaje = "Soy Batman" # Esta variable nace aquí
    print(mensaje)
    # Al llegar aquí, la función termina y la variable 'mensaje' ¡se autodestruye!
```
Si intentas hacer `print(mensaje)` afuera de la función, Python te dirá que esa variable no existe.

## 2. Scope Global (Variables Públicas)

Si creas una variable **totalmente pegada al margen izquierdo** (fuera de los `def`), es una variable Global. Todas las funciones pueden "leerla".

```python
clima = "Soleado" # Variable Global

def mirar_por_la_ventana():
    # La función puede leer 'clima' sin problemas
    print("El clima de hoy es", clima) 
```

## 3. El gran problema: Modificar una variable Global

Python es muy protector. Te deja *leer* las variables globales desde adentro de una función, pero **no te deja modificarlas** directamente. Si intentas modificarlas, Python se confunde y cree que quieres crear una variable local nueva con el mismo nombre.

Para modificar una variable global desde adentro de una habitación (función), tienes que gritar la palabra mágica **`global`**.

```python
puntuacion = 0 # Global

def ganar_puntos():
    global puntuacion # "¡Oye Python! Voy a modificar la variable del pasillo"
    puntuacion = puntuacion + 10
```

---

## 🚨 ¿Qué pasa si me equivoco?

### Error 1: Intentar leer un secreto desde afuera
**El síntoma en la terminal:** `NameError: name 'mensaje' is not defined`
**¿Por qué pasa?** Intentaste imprimir o usar una variable que creaste dentro de un `def`, pero lo hiciste afuera en el pasillo principal. Recuerda: ¡las variables locales se autodestruyen cuando la función acaba!

### Error 2: Modificar una global sin pedir permiso
**El síntoma en la terminal:** `UnboundLocalError: local variable 'puntuacion' referenced before assignment`
**¿Por qué pasa?** Hiciste algo como `puntuacion = puntuacion + 10` dentro de un `def`, pero olvidaste escribir la línea `global puntuacion` antes. Python intentó crear una variable local llamada "puntuacion", pero al mismo tiempo intentó sumarle 10 a algo que (en su mente local) aún no existía. ¡Usa `global` si quieres alterar la variable de afuera!
