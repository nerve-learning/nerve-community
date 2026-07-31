# Teoría: Cámaras de Seguridad en tu Código

La computadora es obediente, pero ciega. Si le das una instrucción equivocada, la ejecutará felizmente. El problema ocurre cuando **tú crees que una variable vale algo, pero en realidad vale otra cosa**.

### ¿Qué es la "Depuración"?
Depurar (*debug*) significa buscar y corregir errores. El error más común a tu nivel no es que la terminal explote (error de sintaxis), sino que el programa no haga lo que querías (error de lógica).

### La técnica del "print() diagnóstico"
Imagina que tienes una tubería de agua y el agua no llega al final. ¿Qué haces? Pones medidores en distintos puntos del tubo.
En código, usamos `print()` para asomarnos dentro del cerebro de Python en puntos clave.

Hay dos cosas principales que queremos imprimir para investigar:
1. **El valor de las variables antes de un `if`:** Para ver si realmente tienen el valor que esperamos.
2. **Mensajes de "estoy aquí":** Para saber en qué bloque `if`, `elif` o `else` decidió entrar Python.

---

## Anatomía (Sintaxis Diagnóstica)

```python
edad_usuario = 15
# ERROR COMÚN: Pensamos que tiene 18.
# SOLUCIÓN: Imprimir antes de evaluar.
print("DEBUG - Valor de edad:", edad_usuario)

if edad_usuario >= 18:
    print("DEBUG - Entró al if") # Nos dice qué camino tomó
    print("Eres mayor de edad.")
else:
    print("DEBUG - Entró al else") # Nos dice qué camino tomó
    print("Eres menor de edad.")
```
*Nota: La palabra "DEBUG" es una costumbre de los programadores para saber que ese print es solo para nosotros, no para el usuario final. Luego, cuando el código funciona, borramos esos prints.*

---

## ¿Qué pasa si me equivoco?

**1. Olvidar borrar los prints de debug**
Si dejas todos tus `print("DEBUG - la variable vale...")` y entregas tu programa, tu usuario verá mensajes extraños que no entiende. ¡Recuerda limpiar tus "cámaras de seguridad" cuando atrapes al ladrón (el error)!

**2. Depurar el síntoma, no la enfermedad**
A veces ves que un `if` falla e intentas cambiar el `if`. Pero si pones un `print` arriba, descubrirás que el error no era el `if`, ¡sino un cálculo matemático mal hecho 5 líneas antes que arruinó la variable!
