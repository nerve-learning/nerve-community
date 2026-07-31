# Teoría: El Cadenero del Club Nocturno 🕶️

Para entender las Propiedades, imagina la puerta de un Club Nocturno VIP.
Tú, como cliente desde afuera, solo ves una puerta. Caminas hacia ella e intentas entrar. Pero **invisiblemente**, detrás de la puerta, hay un Cadenero (un guardia de seguridad).

Si intentas entrar con zapatillas sucias, el cadenero te detiene. Si cumples las reglas, te deja pasar al interior (donde están las variables privadas).

En Python, creamos estos "cadeneros invisibles" usando el símbolo de la arroba `@`. A esto le llamamos **Decoradores**. Son como sombreros mágicos que le ponemos a una función normal para darle superpoderes.

---

## 🧬 Anatomía de las Propiedades

Necesitamos dos sombreros mágicos para que el truco funcione: el que *lee* los datos y el que *guarda* los datos.

### 1. El sombrero que LEE: `@property`
Convierte una función en una variable "falsa" de solo lectura.
```python
class Club:
    def __init__(self):
        self.__gente_adentro = 50 # Privado

    @property
    def gente(self):
        # Este es el cadenero que te dice cuánta gente hay
        return self.__gente_adentro
```
**Magia:** Afuera de la clase escribes `print(mi_club.gente)`. ¡Sin paréntesis `()`! Python ve el `@property` y ejecuta la función por ti.

### 2. El sombrero que GUARDA: `@nombre.setter`
Nos permite usar el signo igual (`=`) desde afuera, pero validando todo primero.
```python
    @gente.setter
    def gente(self, nueva_cantidad):
        # Este es el cadenero revisando a los que quieren entrar
        if nueva_cantidad > 100:
            print("¡Alto! El club está lleno.")
        else:
            self.__gente_adentro = nueva_cantidad
```
**Magia:** Afuera escribes `mi_club.gente = 150`. Python agarra el `150`, se lo pasa silenciosamente al "setter", el setter hace el `if`, ¡y bloquea el acceso! 

*(Nota importante: La función del `@property` y del `@setter` **deben llamarse exactamente igual**).*

---

## 🚨 ¿Qué pasa si me equivoco?

Aquí es donde los bebés programadores se tropiezan más al usar propiedades:

**1. Ponerle paréntesis a una propiedad:**
Si haces `print(mi_club.gente())`.
> `TypeError: 'int' object is not callable`
*Solución:* El objetivo del `@property` es disfrazar la función para que parezca una variable normal. ¡Quítale los paréntesis `()` cuando la uses desde afuera!

**2. Nombres distintos:**
Si al `@property` lo llamas `def gente(self):` y al setter lo llamas `def cambiar_gente(self, valor):`, Python no entenderá que son pareja. 
*Solución:* Ambas funciones deben tener exactamente el mismo nombre (ej. `def gente`). El gorrito `@gente.setter` es el que los conecta.
