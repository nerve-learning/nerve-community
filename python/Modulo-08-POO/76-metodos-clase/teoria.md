# Teoría: El Letrero de la Fábrica 📈

Imagina una fábrica de coches. 
- Cada coche tiene un **velocímetro**. Ese velocímetro es único para cada coche y le pertenece solo a él (eso es una variable de instancia, guardada en `self`).
- En el techo de la fábrica hay un **letrero gigante** que dice: *"Coches producidos hoy: 50"*. Ese letrero es visible para todos, pero le pertenece a la fábrica, no a un coche en específico. (Eso es una **Variable de Clase**).

Para interactuar con ese letrero gigante, la fábrica necesita un Gerente (un **Método de Clase**). El gerente no arregla coches individuales, el gerente administra la fábrica.

---

## 🧬 Anatomía de la Fábrica

### 1. Variables de Clase
Se escriben **fuera** del `__init__`, directamente debajo de la palabra `class`.
```python
class Fabrica:
    total_coches = 0  # <--- Esto le pertenece al molde, no al objeto
    
    def __init__(self, color):
        self.color = color # <--- Esto le pertenece al coche (objeto)
```

### 2. El Decorador `@classmethod` y la palabra `cls`
Para crear un gerente (un método que actúe sobre la fábrica), usamos el gorrito mágico `@classmethod`.
Además, ya no usamos `self` (porque `self` significa "este objeto específico"). Usamos `cls` (que es la abreviatura de *Class* y significa "esta fábrica").

```python
    @classmethod
    def reporte(cls):
        print(f"El letrero dice: {cls.total_coches} creados.")
```

Para usar este método, no necesitas crear un coche. Puedes llamar directamente a la fábrica: `Fabrica.reporte()`.

---

## 🚨 ¿Qué pasa si me equivoco?

El error más común es confundir los roles del empleado (`self`) y el gerente (`cls`).

**Usar `self` dentro de un Método de Clase:**
```python
@classmethod
def reporte(self):
    print(self.color)
```
Si haces esto, Python te gritará con un `AttributeError: type object 'Fabrica' has no attribute 'color'`. 
*Razón:* Estás intentando leer el color de un coche, ¡pero estás hablando con la fábrica! La fábrica no tiene color, los coches sí. En un `@classmethod`, solo puedes usar `cls` para acceder a cosas de la fábrica (variables de clase).
