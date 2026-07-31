# Teoría: Moldes y Galletas 🍪

La mejor forma de entender la Programación Orientada a Objetos es pensar en una fábrica de galletas.

1. **La Clase (El Molde):** Es el plano o el cortador de metal. El molde en sí no se puede comer, no tiene sabor. Solo dicta la *forma* que tendrán las galletas. En código, una "clase" agrupa qué datos y acciones tendrá algo.
2. **El Objeto (La Galleta):** Es lo que sale cuando usas el molde y le agregas masa, chispas de chocolate y lo metes al horno. El objeto es real, ocupa espacio y puedes interactuar con él.

Puedes usar **un solo molde (Clase)** para crear **cientos de galletas distintas (Objetos)**. 

---

## 🧬 Anatomía de una Clase

Vamos a desarmar los símbolos y palabras nuevas que usaremos para crear nuestro molde.

### 1. La palabra `class`
Así como usamos `def` para crear funciones, usamos `class` para crear un molde nuevo. Por regla general (una costumbre de los programadores), los nombres de las clases siempre empiezan con **Mayúscula**.

```python
class Galleta:
```

### 2. El método constructor: `def __init__(self):`
Cuando sacas una galleta del horno, quizás quieras ponerle un glaseado de inmediato. En Python, usamos una función especial llamada `__init__` (viene de "initialize" o "preparar"). 
**Importante:** Lleva **dos** guiones bajos antes y **dos** guiones bajos después. 
Es lo primerísimo que Python hace automáticamente cuando creas un objeto nuevo a partir del molde.

### 3. La palabra mágica: `self`
Si tienes 5 galletas en la mesa y le dices a una "cambia tu sabor a fresa", ¿cómo sabe cuál de las 5 es la que debe cambiar? 
La palabra `self` significa "yo mismo" en inglés. Es como una etiqueta con el nombre que cada galleta lleva pegada en el pecho. 
Al usar `self.sabor`, le estamos diciendo al objeto: *"guarda este sabor dentro de TI MISMO, no se lo pongas a las otras galletas"*.

**Siempre** debes poner `self` como el primer parámetro dentro de los paréntesis del `__init__` y de cualquier función que esté dentro de tu clase.

### 4. Instanciación: Usar el molde
Para crear un objeto (la galleta real) usamos el nombre de la clase seguido de paréntesis `()`. Los paréntesis le dicen a Python: "¡Oye, ejecuta el `__init__` de este molde para construir el objeto!".

```python
mi_postre = Galleta() 
```

---

## 🚨 ¿Qué pasa si me equivoco?

El camino del bebé programador está lleno de tropiezos. Aquí están los más comunes hoy:

**1. Olvidar poner `self` en los parámetros:**
Si escribes `def __init__(sabor):` (sin el `self`), Python se volverá loco cuando intentes crear el objeto y la terminal gritará:
> `TypeError: __init__() takes 1 positional argument but 2 were given`
*Solución:* ¡Siempre pon `self` de primero! `def __init__(self, sabor):`

**2. Olvidar los paréntesis al crear el objeto:**
Si escribes `mi_galleta = Galleta` (sin los `()`), no estás creando una galleta. Estás guardando el *molde* en otra variable. Si luego intentas hacer un `print(mi_galleta)`, verás algo feo como:
> `<class '__main__.Galleta'>`
*Solución:* Recuerda siempre los paréntesis que "encienden la fábrica": `mi_galleta = Galleta()`.
