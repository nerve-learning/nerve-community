# Reto 23: El Tren de Carga 🚂

Eres el conductor de un tren que transporta suministros importantes. Tienes un registro de todos los vagones en orden, pero necesitas extraer información específica para los inspectores.

## Instrucciones

1. Crea un archivo llamado `reto.py`.
2. Crea una lista llamada `tren` con los siguientes 5 elementos en este orden exacto:
   `"Locomotora"`, `"Carbón"`, `"Pasajeros"`, `"Oro"`, `"Madera"`.
3. Imprime un mensaje que diga `"Vagón VIP:"`.
4. Usando el acceso por índice `[]`, extrae e imprime el vagón de los `"Pasajeros"`. (¡Recuerda contar desde cero!).
5. Imprime un mensaje que diga `"Carga preciosa:"`.
6. Usando slicing `[:]`, extrae e imprime una nueva lista que contenga SOLO `"Pasajeros"` y `"Oro"`.

### Conceptos Permitidos
- Listas y asignación de variables.
- Acceso por índice (ej. `lista[2]`).
- Rebanado o Slicing (ej. `lista[1:4]`).
- Función `print()`.

### Conceptos PROHIBIDOS
- Escribir manualmente la lista filtrada (ej. `print(["Pasajeros", "Oro"])`). ¡Debes extraerlos de la variable `tren` usando corchetes!
- Usar `.remove()` o `.append()`. Todo se hace leyendo y cortando la lista original.

## Resultado Esperado en la Terminal

Al ejecutar tu código, la terminal debería mostrar EXACTAMENTE esto:

```text
Vagón VIP:
Pasajeros
Carga preciosa:
['Pasajeros', 'Oro']
```

¡Cuidado con no caerte de los vagones!
