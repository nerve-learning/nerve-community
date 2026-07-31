# Teoría: La Muñeca Rusa 🪆

Hasta ahora usábamos `for` o `while` para repetir cosas. La recursividad es otra forma de repetir, pero usando las mismas funciones que aprendimos.

Toda función recursiva DEBE tener dos partes vitales. Si te olvidas de una, tu programa morirá.

## 1. El Caso Base (El Freno) 🛑
Es un `if`. Es la muñequita sólida del centro. Le dice a la función: *"¡Alto! Ya el problema es tan pequeño que no necesitas llamarte de nuevo. Simplemente devuelve un resultado o termina."*
**Sin esto, la función se llamará a sí misma por toda la eternidad.**

## 2. La Llamada Recursiva (El Espejo) 🪞
Es la parte donde la función se llama a sí misma por su propio nombre, pero pasándole un problema **más pequeño**. (Por ejemplo, si le pasaste el número 5, ahora se llama a sí misma pasándose un 4).

## 🧬 Anatomía de la Recursividad

```python
def cuenta_regresiva(numero):
    # 1. EL FRENO (Caso Base)
    if numero == 0:
        print("¡Despegue!")
        return # Salida de emergencia. Detiene la recursividad.
    
    # 2. ACCIÓN NORMAL
    print(numero)
    
    # 3. EL ESPEJO (Llamada Recursiva)
    # Me llamo a mí mismo, pero con un número más pequeño (numero - 1)
    cuenta_regresiva(numero - 1)
```

Cuando ejecutas `cuenta_regresiva(3)`, pasa esto en cámara lenta:
1. Entra el `3`. Imprime `3`. Llama a `cuenta_regresiva(2)`.
2. La nueva función revisa si es 0. No. Imprime `2`. Llama a `cuenta_regresiva(1)`.
3. La nueva función revisa si es 0. No. Imprime `1`. Llama a `cuenta_regresiva(0)`.
4. La nueva función revisa si es 0. **¡SÍ!** Imprime "¡Despegue!" y pisa el freno (return). ¡Todo termina!

---

## 🚨 ¿Qué pasa si me equivoco?

### Error 1: Olvidar el Caso Base (El Freno)
**El síntoma en la terminal:** `RecursionError: maximum recursion depth exceeded`
**¿Por qué pasa?** A diferencia de un `while True` que se queda congelado girando por siempre, la recursividad es como meter cajas dentro de cajas dentro de cajas. La memoria RAM de tu computadora tiene un límite de "cajas" que puede apilar. Si no pones el `if` que pise el freno, Python creará cajas infinitas hasta quedarse sin memoria, y por seguridad, hace explotar el programa lanzando este error.

### Error 2: Pasar siempre el mismo problema
**El síntoma en la terminal:** También `RecursionError`.
**¿Por qué pasa?** Pusiste el freno (`if numero == 0`), pero en tu llamada recursiva hiciste `cuenta_regresiva(numero)` en vez de `numero - 1`. Si entraste con un 5, te llamas a ti mismo con un 5, luego con un 5... ¡Jamás llegarás al 0! El problema que le pasas al espejo siempre debe ser **más pequeño** para que avance hacia el freno.
