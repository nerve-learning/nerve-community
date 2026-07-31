# Singleton: Hackeando el Nacimiento 🐣

Hasta ahora conoces a `__init__`. Hemos dicho que `__init__` es quien "construye" al objeto, pero eso era una pequeña mentira piadosa. 

En realidad, `__init__` solo *viste y prepara* al objeto una vez que ya nació. Quien realmente hace nacer al objeto, la "cigüeña" de Python, es el método mágico **`__new__`**.

Para crear un Singleton, vamos a interceptar a la cigüeña (`__new__`) y darle una instrucción clara: *"Si ya trajiste a este bebé antes, no crees uno nuevo. Devuélveme exactamente el mismo que ya me diste."*

## 🧬 Anatomía del Singleton

Necesitamos dos cosas:
1. Una variable guardada en la clase (no en `self`, sino en la clase misma) para recordar si el objeto ya existe.
2. El método `__new__` para controlar el nacimiento.

```python
class Rey:
    # 1. La memoria de la clase. Comienza vacía (None).
    _el_unico_rey = None 

    # 2. Interceptamos el nacimiento con __new__
    def __new__(cls):
        # Preguntamos: ¿La clase ya tiene un rey guardado?
        if cls._el_unico_rey is None:
            # Si no hay, le pedimos a la súper fábrica de Python que lo cree
            cls._el_unico_rey = super().__new__(cls)
        
        # Si ya había uno, o si lo acabamos de crear, devolvemos a EL MISMO.
        return cls._el_unico_rey
```

### Desmontando la magia:
1. `_el_unico_rey = None`: Es una caja fuerte que pertenece a la *fábrica* (la clase), no a los productos. Empieza vacía.
2. `def __new__(cls):`: A diferencia de `__init__` que usa `self` (el objeto creado), `__new__` usa `cls` (la clase misma) porque el objeto ¡aún no existe!
3. `super().__new__(cls)`: Es la instrucción sagrada que llama al creador supremo de Python para que asigne memoria y fabrique físicamente el objeto.

## ⚠️ ¿Qué pasa si me equivoco?

El error más brutal al hacer un Singleton es olvidar el `return cls._el_unico_rey` al final de `__new__`.

**¿Qué pasa si lo olvidas?**
Cuando intentes hacer `mi_rey = Rey()`, Python intentará nacer al rey, pero como no devolviste nada (`return`), la variable `mi_rey` se quedará valiendo `None`. 
Y cuando intentes hacer `mi_rey.saludar()`, la terminal te gritará furiosa:
`AttributeError: 'NoneType' object has no attribute 'saludar'`

¡Recuerda siempre que la cigüeña DEBE entregar (return) al bebé!
