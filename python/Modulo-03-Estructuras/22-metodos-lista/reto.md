# Reto 22: El Menú del Restaurante 🍔

Eres el chef de un restaurante y estás diseñando el menú del día usando Python. Sin embargo, los ingredientes se acaban y hay que actualizar la pizarra de platos.

## Instrucciones

1. Crea un archivo llamado `reto.py`.
2. Crea una lista vacía llamada `menu_del_dia`. 
3. Imprime un texto que diga `"Menú inicial:"` y debajo imprime la lista.
4. Usa `.append()` tres veces seguidas para agregar estos platos al menú, en este orden: `"Sopa"`, `"Ensalada"`, `"Pasta"`.
5. Imprime un texto que diga `"Menú actualizado:"` y debajo imprime la lista.
6. ¡Oh no! Se acabó la lechuga. Usa `.remove()` para quitar la `"Ensalada"` del menú.
7. Imprime un texto que diga `"Sin ensalada:"` y debajo imprime tu lista una vez más para ver cómo quedó.

### Conceptos Permitidos
- Listas vacías (`[]`).
- Métodos `.append()` y `.remove()`.
- La función `print()`.

### Conceptos PROHIBIDOS
- Re-asignar la lista manualmente (ej. `menu_del_dia = ["Sopa", "Pasta"]`). ¡Debes usar `.remove()`!
- Borrar por posición (ej. usar la palabra `del` o `.pop()`).

## Resultado Esperado en la Terminal

Al ejecutar tu código, la terminal debería mostrar EXACTAMENTE esto:

```text
Menú inicial:
[]
Menú actualizado:
['Sopa', 'Ensalada', 'Pasta']
Sin ensalada:
['Sopa', 'Pasta']
```

¡A cocinar se ha dicho!
