# Teoría: La Licuadora de Datos 🌪️

Hasta ahora, nuestra bandejita `()` estaba vacía. Hoy vamos a ponerle etiquetas.

## 1. Parámetros (Los Ingredientes)

Cuando **defines** la función, pones "etiquetas" (variables temporales) dentro de los paréntesis. Esto le dice a Python: *"Para que esta receta funcione, me tienes que dar estos datos"*.

```python
def saludar_jugador(nombre):
    print("¡Bienvenido al nivel, " + nombre + "!")
```

- `nombre`: Es una variable que **solo existe dentro de esta función**. Es un hueco vacío esperando ser llenado.

Cuando **llamas** a la función, tienes que entregarle el valor real (el ingrediente de verdad):

```python
saludar_jugador("Alejandro") 
```
Python automáticamente dice: *Ah, "Alejandro" se guarda en la caja `nombre`*.

## 2. El comando `return` (Entregando el platillo)

Hasta ahora usábamos `print()`. El problema de `print()` es que solo muestra un mensaje en la pantalla de la terminal, pero el programa "olvida" ese valor inmediatamente. 

Imagina que le das dinero a un cajero automático para que lo cuente. Si el cajero usa `print()`, solo te grita en la cara: *"¡TIENES 100 DÓLARES!"*, pero no te da el dinero. 
Si el cajero usa `return`, te **entrega** físicamente los billetes para que tú puedas guardarlos en tu billetera.

```python
def sumar(numero1, numero2):
    resultado = numero1 + numero2
    return resultado # ¡Aquí escupe el dato hacia afuera!
```

- `return`: Es una palabra mágica que significa **"Termina la función AHORA MISMO y escupe este valor hacia afuera"**. 
Cualquier código que pongas debajo de un `return` en la misma función, jamás se ejecutará, porque `return` es una puerta de salida inmediata.

Al llamar a una función que tiene `return`, debes **atrapar** el valor en una variable (tu billetera):

```python
mi_dinero = sumar(50, 50) # mi_dinero ahora vale 100
```

---

## 🚨 ¿Qué pasa si me equivoco?

### Error 1: Olvidar un ingrediente
**El síntoma en la terminal:** `TypeError: sumar() missing 1 required positional argument: 'numero2'`
**¿Por qué pasa?** Tu receta exigía 2 ingredientes (ej. `def sumar(a, b):`), pero cuando la llamaste solo le diste uno (`sumar(5)`). ¡Python no sabe qué hacer con el hueco vacío! Tienes que darle exactamente la misma cantidad de ingredientes que pide la receta.

### Error 2: Intentar usar una variable de la función afuera de ella
**El síntoma en la terminal:** `NameError: name 'resultado' is not defined`
**¿Por qué pasa?** Las cajas (variables) que creas dentro de una función **nacen y mueren** dentro de esa función. Son secretas. Si creaste `resultado` dentro del `def`, no puedes usar un `print(resultado)` afuera sin haber usado `return`.

### Error 3: Imprimir en lugar de Retornar
**El síntoma en la terminal:** Al intentar guardar el valor e imprimirlo, sale la palabra `None` (Nada).
**¿Por qué pasa?** Hiciste `def calcular(): print(5 + 5)` y luego `mi_variable = calcular()`. Como no usaste `return`, la función no te entregó nada físico. Mostró un 10 en la pantalla y te entregó aire (`None`). ¡Usa `return` si quieres guardar el dato!
