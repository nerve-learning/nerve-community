# Teoría: El Inspector Automático 🕵️‍♂️

Probar código con `print()` es como pesar ingredientes "a ojo" de buen cubero. Funciona para cocinar en casa, pero en una panadería profesional necesitas una báscula precisa.

**pytest** es tu báscula. Es una herramienta externa (un programa extra que usamos) que ejecuta un código especial llamado **tests** (pruebas). 

## La magia del `assert` (Exigir)

Para escribir un test en Python, usamos una palabra nueva: `assert`. 
En español, `assert` significa "afirmar" o "exigir". Cuando la usas, le estás diciendo a Python: **"Exijo que esto sea verdad. Si es mentira, ¡detén todo y lanza una alarma roja!"**.

```python
def sumar(a: int, b: int) -> int:
    return a + b

# Esto es una función de prueba (un test)
def test_sumar_numeros():
    resultado = sumar(2, 3)
    assert resultado == 5  # "Exijo que resultado sea exactamente 5"
```

### Anatomía de un Test

1. **El nombre de la función:** DEBE empezar con `test_`. Si se llama `probar_suma()`, pytest se pondrá una venda en los ojos y la ignorará por completo.
2. **La acción:** Ejecutar la función real que queremos probar y guardar su resultado.
3. **La exigencia (`assert`):** Comparamos lo que nos dio la función con lo que esperábamos usando el doble igual (`==`). 

---

## ¿Qué pasa si me equivoco?

**El error más común: olvidar el `test_`**

```python
# pytest NUNCA ejecutará esto, porque no empieza con "test_"
def verificar_resta():
    assert 5 - 2 == 3
```
Siempre, siempre llama a tus pruebas empezando con `test_`.

**El segundo "error" (que en realidad es un éxito): El test falla**

Si el `assert` detecta que la afirmación es falsa, pytest te mostrará un mensaje rojo gigante en la terminal llamado `AssertionError`.
¡No te asustes! Si un test se pone rojo, significa que **el test hizo bien su trabajo**. Detectó que tu código tiene un error, ¡antes de que ese código llegara a un cliente! Tu trabajo ahora es ir a tu código real y arreglarlo para que el test se ponga verde (exitoso).
