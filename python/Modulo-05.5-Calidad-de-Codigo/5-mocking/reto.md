# Reto 5: Salva la Tarjeta de Crédito 💳

Estás probando una función para una tienda en línea. Esta función revisa que un carrito de compras tenga cosas y, si es así, intenta cobrar el dinero de verdad.

¡No queremos perder nuestro dinero corriendo tests! Vas a crear un Mock (un doble de acción) para fingir el cobro sin gastar un centavo.

## Instrucciones Paso a Paso:

1. Crea el archivo `test_reto_mock.py`.
2. Copia este código base que simula nuestro sistema:

```python
# El actor peligroso real
def cobrar_a_banco_real():
    print("¡COBRANDO 100 DÓLARES AL BANCO!")
    return "Pagado"

# La función que queremos probar, preparada para recibir Mocks
def finalizar_compra(carrito: list, funcion_cobro = cobrar_a_banco_real) -> str:
    if len(carrito) == 0:
        return "Error: carrito vacio"
    
    # Cobramos usando la función que nos pasen
    estado_pago = funcion_cobro()
    
    if estado_pago == "Pagado":
        return "Compra exitosa"
    else:
        return "Error en el pago"
```

3. Crea un test llamado `def test_finalizar_compra_con_exito():`.
4. Adentro del test, **crea una función falsa** (tu doble de acción) llamada `cobro_falso_exitoso()`. Esta función debe devolver simplemente el texto `"Pagado"`.
5. En el test, llama a `finalizar_compra`. 
   - El primer parámetro (el carrito) debe ser una lista con un producto, por ejemplo: `["Zapatos"]`.
   - El segundo parámetro debe ser tu función doble de acción. **(¡Recuerda pasarla SIN los paréntesis `()`!)**.
   - Guarda el resultado en una variable.
6. Usa `assert` para exigir que el resultado de la compra sea `"Compra exitosa"`.
7. Ejecuta `pytest test_reto_mock.py` en tu terminal. 

> *Opcional: Si quieres un reto mayor, crea un segundo test `test_finalizar_compra_rechazada` donde el doble de acción devuelva `"Rechazado"` y exige que el resultado sea `"Error en el pago"`.*

## Reglas Estrictas:
✅ **Conceptos Permitidos:** `def`, `assert`, listas `[]`, asignar valores por defecto en los parámetros (`=`), pasar funciones como parámetros.
❌ **Conceptos Prohibidos:** Ejecutar la función original `cobrar_a_banco_real()`. ¡Tu test no debe imprimir nada de "COBRANDO 100 DÓLARES"!

## Resultado Esperado en tu Terminal:

```text
============================= test session starts ==============================
collected 1 item                                                               

test_reto_mock.py .                                                      [100%]

============================== 1 passed in 0.01s ===============================
```
¡Tu test corrió exitosamente y tu billetera está a salvo gracias al Mock!
