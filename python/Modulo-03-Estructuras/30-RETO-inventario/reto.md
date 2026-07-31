# Reto 30: El Mercader del Reino 🏪

Es tu turno de aplicar absolutamente todo lo aprendido. Eres el dueño de una tienda de pociones en un mundo de fantasía. Necesitas crear el sistema de gestión de tu tienda combinando todas las estructuras de datos en una sola.

## Instrucciones

1. En la primera línea de tu código, trae la herramienta para clonar (`import copy`).
2. Crea un diccionario principal llamado `tienda`. Debe contener exactamente estas llaves y valores:
   - Clave `"nombre"`: El texto `"Pociones Mágicas"`.
   - Clave `"coordenadas"`: Una tupla con los números `(42, 108)`.
   - Clave `"productos"`: Una lista que contenga los textos `"Poción Roja"` y `"Poción Azul"`.
   - Clave `"clientes_vip"`: Un set que contenga los textos `"Mago Gandalf"` y `"Rey Arturo"`.
3. ¡Ha llegado un nuevo cliente VIP! Añade a `"Reina Reina"` al set de clientes VIP de la tienda.
4. ¡El proveedor trajo nueva mercancía! Agrega la `"Poción Verde"` a la lista de productos de la tienda.
5. Has decidido abrir una franquicia en otro lado. Crea una variable llamada `tienda_franquicia` y hazle un **clon profundo** (deepcopy) a la `tienda` original.
6. A la `tienda_franquicia`, cámbiale el nombre a `"Pociones Mágicas - Sur"`.
7. En la `tienda_franquicia`, elimina la `"Poción Roja"` de su lista de productos (ya no la venden ahí).
8. Imprime la `tienda` original completa.
9. Imprime la `tienda_franquicia` completa.

## Conceptos permitidos
- Diccionarios `{}`, Tuplas `()`, Listas `[]`, Sets `set()` o `{}`.
- Agregar a listas (`.append()`), eliminar de listas (`.remove()`).
- Agregar a sets (`.add()`).
- Asignar o cambiar valores en diccionarios `diccionario["clave"] = nuevo_valor`.
- `import copy` y `copy.deepcopy()`.
- `print()`.

## Resultado esperado en la terminal
*(Nota: El orden de los elementos dentro del set (los clientes VIP) puede verse diferente en tu terminal, ¡eso es normal y correcto!)*

```text
{'nombre': 'Pociones Mágicas', 'coordenadas': (42, 108), 'productos': ['Poción Roja', 'Poción Azul', 'Poción Verde'], 'clientes_vip': {'Reina Reina', 'Mago Gandalf', 'Rey Arturo'}}
{'nombre': 'Pociones Mágicas - Sur', 'coordenadas': (42, 108), 'productos': ['Poción Azul', 'Poción Verde'], 'clientes_vip': {'Reina Reina', 'Mago Gandalf', 'Rey Arturo'}}
```
