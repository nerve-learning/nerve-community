# Teoría: La Pizarra de la Oficina

Imagina que en tu oficina (tu programa de Python) hay una **pizarra gigante** pegada en la pared. Esa pizarra es tu **Estado Global** (variables creadas fuera de cualquier función).

Tú contrataste a un recepcionista (tu función `listen`) que trabaja en su propio **escritorio** (el espacio de memoria local de la función). 

Si el recepcionista recibe un paquete que dice "Suma 1 punto a la pizarra", él no puede simplemente tachar la pizarra desde su silla. Si lo intenta sin permiso, agarrará una libreta pequeña en su propio escritorio, anotará el "1", y cuando termine su turno, tirará la libreta a la basura. ¡La pizarra grande nunca cambió!

Para que el recepcionista pueda pararse, caminar a la pared y modificar la pizarra grande, necesita un **permiso especial**. Ese permiso es la palabra mágica `global`.

## Anatomía del Estado Global

```python
# 1. LA PIZARRA (Estado Global)
puntos = 0

def recepcionista(datos):
    # 2. EL PERMISO ESPECIAL
    global puntos
    
    # 3. MODIFICANDO LA PIZARRA
    puntos = puntos + 1
    print("Puntos actuales:", puntos)
```

* **`puntos = 0`**: Creamos la variable afuera, en el espacio principal. Vivirá mientras el programa esté encendido.
* **`global puntos`**: Le dice a Python: *"Oye, adentro de esta función no crees una variable nueva llamada puntos. Quiero usar y modificar la que está allá afuera en la pared"*.
* **`puntos = puntos + 1`**: Ahora sí, el cambio se guarda en la memoria permanente del programa.

---

## ¿Qué pasa si me equivoco?

El error más frustrante ocurre cuando olvidas escribir la palabra `global`.

**El Error:**
`UnboundLocalError: local variable 'puntos' referenced before assignment`

**¿Qué significa?**
Python te está diciendo: *"Intentaste sumar 1 a 'puntos', pero en el escritorio de este recepcionista no hay ninguna variable que se llame así, y no me diste permiso (global) para buscarla en la pared"*.

**La Regla de Oro:**
Si tu función de Nerve solo va a **LEER** la variable de afuera (ej. solo imprimirla), no necesitas `global`. Pero si la función va a **MODIFICARLA** (cambiar su valor con `=`), poner `global` es obligatorio.
