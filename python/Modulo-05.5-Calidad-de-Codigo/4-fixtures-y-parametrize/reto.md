# Reto 4: La Fábrica de Pruebas 🏭

Tu equipo está creando un carrito de compras online. Te piden que pruebes la función que calcula el total con impuestos. Pero son exigentes: quieren que la pruebes con **varios precios a la vez**, y que uses un **ayudante (Fixture)** para obtener el porcentaje del impuesto, en vez de escribirlo a mano en el test.

## Instrucciones Paso a Paso:

1. Crea el archivo `test_reto_avanzado.py`.
2. En la línea 1, escribe `import pytest` para tener acceso a los superpoderes.
3. Copia la función real que vamos a probar:
```python
def calcular_total(precio: float, impuesto: float) -> float:
    return precio + (precio * impuesto)
```
4. **Crea un Fixture:** 
   Usa `@pytest.fixture` arriba de una función llamada `impuesto_estandar()`. Esta función simplemente debe usar `return` para devolver el número decimal `0.15` (que representa el 15%).
5. **Crea un Test Parametrizado que además usa el Fixture:**
   - Usa `@pytest.mark.parametrize` para probar tres precios distintos en una sola pasada: `100.0`, `50.0`, y `200.0`. Llámale al parámetro `"precio_base"`.
   - Crea el test: `def test_calcular_total(precio_base, impuesto_estandar):`. (¡Mira! El test pide tanto el valor parametrizado como el ayudante al mismo tiempo).
   - Adentro del test, calcula el resultado usando tu función real `calcular_total()` y guárdalo en una variable.
   - Usa `assert` para verificar que el total calculado es **mayor** (`>`) que el `precio_base` original. (Tiene sentido, si le sumas impuestos a algo, siempre cuesta más).
6. Ejecuta `pytest test_reto_avanzado.py` en la terminal de tu editor.

## Reglas Estrictas:
✅ **Conceptos Permitidos:** `import pytest`, `@pytest.fixture`, `@pytest.mark.parametrize`, `def`, `return`, `assert`, operadores matemáticos y lógicos (`>`, `+`, `*`).
❌ **Conceptos Prohibidos:** Usar `print()`. Evita hacer 3 funciones de test; el parametrize debe hacer el trabajo de multiplicar el test.

## Resultado Esperado en tu Terminal:

Al correr el test, verás que aunque escribiste la función `test_calcular_total` una sola vez, pytest ejecuta **tres pruebas** automáticamente (una por cada precio). Debería salir todo en verde, indicando "3 passed".
