# Reto 2: El Filtro de Mensajes 📨

Trabajas para el equipo de moderación de una red social. Recibes una lista enorme de mensajes del día. Tu tarea: construir un generador que revise los mensajes **uno a uno** y solo entregue los que contienen una palabra clave sospechosa, sin cargar todos en memoria a la vez.

## Instrucciones Paso a Paso:

Copia esta lista de mensajes en tu código:

```python
mensajes = [
    "Hola, ¿cómo estás?",
    "Compra ahora con DESCUENTO increíble",
    "El partido fue increíble ayer",
    "GANA dinero desde casa GRATIS",
    "Me comí una pizza enorme",
    "URGENTE: reclama tu premio GRATIS",
    "El examen estuvo difícil",
    "Haz click AQUÍ para ganar DESCUENTO",
]
```

1. Crea una función generadora llamada `filtrar_sospechosos` que reciba una lista de mensajes y una palabra clave.
2. Dentro de la función, usa un bucle `for` para recorrer los mensajes.
3. Con un `if`, revisa si la palabra clave está **contenida** en el mensaje (recuerda: `"palabra" in texto` devuelve `True` o `False`).
4. Si el mensaje contiene la palabra clave, usa `yield` para entregarlo.
5. En tu programa principal, crea el generador buscando la palabra `"GRATIS"`.
6. Recorre el generador con un `for` e imprime cada mensaje sospechoso con su número de alerta.

> **Pista:** Para numerar los mensajes mientras los recorres, usa `enumerate()` sobre el generador. Ya lo aprendiste en el módulo de bucles.

## Reglas Estrictas:
✅ **Conceptos Permitidos:** `def`, `yield`, `for`, `if`, `in` (para buscar en texto), `enumerate()`, `print()`, f-strings, listas.
❌ **Conceptos Prohibidos:** Clases, `import`, list comprehensions como solución, guardar en una lista todos los sospechosos antes de imprimirlos.

## Resultado Esperado en tu Terminal:

```text
=== Escaneando mensajes con la palabra: GRATIS ===

Alerta #1: GANA dinero desde casa GRATIS
Alerta #2: URGENTE: reclama tu premio GRATIS

Escaneo completo. 2 mensajes sospechosos encontrados.
```

Crea tu código en `reto.py`. Si cambias la palabra clave a `"DESCUENTO"`, tu generador debe encontrar 2 mensajes distintos sin tocar más código.
