# Teoría: El Acróbata y la Red (`try` y `except`)

Imagina que tu código es un acróbata de circo. Hay partes de su rutina que son seguras (caminar por el suelo), pero hay partes muy peligrosas (saltar en el trapecio a 10 metros de altura).

Si el acróbata resbala en el trapecio sin protección, el show termina en tragedia (tu programa muere). 
Para evitar esto, le ponemos una red de seguridad abajo. Si resbala, cae en la red, se levanta, y el show continúa.

En Python, el trapecio se llama `try` y la red de seguridad se llama `except`.

## La Anatomía de `try / except`

```python
try:
    # Código peligroso aquí
    resultado = 10 / 0
except Exception as e:
    # Código de rescate aquí
    print("¡Ups! Caímos en la red:", e)
```

**Desmontaje de los símbolos nuevos:**
- `try:` (Intenta): Literalmente le dice a Python *"Intenta ejecutar las siguientes líneas, pero ten mucho cuidado porque podrían fallar"*.
- `except:` (Excepto): Significa *"Si alguna línea dentro de 'try' falla, detén la caída inmediatamente y salta hacia aquí"*.
- `Exception`: Es la palabra oficial en Python para decir "Cualquier Error".
- `as e` (como `e`): Le decimos a Python *"Toma todos los detalles técnicos y feos del error, y guárdalos en una cajita (variable) llamada 'e', por si quiero leerlos"*.

## ¿Cómo funciona el flujo?
1. Python entra al bloque `try`.
2. Ejecuta línea por línea.
3. Si **TODO** sale bien, Python ignora por completo el bloque `except` y sigue con el resto del programa.
4. Si **ALGO** falla, Python aborta inmediatamente el bloque `try` (las líneas que faltaban ahí no se ejecutan) y salta directo al bloque `except`. ¡El programa no muere!

## ¿Qué pasa si me equivoco?

### Error Común 1: Olvidar los dos puntos `:`
Al igual que con los `if`, `for`, `while` y `def`, las palabras `try` y `except` abren un nuevo bloque de código. Por lo tanto, SIEMPRE deben terminar con dos puntos `:`. Si los olvidas, Python se quejará con un *SyntaxError*.

### Error Común 2: Mala Indentación
Todo lo que está *dentro* de la red de seguridad debe tener un espacio hacia la derecha (indentación). 
```python
# MAL:
try:
print("Peligro")
```

### Error Común 3: Poner código seguro dentro de la zona de peligro
El bloque `try` debe ser lo más pequeño posible. Solo debes meter ahí la instrucción exacta que sospechas que puede explotar (como abrir un archivo o dividir variables). El resto del código normal debe ir fuera.
