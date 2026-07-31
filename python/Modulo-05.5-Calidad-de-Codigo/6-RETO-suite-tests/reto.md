# Reto 6: El Guardián del Código (Jefe Final) 🐉

¡El código del banco es un desastre! Encontraste un archivo viejo llamado `sistema_banco.py`. No tiene etiquetas de tipo (Type Hints), no tiene manual de instrucciones (Docstrings), y lo peor de todo... **¡No tiene ni un solo test!**

Tu misión es transformar este código frágil en código de nivel profesional usando todas tus herramientas.

## Código Base (Copia esto en `reto.py`)

```python
# CÓDIGO VIEJO A ARREGLAR:
def transferir_dinero(saldo_origen, cantidad, funcion_cobro):
    if cantidad > saldo_origen:
        return "Saldo insuficiente"
    
    resultado = funcion_cobro(cantidad)
    
    if resultado == True:
        return "Transferencia exitosa"
    else:
        return "Error en el banco"
```

## Instrucciones Paso a Paso:

### Fase 1: Calidad Visual (Type Hints y Docstrings)
1. Agrega **Type Hints** a la función `transferir_dinero`. (Pista: `saldo_origen` y `cantidad` son `float`. ¿Qué tipo de dato devuelve la función en sus `return`?).
2. Agrega un **Docstring** debajo de la línea `def` explicando qué hace la función, documentando cada parámetro en `Args:` y qué devuelve en `Returns:`.

### Fase 2: La Suite de Pruebas Automáticas
3. Escribe `import pytest` arriba de todo tu archivo.
4. Crea un **Fixture** llamado `saldo_rico()` que use `return` para devolver el número decimal `1000.0`.
5. **Prueba Parametrizada de Fallo:** Crea un test llamado `test_fondos_insuficientes` parametrizado.
   - Usa `@pytest.mark.parametrize` para probar tres cantidades imposibles de pagar: `1500.0`, `5000.0` y `1000.1`. (El parámetro puede llamarse `"monto_gigante"`).
   - El test debe recibir tu fixture `saldo_rico` y el `"monto_gigante"`.
   - Crea un "Doble de Acción" vacío adentro del test (`def cobro_falso(monto): return False`) y pásalo a la función. En realidad el código nunca llegará a usarlo porque fallará antes.
   - Llama a `transferir_dinero` y usa `assert` para exigir que devuelva `"Saldo insuficiente"`.
6. **Prueba con Mock Exitoso:** Crea un test llamado `test_transferencia_correcta`.
   - Debe recibir el fixture `saldo_rico`.
   - Crea un Doble de Acción adentro del test que SIEMPRE devuelva `True`.
   - Llama a `transferir_dinero` pasándole el `saldo_rico`, un monto de `100.0`, y tu Doble de Acción.
   - Usa `assert` para exigir que devuelva `"Transferencia exitosa"`.
7. Ejecuta `pytest reto.py` en tu terminal.

## Reglas Estrictas:
✅ **Conceptos Permitidos:** Todos los del Módulo 5.5 (`def`, `assert`, `import pytest`, `@pytest.fixture`, `@pytest.mark.parametrize`, Mocks pasados por parámetro, Type Hints, Docstrings).
❌ **Conceptos Prohibidos:** Clases o librerías externas que no sean `pytest`. ¡Nada de prints!

## Resultado Esperado:
Tu archivo `reto.py` ahora tendrá una función bellamente documentada y etiquetada, acompañada de una suite de tests (uno parametrizado que ejecuta 3 pruebas, y uno normal con Mock). 

Al ejecutar `pytest reto.py`, la terminal debería mostrarte todo en verde con un glorioso **"4 passed"**. ¡Felicidades, te has graduado del Módulo de Calidad de Código!
