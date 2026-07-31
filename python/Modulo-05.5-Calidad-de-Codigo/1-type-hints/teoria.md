# Teoría: Las Etiquetas de las Cajas 🏷️

Imagina que trabajas en un almacén. Llegan cajas sin etiquetar. Para saber qué contienen, tienes que abrirlas una por una. Una pérdida de tiempo enorme.

Ahora imagina que cada caja lleva una etiqueta: `"Contenido: Vasos de Vidrio | Máximo: 2 kg"`. Cualquier trabajador sabe qué va adentro y cómo manejarla, sin abrirla.

Tus funciones sin **Type Hints** son cajas sin etiqueta. Con Type Hints, cualquiera sabe qué esperar.

---

## Anatomía de los Type Hints

Hay dos lugares donde se ponen etiquetas en una función:

**1. En los parámetros (la entrada de la caja):**
Después del nombre del parámetro, escribe `: Tipo`.

**2. En el `return` (la salida de la función):**
Después del `:` del `def`, antes de los dos puntos del cuerpo, escribe `-> Tipo`.

```python
# ANTES: Sin etiqueta — ¿Qué le meto? ¿Qué me devuelve?
def calcular_descuento(precio, porcentaje):
    return precio - (precio * porcentaje / 100)


# DESPUÉS: Con etiquetas — contrato claro
#     parámetro: Tipo       parámetro: Tipo    -> Tipo de retorno
def calcular_descuento(precio: float, porcentaje: float) -> float:
    return precio - (precio * porcentaje / 100)
```

Desmontando los símbolos nuevos:
- `: float` después de `precio` — la etiqueta que dice "aquí espero un número decimal"
- `-> float` antes de los dos puntos del `def` — la etiqueta que dice "esta función devuelve un número decimal"
- `->` — la flecha. En Python, significa "esta función produce esto". No es matemática, es solo un indicador visual.

**Los tipos más comunes** que ya conoces:

| Tipo en Python | Qué significa |
|---|---|
| `str` | Texto ("hola", "Ana") |
| `int` | Número entero (1, 42, -5) |
| `float` | Número decimal (3.14, 9.99) |
| `bool` | Verdadero o Falso (True, False) |
| `list` | Una lista ([1, 2, 3]) |
| `dict` | Un diccionario ({"clave": "valor"}) |
| `None` | La función no devuelve nada |

```python
# Ejemplo con cada tipo
def saludar(nombre: str) -> str:
    return "Hola, " + nombre

def es_mayor_de_edad(edad: int) -> bool:
    return edad >= 18

def mostrar_menu(opciones: list) -> None:
    for opcion in opciones:
        print(opcion)
    # No hay return — devuelve None (nada)
```

---

## ¿Qué pasa si me equivoco?

**La trampa más importante: Python NO te detiene si ignoras las etiquetas**

```python
def sumar(a: int, b: int) -> int:
    return a + b

sumar("hola", "mundo")   # Python NO lanza un error
# Resultado: "holamundo" — Python concatenó strings en vez de sumar
```

**¿Por qué pasa?**
Los Type Hints son solo *etiquetas de documentación*. Python las lee y las ignora en tiempo de ejecución. No valida que realmente le pases un `int`. Si le pasas un `str`, lo acepta igual y hace lo que pueda con él.

**¿Entonces para qué sirven?**
Sirven para dos cosas muy valiosas:
1. **Para ti y tus compañeros:** Leen la firma de la función y saben qué pasar sin leer el cuerpo.
2. **Para tu editor (VS Code, PyCharm):** Ellos *sí* leen los type hints y te marcan en rojo si pasas el tipo incorrecto, antes de ejecutar. Es como un corrector ortográfico, pero para tipos de datos.
