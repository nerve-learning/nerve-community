# Reto 3: El Primer Test 🕵️‍♂️

Tu compañero de trabajo escribió una función para verificar si una contraseña es válida (tiene al menos 8 caracteres). ¡Pero no la ha probado! Te toca a ti crear las pruebas automáticas.

## Instrucciones Paso a Paso:

1. Crea un archivo llamado `test_reto.py` (es vital que el archivo empiece con `test_`).
2. Copia la función de tu compañero en ese archivo:
```python
def es_contrasena_segura(contrasena: str) -> bool:
    """Devuelve True si la contraseña tiene 8 caracteres o más."""
    return len(contrasena) >= 8
```
3. Abajo de esa función, crea un test llamado `test_contrasena_corta()`. Adentro, usa `assert` para exigir que al pasarle `"123"` a la función, el resultado sea igual a `False`.
4. Crea otro test llamado `test_contrasena_larga()`. Adentro, usa `assert` para exigir que al pasarle `"secreto123"` a la función, el resultado sea igual a `True`.
5. Abre la **terminal** de tu editor y ejecuta el siguiente comando: 
   `pytest test_reto.py`

## Reglas Estrictas:
✅ **Conceptos Permitidos:** `def`, `assert`, `len()`, `==` (doble igual), y crear funciones que empiecen con `test_`.
❌ **Conceptos Prohibidos:** Usar `print()`. ¡En los tests automáticos no miramos prints en la pantalla, miramos que todo salga verde!

## Resultado Esperado en tu Terminal:

Cuando ejecutes `pytest test_reto.py`, deberías ver un mensaje hermoso y verde (o al menos con texto indicando 100% de éxito), muy parecido a esto:

```text
============================= test session starts ==============================
collected 2 items                                                              

test_reto.py ..                                                          [100%]

============================== 2 passed in 0.01s ===============================
```

Si logras ver ese "2 passed", ¡felicidades! Eres oficialmente un programador que hace tests automáticos.
