# Nivel 57: El Controlador de Títeres (`subprocess`)

Hasta ahora, tus programas en Python hacían todo por sí mismos. Leían archivos, calculaban cosas y mostraban resultados. Pero, ¿qué pasa si tu programa necesita que *otro* programa haga un trabajo por él?

Imagina que tu código de Python es un director de orquesta. A veces, en lugar de tocar un instrumento, solo necesita apuntar a un músico (otro programa) y decirle: *"Oye tú, haz esto y dime cuando termines"*.

Para eso usamos el módulo `subprocess`. Nos permite crear **subprocesos**: programas hijos que nacen, trabajan y mueren bajo las órdenes de tu programa principal.

## El Concepto: `subprocess.run()`

Para ejecutar otro programa, usamos la función `run()` (que significa "correr" o "ejecutar").

```python
import subprocess

resultado = subprocess.run(["python", "--version"], capture_output=True, text=True)
```

Desmontemos esta instrucción pieza por pieza, porque tiene varios elementos nuevos:

### 1. La Lista del Comando: `["python", "--version"]`
Cuando escribes en tu terminal, usas espacios: `python --version`. 
Pero a `subprocess` no le gustan los textos largos con espacios, porque se puede confundir si un nombre de archivo tiene un espacio en blanco. 
Para evitar errores, le damos el comando desarmado en una **lista** `[]`:
- El primer elemento (`"python"`) es **quién** va a trabajar (el programa).
- Los elementos siguientes (`"--version"`) son **qué** queremos que haga (los argumentos).

### 2. Atrapando las palabras: `capture_output=True`
Por defecto, si el otro programa imprime algo, saldrá directo a tu pantalla, mezclándose con los mensajes de tu programa. 
Al usar `capture_output=True` (atrapar salida = Verdadero), le decimos a Python: *"Ponle una mordaza al programa hijo. Todo lo que intente decir, guárdalo en secreto y entrégamelo a mí"*.

### 3. Hablando nuestro idioma: `text=True`
Las computadoras se comunican internamente en un formato crudo llamado "bytes" (ceros y unos empaquetados). Si no ponemos esta regla, el programa hijo nos devolverá un texto extraño lleno de símbolos raros como `b'...'`.
Al poner `text=True`, le decimos: *"Traduce la respuesta del programa hijo a texto normal que los humanos podamos leer"*.

### 4. Leyendo la respuesta: `.stdout`
Cuando `subprocess.run()` termina, no te da el texto directamente. Te da un "paquete completo" de información sobre cómo le fue al programa hijo (su expediente).
Para leer lo que el programa hijo imprimió exitosamente, abrimos ese paquete y buscamos la propiedad `.stdout` (que significa *Standard Output* o "Salida Estándar").

```python
print(resultado.stdout)
```

## ¿Por qué esto es poderoso?
Con `subprocess`, tu script de Python ya no está aislado. Puede mandar correos usando herramientas del sistema, comprimir archivos usando otros programas, o incluso abrir el navegador web. Tu código de Python se convierte en un cerebro que coordina a toda tu computadora.
