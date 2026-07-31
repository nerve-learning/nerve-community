# Teoría: La Primera Estación de Ensamblaje 🏭

Imagina que estás en una fábrica de coches. El método `__init__` es la **primerísima estación** de la línea de ensamblaje. Es obligatorio pasar por ahí. En esa estación le ponen el motor y pintan el coche del color que el cliente pidió. No puedes sacar el coche a la calle sin pasar primero por ahí.

En Python, `__init__` es un **método mágico**. Se llaman "mágicos" porque tú no los llamas directamente (nunca escribes `mi_coche.__init__()`). Python lo ejecuta de forma automática e invisible en el instante en que creas el objeto con los paréntesis: `mi_coche = Coche()`.

---

## 🧬 Anatomía del `__init__`

Vamos a desarmar cómo fluye la información desde que creamos el objeto hasta que se guarda adentro.

```python
class Pizza:
    def __init__(self, ingrediente_elegido):
        self.ingrediente = ingrediente_elegido
        self.horneada = False
```

1. **Los dobles guiones bajos (`__`):** Son dos a la izquierda y dos a la derecha. Le dicen a Python: *"Oye, este método es especial, trátalo diferente a una función normal"*.
2. **El parámetro `ingrediente_elegido`:** Es la variable temporal que recibe el dato desde afuera.
3. **El guardado `self.ingrediente = ...`:** Aquí ocurre la transferencia. Tomamos el dato temporal que vino de afuera y lo pegamos permanentemente en el pecho de la pizza (en su `self`). A partir de ahora, la pizza nunca olvidará de qué sabor es.
4. **Valores por defecto (`self.horneada = False`):** ¡No todo tiene que venir de los parámetros! Podemos definir verdades universales para todos los objetos que nacen. Todas las pizzas nacen crudas (`False`). No hace falta pedírselo al usuario.

---

## 🚨 ¿Qué pasa si me equivoco?

El `__init__` es quisquilloso. Aquí están los tropiezos más comunes:

**1. Escribir mal los guiones bajos:**
Si escribes `def init(self):` o `def _init_(self):` (con un solo guion), Python pensará que es una función normal y corriente. ¡El método mágico no se ejecutará automáticamente! Tu objeto nacerá vacío.
*Solución:* Siempre son **DOS** guiones bajos: `__init__`.

**2. Olvidar pasar los parámetros al crear el objeto:**
Si tu `__init__` exige un ingrediente (`def __init__(self, ingrediente):`) y tú intentas crear la pizza así:
`mi_cena = Pizza()`
La terminal se quejará amargamente:
> `TypeError: __init__() missing 1 required positional argument: 'ingrediente'`
*Solución:* Si el `__init__` pide datos (además de `self`), tienes que enviarlos dentro de los paréntesis al crear el objeto: `mi_cena = Pizza("Pepperoni")`.
