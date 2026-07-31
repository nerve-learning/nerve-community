# Teoría: La Máquina Expendedora 🥤

La mejor forma de entender el encapsulamiento es ver una **Máquina Expendedora**. 

- **Lo Privado (Las tripas):** Adentro de la máquina están las latas de refresco y la caja con las monedas. Tú no puedes (ni debes) meter la mano directamente para sacar una lata o cambiar los precios. Eso está **encapsulado** (oculto y protegido) tras un cristal.
- **Lo Público (Los botones):** La única forma de interactuar con la máquina es a través de sus métodos públicos: insertar una moneda por la ranura y presionar el botón de la bebida. 

En programación, hacemos lo mismo. Hacemos que las variables importantes sean privadas (las ocultamos tras el cristal), y creamos funciones públicas (botones) para que el resto del programa interactúe con ellas de forma segura.

---

## 🧬 Anatomía de la Privacidad en Python

Python usa un truco visual para esconder variables. Si le pones **dos guiones bajos (`__`) al principio del nombre de la variable**, Python le pone un candado invisible.

```python
class MaquinaExpendedora:
    def __init__(self):
        # Variable PÚBLICA (cualquiera puede verla y cambiarla)
        self.color = "Roja"
        
        # Variable PRIVADA (oculta tras el cristal)
        self.__dinero_recaudado = 0
```

Si intentas hacer algo con `self.__dinero_recaudado` **desde adentro** de cualquier función de la misma clase, funcionará perfecto.
Pero si alguien desde **afuera** de la clase intenta modificarla o incluso leerla, Python actuará como si esa variable no existiera.

---

## 🚨 ¿Qué pasa si me equivoco?

El error más común aquí es la curiosidad de intentar tocar lo intocable.

**Intentar acceder a una variable privada desde afuera:**
```python
mi_maquina = MaquinaExpendedora()
print(mi_maquina.__dinero_recaudado)
```
Si haces esto, la terminal te gritará con letras rojas un error muy específico:
> `AttributeError: 'MaquinaExpendedora' object has no attribute '__dinero_recaudado'`

Fíjate lo inteligente que es Python: no te dice "¡Acceso denegado!". Simplemente te miente y dice: *"Oye, este objeto no tiene ningún atributo con ese nombre"*. Protege el secreto fingiendo que no existe. 

*Solución:* Nunca intentes leer o escribir variables con `__` desde afuera de la clase. Crea una función normal (un "botón") dentro de la clase para que te diga cuánto dinero hay.
