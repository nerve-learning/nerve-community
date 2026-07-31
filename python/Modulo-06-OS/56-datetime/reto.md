# Reto 56: El Diario Automático 📓

Vas a crear un programa que escriba tus pensamientos en un archivo de texto, pero que tenga el "poder" de agregarle automáticamente la fecha y la hora en la que lo escribiste. ¡Así tendrás una bitácora perfecta!

### Instrucciones paso a paso:

1. Importa la caja del tiempo (`datetime`).
2. Crea una función (con `def`) llamada `escribir_diario(mensaje)` que reciba un texto.
3. Dentro de la función, captura el momento actual usando `datetime.datetime.now()` y guárdalo en una variable llamada `momento`.
4. Extrae el día, el mes, el año, la hora y los minutos en variables separadas.
5. Abre (o crea) un archivo llamado `"mi_diario.txt"` usando tu guardián `with open(...)`. Recuerda abrirlo en modo **Agregar** (la letra `"a"`) para no borrar las entradas de días anteriores. ¡Pon `newline=""` si estás en Windows para evitar saltos raros!
6. Adentro del bloque `with`, usa la herramienta de escritura (`.write()`) para guardar el título de la fecha. 
   **¡ATENCIÓN!**: Como `.write()` solo acepta texto (letras), y tus fechas son números, deberás usar la función `str(numero)` para convertirlos a texto y poder sumarlos con el signo `+`. 
   Escribe algo así: `"--- Entrada del día: " + str(dia) + "/" + str(mes) + "/" + str(anio) + " ---\n"`
7. Usa otro `.write()` para guardar el `mensaje` que recibiste por parámetro. Asegúrate de sumarle un salto de línea (`+ "\n"`) al final para que la siguiente entrada no se pegue.
8. Afuera de la función, llámala pasándole el mensaje: `"¡Hoy aprendí a viajar en el tiempo con Python!"`.
9. (Opcional): Espera un minuto, cambia el mensaje de la función y vuelve a correr el programa. ¡Abre tu archivo y ve cómo se van acumulando con diferentes horas!

---

### 🟢 Conceptos Permitidos (Lo único que puedes usar)
* `import datetime`
* Reloj: `datetime.datetime.now()`
* Etiquetas pasivas: `.year`, `.month`, `.day`, `.hour`, `.minute`
* Convertir a texto (`str(numero)`) y unir textos con suma (`+`)
* Crear/Agregar a archivos (`with open(archivo, "a") as apodo:`)
* Escribir texto (`apodo.write(...)`)
* Funciones (`def`) y parámetros.

### 🔴 Prohibido
* Usar librerías externas o formateadores de fecha avanzados como `.strftime()` (¡hoy queremos armarlo pieza por pieza con nuestras manos!).
* Usar el modo escritura destructiva `"w"` (¡no queremos borrar todo nuestro diario!).

---

### 🎯 Resultado esperado
*(No verás nada en la terminal. El resultado estará dentro del archivo "mi_diario.txt" que tu programa va a crear. Debería verse así, pero con TU hora local actual):*

```text
--- Entrada del día: 29/7/2026 ---
¡Hoy aprendí a viajar en el tiempo con Python!
```

¡Mucha suerte escribiendo tu bitácora temporal! Recuerda no ponerle paréntesis a los números del año o mes si Python te lanza el error del número actuante.
