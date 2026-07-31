# Teoría: El Toque Profesional 🎩

Hasta ahora, tú (el creador) has usado la terminal para hacer cosas mágicas con Nerve. Pero, ¿qué pasa cuando le envías tu programa a tu amigo, mamá o cliente? Ellos no saben abrir una terminal.

Para que tu programa sea "profesional", debe configurarse solo.

## Automatizando la Asociación

En niveles anteriores aprendiste que el comando `nerve associate` le enseña a tu sistema operativo a reconocer los archivos `.nrv` (para que tengan el ícono de Nerve y se abran al hacer doble clic). 

¿Y si hacemos que Python escriba ese comando por nosotros?

Ya conocemos la herramienta perfecta para esto: `os.system()` de nuestro módulo `os`.

### 🧠 Anatomía de un Comando Automatizado

```python
import os

# Python le dice a la terminal que ejecute este comando por nosotros
os.system("nerve associate")
```

1. **`import os`**: Despertamos a nuestro traductor del sistema operativo.
2. **`os.system()`**: Le damos una instrucción para que la escriba en la terminal invisible.
3. **`"nerve associate"`**: El comando exacto que queremos ejecutar.

De la misma manera, si el usuario quiere desinstalar nuestro programa, podemos ser educados y limpiar la computadora usando su hermano gemelo:

```python
import os

# Python elimina la configuración
os.system("nerve unassociate")
```

## ¿Qué pasa si me equivoco?

El error más común aquí es **olvidar importar `os`** antes de intentar usar `os.system()`. Si lo olvidas, Python se quejará diciendo: `NameError: name 'os' is not defined`. Esto es Python diciéndote: *"Me pides que hable con 'os', pero no me lo has presentado"*. ¡Siempre incluye `import os` arriba de tu receta!
