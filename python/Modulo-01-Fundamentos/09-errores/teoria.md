# Teoría: Entendiendo a Python cuando se enoja

Cuando cometes un error escribiendo código, Python detiene el programa y te muestra un mensaje. A este mensaje se le llama **Traceback** (Rastreo). 

Al principio, un Traceback parece un montón de texto aterrador e incomprensible, pero en realidad es un mapa del tesoro que te dice exactamente dónde está el problema.

## Anatomía de un Error (Traceback)

Imagina que ejecutas un archivo y Python te responde esto:

```text
Traceback (most recent call last):
  File "mi_programa.py", line 3, in <module>
    print(mi_variable)
NameError: name 'mi_variable' is not defined
```

¡No entres en pánico! Léelo de abajo hacia arriba:

1.  **La última línea es la más importante**: `NameError: name 'mi_variable' is not defined`. 
    *   Te dice el **tipo de error** (`NameError`).
    *   Te da una **descripción** del problema ("el nombre 'mi_variable' no está definido").
2.  **Las líneas de arriba te dicen DÓNDE ocurrió**: 
    *   `File "mi_programa.py", line 3`. ¡Te está diciendo que vayas a la línea 3 de tu archivo!

## Los 3 Errores Clásicos

Como principiante (y como experto), te vas a encontrar con estos tres errores miles de veces.

### 1. SyntaxError (Error de Sintaxis)
**Qué significa:** Escribiste algo mal. Te faltó un paréntesis, una comilla o usaste un símbolo donde no iba. Para Python, esto es como si escribieras "Hola com0 stas" con mala ortografía; simplemente se niega a leerlo.

**Ejemplo que lo causa:**
```python
print("Hola mundo)  # ¡Falta la comilla de cierre!
```

### 2. NameError (Error de Nombre)
**Qué significa:** Estás intentando usar una variable que **no existe** (porque nunca la creaste con el símbolo `=`) o escribiste mal su nombre.

**Ejemplo que lo causa:**
```python
mensaje = "Hola"
print(mensaj)  # Escribiste "mensaj" en lugar de "mensaje". Python no sabe qué es "mensaj".
```

### 3. TypeError (Error de Tipo)
**Qué significa:** Estás intentando mezclar agua y aceite. Es decir, intentas hacer una operación con dos Tipos de Datos incompatibles (por ejemplo, sumar texto con números).

**Ejemplo que lo causa:**
```python
texto = "Tengo "
edad = 25
resultado = texto + edad  # ¡Error! No puedes sumar una palabra con un número entero así nomás.
```
*(Recuerda que para mezclar texto y números aprendimos a usar las f-strings).*

---
**Regla de Oro del Programador:** Los errores no significan que seas malo programando, son la forma en que la computadora te guía para arreglar el problema. Lee siempre la última línea del Traceback.
