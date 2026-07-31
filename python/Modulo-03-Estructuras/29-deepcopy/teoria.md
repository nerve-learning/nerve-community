# Teoría: La Caja Fuerte de los Clones

Hasta ahora, todo lo que hemos usado (`print`, `int`, `len`, `type`) viene incluido por defecto cada vez que abres Python. Es como tu cinturón de herramientas básico.

Pero Python es gigante. Tiene herramientas para matemáticas avanzadas, para leer archivos, para conectarse a internet... ¡Si cargara todo al principio, sería lentísimo!

Por eso existen los **Módulos**. Un módulo es una caja de herramientas especial que está guardada en el almacén de Python. Si la necesitas, debes pedirla explícitamente al principio de tu código.

## 1. El comando `import`
Para traer una caja de herramientas externa, usamos la palabra especial `import`.

```python
import copy
```

### Anatomía del código
- `import`: Es una orden directa a la computadora. Significa: "Ve al almacén central de Python, busca esto y tráelo aquí para que yo lo pueda usar".
- `copy`: Es el nombre exacto de la caja de herramientas que queremos. `copy` significa "copiar" en inglés.

## 2. El método `deepcopy`
Una vez que trajimos la caja `copy`, podemos usar las herramientas que tiene adentro. Lo hacemos usando un punto `.`.

```python
import copy

clon_perfecto = copy.deepcopy(lista_original)
```

### Anatomía del código
- `copy`: Nuestra caja de herramientas importada.
- `.`: Significa "busca adentro de" la caja `copy`.
- `deepcopy()`: La herramienta específica que queremos usar. "Deep" significa profundo y "copy" copia.
- `lista_original`: Lo que ponemos entre los paréntesis `()` es lo que queremos que la máquina meta en la clonadora 3D.
- `=`: El resultado de esa clonación se guarda en la variable `clon_perfecto`.

### ¿Por qué "Profunda"?
`deepcopy` revisa tu lista. Si encuentra un texto, lo copia. Si encuentra un número, lo copia. **Si encuentra otra lista adentro**, hace una pausa, entra a esa lista interna, y copia todo lo de adentro, creando una lista interna totalmente nueva. Esto lo hace capa por capa, sin importar qué tan profundo estén anidadas las cosas. ¡Crea cajas nuevas para todo!

## ¿Qué pasa si me equivoco?

### Error 1: Olvidar el `import`
Si intentas usar `copy.deepcopy()` sin haber puesto `import copy` en la primera línea de tu archivo, la terminal te gritará:
`NameError: name 'copy' is not defined`
(Error de nombre: el nombre 'copy' no está definido).
La computadora te está diciendo: "¿Qué es 'copy'? ¡No tengo ninguna herramienta con ese nombre en mi cinturón básico!".

### Error 2: Escribir mal la orden
Poner `Import copy`, `import Copy`, o `copy.deepCopy()`. 
Recuerda que Python es extremadamente estricto y alérgico a las mayúsculas fuera de lugar. Todo este comando debe escribirse exactamente en minúsculas.
