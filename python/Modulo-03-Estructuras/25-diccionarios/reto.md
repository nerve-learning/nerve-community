# Reto 25: El Traductor Alienígena 👽

Has hecho contacto con una especie alienígena. Para poder comunicarte, necesitas crear un pequeño diccionario traductor de su idioma al español.

## Instrucciones

1. Crea un archivo llamado `reto.py`.
2. Crea una variable llamada `traductor` que sea un **Diccionario**.
3. Añade tres parejas (Clave: Valor) a tu diccionario. Las claves serán las palabras alienígenas (textos) y los valores su significado en español (textos):
   - `"Blarg"` significa `"Hola"`
   - `"Flib"` significa `"Adiós"`
   - `"Grox"` significa `"Comida"`
4. Imprime el mensaje: `"--- INICIANDO TRADUCTOR ---"`.
5. Extrae el significado de la palabra `"Blarg"` usando corchetes (ej. `traductor["palabra"]`) y guárdalo en una variable llamada `saludo`.
6. Imprime la variable `saludo`.
7. Los alienígenas te han enseñado una nueva palabra. Añade al diccionario la clave `"Zorp"` con el valor `"Paz"`. (Hazlo en una nueva línea, no modificando la variable original inicial).
8. Imprime el diccionario `traductor` completo para ver la nueva palabra agregada.

### Conceptos Permitidos
- Diccionarios (creación con llaves `{}` y `:`).
- Acceso y modificación usando corchetes con el nombre de la clave `["clave"]`.
- La función `print()`.

### Conceptos PROHIBIDOS
- Usar índices numéricos (`traductor[0]`). ¡Los diccionarios no tienen orden numérico, tienen etiquetas!
- Usar métodos avanzados que no hemos visto como `.get()` o `.update()`.

## Resultado Esperado en la Terminal

Al ejecutar tu código, la terminal debería mostrar EXACTAMENTE esto:

```text
--- INICIANDO TRADUCTOR ---
Hola
{'Blarg': 'Hola', 'Flib': 'Adiós', 'Grox': 'Comida', 'Zorp': 'Paz'}
```

¡Excelente trabajo de diplomacia intergaláctica!
