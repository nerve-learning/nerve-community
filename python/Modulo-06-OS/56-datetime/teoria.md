# Fechas y Horas con `datetime`

Tu computadora tiene un reloj maestro interno. Para poder leerlo y extraer sus datos, usamos una nueva caja de herramientas llamada `datetime` (fecha y hora en inglés).

Cuando le preguntamos a Python la hora actual, nos devuelve un "paquete" con muchísima información junta: año, mes, día, hora, minutos, segundos ¡e incluso milisegundos! Como a nosotros los humanos nos gusta leer las cosas por separado, usaremos el punto (`.`) para abrir ese paquete y sacar solo las gavetas que nos interesan.

---

### Anatomía de los nuevos símbolos

Esta es la forma clásica de leer el tiempo en Python:

```python
import datetime

momento_actual = datetime.datetime.now()

mi_anio = momento_actual.year
mi_hora = momento_actual.hour
```

* **`import datetime`**: Trae la caja principal de fechas y horas.
* **`datetime.datetime`**: Adentro de la caja `datetime`, hay un compartimento especial que curiosamente también se llama `datetime`. Este compartimento maneja específicamente las fechas mezcladas con horas.
* **`.now()`**: Es la acción (herramienta) que significa "AHORA". Lleva paréntesis `()` porque es una orden activa: le estamos diciendo a Python "¡Calcula exactamente qué hora es en este preciso milisegundo y devuélvemela!".
* **`momento_actual.year`**: Tomamos el paquete de tiempo que guardamos, y usamos el punto (`.`) para mirar dentro y sacar la etiqueta del año (`year`). **¡Presta mucha atención! No lleva paréntesis al final**. No es una acción, es simplemente un cajón donde ya estaba guardado el número del año. (Otras etiquetas útiles: `.month`, `.day`, `.hour`, `.minute`, `.second`).

---

### ⚠️ ¿Qué pasa si me equivoco?

**El error del número actuante**
Imagina que te confundes y crees que pedir el año es una acción, así que le pones paréntesis: `momento_actual.year()`. Python te lanzará este error:

```text
TypeError: 'int' object is not callable
```

**¿Qué significa esto en lenguaje humano?**
Python se está rascando la cabeza y dice: *"Oye, la etiqueta `year` guarda un simple número entero (`int`), por ejemplo el 2024. ¡Pero le pusiste paréntesis, lo que significa que quieres que el número 2024 corra, salte o haga una acción! Los números no hacen cosas, ¡solo son números!"*.

**¿Cómo lo soluciono?**
Recuerda: las funciones o acciones (como `.now()` o `.read()`) llevan paréntesis porque hacen un trabajo. Los datos o propiedades guardadas (como `.year` o `.hour`) **no llevan paréntesis** porque solo te entregan información pasiva. Solo quítale los paréntesis.
