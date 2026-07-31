# Reto 28: El Espía del FBI 🕵️‍♀️

El FBI tiene una lista con los nombres de 3 sospechosos. Un espía novato intentó hacer una copia del archivo para estudiarlo, pero cometió el error de usar el signo `=` directamente. Cuando borró un nombre de su "copia", ¡lo borró de la base de datos central!

Tu misión es recrear el desastre y luego arreglarlo creando una copia real.

## Instrucciones

1. Crea un archivo llamado `reto.py`.
2. Crea una variable llamada `sospechosos_fbi` que sea una **Lista** con 3 textos: `"Zorro"`, `"Halcón"`, `"Cuervo"`.
3. Crea otra variable llamada `copia_novato` y asígnale `sospechosos_fbi` (usando solo `=`).
4. Usa `.remove()` en `copia_novato` para eliminar al `"Halcón"`.
5. Imprime el mensaje: `"¡Desastre! La base del FBI ahora es:"`.
6. Imprime `sospechosos_fbi` para ver el desastre (el Halcón ya no está).
7. ¡Reinicia el servidor! Crea de nuevo la variable `sospechosos_fbi` con los 3 nombres originales (`"Zorro"`, `"Halcón"`, `"Cuervo"`).
8. Crea una variable `copia_experto` pero esta vez **haz un clon real** usando el truco del slicing `[:]`.
9. Borra al `"Halcón"` de `copia_experto`.
10. Imprime el mensaje: `"Base de datos segura:"`.
11. Imprime la lista `sospechosos_fbi`. (¡El Halcón debería seguir ahí!).

### Conceptos Permitidos
- Listas y el método `.remove()`.
- Slicing `[:]` para hacer copias reales.
- La función `print()`.

### Conceptos PROHIBIDOS
- Escribir las listas modificadas manualmente en el `print`. ¡Todo debe ser a través de las variables!

## Resultado Esperado en la Terminal

Al ejecutar tu código, la terminal debería mostrar EXACTAMENTE esto:

```text
¡Desastre! La base del FBI ahora es:
['Zorro', 'Cuervo']
Base de datos segura:
['Zorro', 'Halcón', 'Cuervo']
```

¡Excelente trabajo salvando los datos del gobierno!
