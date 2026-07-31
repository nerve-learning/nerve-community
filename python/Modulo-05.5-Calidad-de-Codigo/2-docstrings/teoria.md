# Teoría: El Manual de Instrucciones 📖

¿Alguna vez compraste algo sin manual? Un control remoto con 40 botones y cero explicaciones. Para entender para qué sirve cada botón, tienes que probarlo todo y rezar para no romper nada.

Ahora imagina que el control tiene un pequeño sticker en el reverso: *"Botón rojo: apagar. Botón azul: cambiar fuente. Botón amarillo: temporizador. Advertencia: no presionar rojo y azul al mismo tiempo o se reinicia."*

Eso es un **Docstring**: el manual de instrucciones que vive **adentro** de tu función.

---

## Anatomía del Docstring

Un docstring es una cadena de texto con comillas triples `"""` que va **inmediatamente después** de la línea `def`, antes del cuerpo de la función.

```python
def calcular_imc(peso: float, altura: float) -> float:
    """
    Calcula el Índice de Masa Corporal (IMC) de una persona.

    El IMC se obtiene dividiendo el peso en kilogramos entre
    el cuadrado de la altura en metros.

    Args:
        peso:   El peso de la persona en kilogramos. Debe ser mayor a 0.
        altura: La altura de la persona en metros. Debe ser mayor a 0.

    Returns:
        El valor del IMC como número decimal, redondeado a 2 decimales.
    """
    return round(peso / (altura * altura), 2)
```

Desmontando el docstring:

- `"""` — Tres comillas dobles abren y tres cierran el texto. Ya las conoces: son para strings que ocupan varias líneas.
- **Primera línea:** Un resumen en una oración. Qué hace la función. Siempre empieza con un verbo: "Calcula...", "Devuelve...", "Verifica...".
- `Args:` — La sección de ingredientes. Aquí listas cada parámetro con su descripción.
- `Returns:` — La sección de producto final. Qué devuelve la función y bajo qué circunstancias.

### La regla mínima: al menos una línea

Si no tienes tiempo para el manual completo, escribe **al menos la primera línea**. Algo es infinitamente mejor que nada:

```python
def saludar(nombre: str) -> str:
    """Devuelve un saludo personalizado con el nombre dado."""
    return "Hola, " + nombre
```

---

## El poder de `help()`

Cuando alguien llama `help(calcular_imc)` en la terminal de Python, ve exactamente el docstring que escribiste. Es como tener un sistema de ayuda integrado en tu función.

```python
help(calcular_imc)
# Muestra:
# Help on function calcular_imc:
# calcular_imc(peso: float, altura: float) -> float
#     Calcula el Índice de Masa Corporal...
```

---

## ¿Qué pasa si me equivoco?

**El error más peligroso: el docstring mentiroso**

```python
def dividir(a: float, b: float) -> float:
    """Suma dos números y devuelve el resultado."""  # ← MENTIRA. Esta función DIVIDE.
    return a / b
```

Un docstring incorrecto es **peor que no tener docstring**. Engaña activamente a quien lee el código. Si cambias lo que hace una función, lo primero que debes actualizar es su docstring.

**El segundo error más común: poner el docstring en el lugar equivocado**

```python
# MAL: el docstring está afuera de la función
"""Calcula el área."""
def calcular_area(base, altura):
    return base * altura

# BIEN: el docstring va ADENTRO, en la primera línea del cuerpo
def calcular_area(base, altura):
    """Calcula el área de un rectángulo dado su base y altura."""
    return base * altura
```

Si el docstring está afuera, Python lo trata como un string suelto (lo ignora) y `help()` no lo mostrará.
