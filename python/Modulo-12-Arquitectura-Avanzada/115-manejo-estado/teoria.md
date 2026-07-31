# El Pez Dorado y El Elefante

Cuando usamos `client.listen(on_payload=mi_funcion)`, Nerve ejecuta tu función cada vez que llega un mensaje. 

Si dentro de esa función creas una variable (ej. `contador = 0`), esa variable nace y muere **dentro** de ese mensaje. Es como un Pez Dorado: recibe el mensaje, cuenta, y un milisegundo después se le olvida.

Para tener un Elefante (un sistema con memoria o "Manejo de Estado"), la memoria debe vivir **afuera** de la función, para que no se destruya cuando el mensaje termina de procesarse.

### Anatomía del Estado (El Diccionario)

La forma más sencilla y dolorosamente simple de manejar el estado sin crear código complejo, es usar un **Diccionario** global. Una caja fuerte que vive fuera de la función, pero que la función puede leer y modificar.

```python
# NUESTRO ESTADO (La memoria vive afuera, a salvo)
estado = {
    "total_dinero": 0
}

def procesar_mensaje(payload):
    # La función lee y modifica el estado
    estado["total_dinero"] = estado["total_dinero"] + payload["pago"]
```

Desarmemos los símbolos:
- `estado = {}`: Creamos un diccionario. Elegimos un diccionario porque podemos guardar muchas "etiquetas" (dinero, nombre, nivel) dentro de una sola caja.
- `"total_dinero": 0`: El valor inicial. Es como poner la caja registradora en cero al empezar el día.
- `estado["total_dinero"] = ...`: Cuando llega un mensaje, abrimos la caja fuerte `estado`, miramos la etiqueta `"total_dinero"`, le sumamos el valor nuevo y lo volvemos a guardar.

---

### ¿Qué pasa si me equivoco?

**Error Clásico #1: Amnesia inducida por mala indentación**

Si pones el diccionario **adentro** de la función:
```python
def procesar_mensaje(payload):
    estado = {"total_dinero": 0}  # <--- ¡ERROR TERRIBLE!
    estado["total_dinero"] = estado["total_dinero"] + payload["pago"]
```
**Consecuencia:** Cada vez que llegue un mensaje (incluso si es el mensaje número mil), Python creará un diccionario *nuevo* desde cero con el valor `0`, le sumará el pago, y luego lo tirará a la basura al terminar la función. Tu dinero total siempre será igual al último pago, nunca se acumulará.
**Solución:** Mueve la creación de `estado = {...}` completamente afuera y arriba de la función.

**Error Clásico #2: Asumir que el estado se guarda si se apaga el PC**

**Consecuencia:** Este "Estado" vive en la Memoria RAM de la computadora. Si detienes tu programa de Python o se va la luz, el elefante muere y la memoria vuelve a cero.
**Solución:** En sistemas de verdad, este estado eventualmente se guarda en una Base de Datos (tema para otro módulo). Por ahora, debes saber que tu memoria dura exactamente lo que dure tu programa abierto.
