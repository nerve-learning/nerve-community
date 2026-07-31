# Teoría: La Salsa por Defecto 🥫

Hasta ahora usábamos los parámetros como huecos vacíos obligatorios. Hoy vamos a ponerles un "valor de rescate".

## 1. Asignando un Plan B

Cuando **defines** la función, puedes usar el símbolo `=` al lado del parámetro. 
¡Atención! Aquí el `=` no funciona exactamente igual que cuando creas una variable normal. Aquí el `=` significa: *"Si el programador olvida o decide no darme este ingrediente, usa esto en su lugar"*.

```python
def pedir_hamburguesa(salsa="ketchup"):
    print("Preparando hamburguesa con", salsa)
```

Si la llamamos vacía:
```python
pedir_hamburguesa() 
# No le pasamos nada. Python dice: "¡No hay problema! Uso el Plan B: ketchup".
# Salida: Preparando hamburguesa con ketchup
```

Si le pasamos un valor, **destruimos el Plan B**:
```python
pedir_hamburguesa("mayonesa")
# Python dice: "Me diste un valor, así que ignoro el ketchup y uso mayonesa".
# Salida: Preparando hamburguesa con mayonesa
```

## 2. La Regla de Oro del Orden ⚖️

Cuando combinas parámetros obligatorios (los que no tienen `=`) y parámetros opcionales (los que sí tienen `=`), **los obligatorios siempre deben ir PRIMERO de izquierda a derecha**.

**✅ CORRECTO:**
```python
def crear_personaje(nombre, nivel=1, vida=100):
```
*(Primero el obligatorio `nombre`, luego los opcionales `nivel` y `vida`).*

**❌ INCORRECTO:**
```python
def crear_personaje(nivel=1, nombre):
```
*(No puedes poner un opcional antes de uno obligatorio).*

¿Por qué? Porque cuando llamas a la función y pones `crear_personaje("Arthur")`, Python lee de izquierda a derecha. Si pusieras los opcionales primero, Python no sabría si "Arthur" es el nivel, el nombre, o qué. ¡Los obligatorios siempre van al principio de la fila!

---

## 🚨 ¿Qué pasa si me equivoco?

### Error 1: Romper la regla del orden
**El síntoma en la terminal:** `SyntaxError: non-default argument follows default argument`
**¿Por qué pasa?** Como dice el inglés literal: "Un argumento no-por-defecto (obligatorio) está siguiendo a uno por-defecto (opcional)". Python te está regañando porque pusiste un parámetro con `=` antes de uno normal en los paréntesis de tu `def`. ¡Mueve los que tienen `=` al final!

### Error 2: Pasar demasiados argumentos
**El síntoma en la terminal:** `TypeError: pedir_hamburguesa() takes from 0 to 1 positional arguments but 2 were given`
**¿Por qué pasa?** Tu función tenía un parámetro opcional, y al llamarla intentaste pasarle 2 cosas (ej. `pedir_hamburguesa("mayonesa", "mostaza")`). Aunque tenga un Plan B, la caja `salsa` sigue siendo UNA sola caja. No puedes meterle dos cosas si la función no tiene otra variable esperando.
