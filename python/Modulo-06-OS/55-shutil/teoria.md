# Copiar y Mover con `shutil`

Vimos que `os` era como nuestros "ojos" para ver qué hay en las habitaciones del edificio de tu computadora.
Ahora te presento a **`shutil`** (abreviatura de *Shell Utilities*). Piensa en `shutil` como un camión de mudanzas o unas manos muy fuertes. Su trabajo principal es agarrar las cajas (archivos) y copiarlas o moverlas de lugar.

---

### Anatomía de los nuevos símbolos

Para tener acceso al camión de mudanzas, la palabra mágica es:
```python
import shutil
```

#### 1. Clonar (Copiar) Archivos
```python
shutil.copy("carta.txt", "copia_carta.txt")
```
* **`shutil`**: La caja de herramientas de mudanzas.
* **`.copy()`**: Es la acción de "Clonar". Necesita que le des **dos** ingredientes exactos separados por una coma:
  * **El Origen (`"carta.txt"`)**: ¿Cuál es el archivo original que quiero clonar?
  * **El Destino (`"copia_carta.txt"`)**: ¿Qué nombre quiero que tenga mi nueva copia?

#### 2. Mover / Renombrar Archivos
```python
shutil.move("viejo.txt", "nuevo.txt")
```
* **`.move()`**: Es la acción de "Mover". Al igual que `copy`, toma un Origen y un Destino.
* **El gran truco de Mover**: Si le das un nombre de destino nuevo que está en la misma habitación (carpeta), la herramienta `.move()` simplemente **le cambia el nombre** al archivo original. ¡El archivo viejo desaparece y reaparece instantáneamente con su nuevo nombre!

---

### ⚠️ ¿Qué pasa si me equivoco?

**El error del fantasma**
Si le pides a tu camión de mudanzas que copie o mueva algo que no existe, Python se asustará:

```text
FileNotFoundError: [Errno 2] No such file or directory: 'fantasma.txt'
```

**¿Qué significa esto en lenguaje humano?**
Python te está diciendo: *"Me pediste que tome la caja 'fantasma.txt' con mis manos, pero fui a buscarla y no hay nada ahí. ¡No puedo mudar cosas invisibles!"*

**¿Cómo lo soluciono?**
Siempre asegúrate de que el archivo que pones de **Origen** exista en la vida real antes de intentar copiarlo o moverlo. Si es necesario, ¡créalo tú mismo primero usando el modo `"w"` que aprendimos en el nivel 53!
