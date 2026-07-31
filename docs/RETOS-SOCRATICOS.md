# Filosofía de los Retos Socráticos

En Nerve Community usamos un enfoque metodológico llamado **Aprendizaje Socrático**. A diferencia de los tutoriales tradicionales donde se te dice "escribe esto línea por línea", aquí el proceso es distinto: se te presenta un problema y tú debes deducir la solución investigando, probando y leyendo el código que te evalúa.

---

## Qué es un Reto Socrático

Un Reto Socrático es un problema técnico planteado de forma que **tú** debes encontrar la respuesta. No hay una respuesta directa en el enunciado. En cambio, hay:

- Un archivo `reto.md` que describe el problema en lenguaje natural.
- Un archivo de pruebas (`test_main.py`) que describe exactamente qué debe hacer tu código.
- Un archivo vacío o incompleto donde escribes tu solución.

El archivo de pruebas es el requisito funcional. Si el test espera que tu función devuelva un diccionario con ciertas llaves, eso es lo que tu código debe hacer.

---

## Principios de evaluación

**El test es tu guía, no el enunciado.**
La forma más eficiente de entender un reto es leer el archivo de pruebas antes de leer el enunciado. El test describe con precisión qué entradas recibe tu función y qué debe devolver.

**El error es información.**
Un error en la terminal no es una señal de que fallaste. Es la descripción exacta de qué salió mal. Leer el mensaje de error completo, incluyendo el stack trace, te dice en qué línea falló, qué recibió tu función y qué esperaba recibir.

**La reflexión activa consolida el conocimiento.**
Rompe el código a propósito: cambia un valor, quita un `return`, modifica el tipo de dato que devuelves. Corre los tests después de cada cambio. Observar cómo reacciona el sistema ante cada modificación es una de las formas más efectivas de aprender.

**La búsqueda es parte del trabajo.**
Si no sabes cómo hacer algo, busca en la documentación oficial de Python, en Stack Overflow, o usa herramientas de IA. Lo importante es que entiendas lo que estás copiando. El objetivo no es que el test pase, sino que puedas explicar por qué pasó.

---

## Cómo leer un error de pytest

Cuando ejecutas `pytest test_main.py` y hay un fallo, la salida tiene esta estructura:

```
FAILED test_main.py::test_suma - AssertionError: assert 0 == 5
```

Cada parte te dice algo útil:

- `FAILED` — el test no pasó.
- `test_main.py::test_suma` — el nombre del archivo y la función de test que falló.
- `AssertionError: assert 0 == 5` — tu función devolvió `0`, pero el test esperaba `5`.

Un ejemplo más completo:

```
def test_suma():
    resultado = suma(2, 3)
>   assert resultado == 5
E   AssertionError: assert 0 == 5

test_main.py:6: AssertionError
```

La línea con `>` muestra exactamente qué instrucción falló. La línea con `E` muestra los valores reales. El número al final (`test_main.py:6`) es la línea del test donde ocurrió el fallo.

Con esa información puedes ir directamente a tu código y preguntar: ¿por qué `suma(2, 3)` está devolviendo `0`?

---

## Errores comunes al enfrentar un reto

**No leer el archivo de pruebas antes de empezar.**
El test es el requisito. Leerlo primero te ahorra tiempo de intentar cosas que el test no pide.

**Ignorar el mensaje de error.**
El mensaje de error contiene la respuesta a qué falla. Leerlo completo, incluyendo el stack trace, es el primer paso antes de cambiar cualquier línea de código.

**Cambiar varias cosas al mismo tiempo.**
Si cambias cinco cosas y los tests pasan, no sabes cuál de los cinco cambios fue el correcto. Cambia una cosa, corre los tests, evalúa el resultado.

**Buscar la solución completa antes de intentar.**
El aprendizaje ocurre en el proceso de resolver, no en tener el resultado. Intenta primero. Busca ayuda cuando hayas agotado tus hipótesis, no cuando el reto se vea difícil.

---

## Qué se valida cuando entregas

Cuando haces push a tu repositorio, el CI automático corre:

- Los mismos tests que tienes en local (`pytest`).
- El formateador de estilo (`black`).

Si ambos pasan, el check verde en tu commit indica que tu solución es correcta y el siguiente módulo queda disponible.

Cuando resuelves un reto socrático, demuestras haber entendido un concepto técnico con suficiente profundidad como para aplicarlo correctamente ante condiciones que no conocías de antemano.

---

← [Volver a Cómo usar como Alumno](COMO-USAR-COMO-ALUMNO.md) | [Volver al repositorio](../README.md)
