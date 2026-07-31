# Reto 27: El Hacker de Archivos 🕵️‍♂️

Te has infiltrado en la base de datos de una corporación maligna. Han ocultado la contraseña secreta muy profundo dentro de unas estructuras de datos anidadas. ¡Tu misión es extraerla usando tus conocimientos de corchetes dobles!

## Instrucciones

1. Crea un archivo llamado `reto.py`.
2. Copia EXACTAMENTE esta variable en tu archivo (¡no la modifiques!):
   ```python
   servidor = [
       {"id": 1, "datos": ["basura", "basura"]},
       {"id": 2, "datos": ["basura", "CONTRASEÑA_SECRETA"]}
   ]
   ```
3. Imprime el mensaje: `"--- INICIANDO HACKEO ---"`.
4. Necesitas llegar a `"CONTRASEÑA_SECRETA"`. Fíjate bien:
   - `servidor` es una lista. ¿En qué posición numérica está el diccionario que nos importa?
   - Una vez en el diccionario, ¿qué clave (`"id"` o `"datos"`) tiene lo que queremos?
   - Esa clave nos da otra lista. ¿En qué posición numérica está la contraseña?
5. Extrae el valor usando los accesos anidados (por ejemplo, pegando corchetes uno tras otro: `variable[a]["b"][c]`) y guárdalo en una variable llamada `clave_extraida`.
6. Imprime la variable `clave_extraida`.

### Conceptos Permitidos
- Variables, Listas (acceso numérico `[0]`) y Diccionarios (acceso por clave `["clave"]`).
- Anidamiento (`[][]`).
- La función `print()`.

### Conceptos PROHIBIDOS
- Escribir manualmente `print("CONTRASEÑA_SECRETA")`. ¡Tienes que sacarla de la variable `servidor`!
- Modificar la variable `servidor` original.

## Resultado Esperado en la Terminal

Al ejecutar tu código, la terminal debería mostrar EXACTAMENTE esto:

```text
--- INICIANDO HACKEO ---
CONTRASEÑA_SECRETA
```

¡Excelente trabajo rompiendo la seguridad!
