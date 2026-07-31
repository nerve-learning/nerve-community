# Teoría: Claves y Valores

Para crear un Diccionario, usamos un nuevo símbolo: **las llaves `{` y `}`**.

Adentro de las llaves, la información siempre viaja en parejas. A esta pareja la llamamos **Clave y Valor**. 
- La **Clave** es la etiqueta que usas para buscar (como la palabra en un diccionario real).
- El **Valor** es lo que está guardado ahí (como el significado de esa palabra).

Para separar la Clave del Valor, usamos **dos puntos `:`**. Para separar una pareja de otra, usamos la **coma `,`**.

## Anatomía

```python
agenda = {"Ana": 5551234, "Beto": 5559876}
```

Desmontemos la sintaxis:
- `agenda`: El nombre de la variable.
- `=`: Símbolo de asignación.
- `{`: Abre el diccionario.
- `"Ana"`: La **Clave** (siempre suele ser un texto).
- `:`: Conecta la Clave con su Valor. Significa "le corresponde".
- `5551234`: El **Valor** (puede ser texto, número, booleano...).
- `,`: Separa la pareja de Ana de la pareja de Beto.
- `}`: Cierra el diccionario.

## ¿Cómo busco algo?
En las listas usábamos números: `lista[0]`. En los diccionarios, usamos el nombre de la clave.
```python
numero_de_ana = agenda["Ana"]
```

## ¿Qué pasa si me equivoco?

**El error más común:** Buscar una etiqueta que no existe.
Si escribes:
```python
agenda = {"Ana": 5551234}
print(agenda["Carlos"])
```
La computadora entrará en pánico y mostrará: `KeyError: 'Carlos'`. 
Significa "Error de Clave: Carlos no existe en este diccionario". ¡No puedes buscar una palabra que no ha sido escrita en tu libro!

**Otro error común:** Confundir `:` con `=`.
Al crear el diccionario, las parejas se unen con `:`. Si usas `=` adentro de las llaves, la terminal mostrará un error de sintaxis (`SyntaxError`).
