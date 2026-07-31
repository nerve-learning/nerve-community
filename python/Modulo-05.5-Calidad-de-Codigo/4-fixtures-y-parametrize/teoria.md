# Teoría: Superpoderes para tus Tests 🦸‍♂️

Para usar Fixtures y Parametrize, necesitamos usar una herramienta nueva de Python: el **Decorador** (el símbolo `@`). 

## El símbolo `@` (El Decorador) y la palabra `import`

En Python, cuando pones un símbolo `@` (arroba) justo arriba de un `def`, le estás pegando un "sticker mágico" a esa función. 

```python
@superpoder
def mi_funcion():
    pass
```
El `@` le dice a Python: "Envuélvela con un comportamiento especial". Hoy usaremos dos superpoderes que vienen de una fábrica externa llamada `pytest`.

Para traer herramientas de otras fábricas, usamos la palabra `import`.
Escribir `import pytest` al inicio de tu archivo significa: "Python, ve y tráeme la caja de herramientas de pytest para poder usar sus superpoderes".

---

## 1. Fixtures: Tus Ayudantes Preparadores

Un **Fixture** es una función que "fabrica" algo que tus tests necesitan. Se crea poniéndole el superpoder `@pytest.fixture` arriba.

```python
import pytest

# 1. Creamos el ayudante (Fixture)
@pytest.fixture
def carrito_compras():
    # Fabrica un carrito con 2 productos listos para usar
    return ["manzana", "leche"]

# 2. El test PIDE al ayudante por su nombre (adentro de sus paréntesis)
def test_carrito_tiene_dos_cosas(carrito_compras):
    assert len(carrito_compras) == 2
```
Fíjate en el truco: ¡el test recibe `carrito_compras` como un parámetro! Pytest es inteligente: ve que el test pide eso, busca el fixture con ese nombre, lo ejecuta en secreto, y le pasa el resultado (la lista) al test. ¡Tú no tuviste que crear la lista adentro del test!

---

## 2. Parametrize: El Repetidor Automático

Imagina que quieres probar que multiplicar un número por cero siempre da cero. En lugar de hacer un test para el 5, otro para el 10, y otro para el 99, usamos el superpoder `@pytest.mark.parametrize`.

```python
import pytest

# El decorador dice: "El parámetro se llamará 'numero'. 
# Repite este test usando los valores 5, 10 y 99 de la lista".
@pytest.mark.parametrize("numero", [5, 10, 99])
def test_multiplicar_por_cero(numero):
    resultado = numero * 0
    assert resultado == 0
```
Pytest ejecutará el mismo test **tres veces automáticamente**, una por cada número.

---

## ¿Qué pasa si me equivoco?

**La trampa del parámetro mal escrito**

Si en el decorador escribes `@pytest.mark.parametrize("num", ...)` pero luego en el `def` pones `def test_algo(n):`, ¡pytest explotará!
Te dirá `fixture 'n' not found`. ¿Por qué? Porque intentará buscar un parámetro que se llame `n` y solo sabe entregar uno que se llame `num`. 
**Solución:** El nombre entre las comillas del parametrize DEBE ser exactamente igual al nombre del parámetro en el `def`.
