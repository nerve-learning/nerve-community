# Teoría: Padres, Hijos y Botones Universales 👨‍👦

## 1. Herencia (Compartir el ADN)

Imagina un árbol genealógico. Un hijo hereda los apellidos y quizás el color de ojos de sus padres sin tener que hacer ningún esfuerzo. 

En Python, podemos decirle a una Clase que "herede" de otra. La clase hija obtendrá todas las variables del `__init__` y todas las funciones de la clase padre automáticamente.

### Anatomía de la Herencia:
Para heredar, ponemos el nombre de la clase padre **entre paréntesis** al crear la clase hija:

```python
class Animal:
    # ... código del padre ...

class Perro(Animal):
    # ¡El Perro ya sabe hacer todo lo que hace el Animal!
```
Fíjate bien: los paréntesis aquí **no** son para crear el objeto. Al estar pegados a la palabra `class`, significan "yo heredo de...".

## 2. Polimorfismo (Mismo Botón, Diferente Resultado)

Imagina el botón "Play" (▶) de un control remoto. 
- Si aprietas "Play" en un reproductor de DVD, sale un **video**.
- Si aprietas "Play" en un reproductor de CD, sale **música**.
El *botón* es el mismo, pero el *comportamiento* cambia dependiendo de a quién se lo aprietes.

Eso es el **Polimorfismo** (Poli = muchos, Morfos = formas). En código, significa que podemos tener una misma función en diferentes clases, y cada clase hace lo que le corresponde.

### Anatomía de Sobrescribir (Aplastar):
Si el padre `Animal` tiene una función `hablar()` que dice "Mmm...", el hijo `Perro` puede crear su propia función `hablar()`. Al hacerlo, la función del hijo **aplasta** (sobrescribe) a la del padre. 

---

## 🚨 ¿Qué pasa si me equivoco?

Aquí tienes las trampas donde suelen caer los bebés programadores en este nivel:

**1. Confundir los paréntesis de Clase con los de Objeto:**
Al definir la clase es `class Perro(Animal):`. 
Pero al crear el perro de verdad es `mi_perro = Perro("Boby")`.
*¡No intentes meter el nombre ("Boby") en la definición de la clase!*

**2. Creer que tienes que reescribir el `__init__`:**
Si tu clase padre ya tiene un `__init__` que pide el nombre, ¡la clase hija lo hereda! No hace falta que escribas un `__init__` nuevo en el hijo, a menos que quieras agregarle datos extra (pero eso es magia avanzada para otro día). Simplemente, cuando crees el hijo, pásale el nombre en los paréntesis y el `__init__` del padre se encargará del resto.
