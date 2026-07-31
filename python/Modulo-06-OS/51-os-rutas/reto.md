# Reto 51: El Inspector de Tesoros 🔎

Has llegado a una habitación nueva del edificio y necesitas clasificar lo que hay en ella. Tu misión es crear un programa que mire todos los archivos de la carpeta actual y determine cuáles son "tesoros" y cuáles son "basura".

### Instrucciones paso a paso:

1. Escribe la palabra mágica para traer las herramientas del sistema operativo.
2. Averigua en qué dirección estás parado y guárdala en una variable llamada `ruta_secreta`.
3. Imprime tu ruta secreta para confirmar dónde estás.
4. Usa la herramienta para ver qué cosas hay a tu alrededor y guárdalas en una lista llamada `inventario`.
5. Crea una función (usando `def`) llamada `inspeccionar_tesoros(lista_de_cosas)` que reciba una lista como parámetro.
6. Dentro de la función, usa un bucle `for` para analizar cada cosa de la lista.
7. **La regla del tesoro**: Usando un condicional (`if`), verifica si la primera letra del nombre del objeto es la letra `"e"` (recuerda que puedes ver la primera letra de un texto usando índices, como `palabra[0] == "e"`).
8. Si empieza con `"e"`, imprime: `"¡Tesoro especial encontrado: [nombre del archivo]!"`
9. Si NO empieza con `"e"`, imprime: `"Solo es basura: [nombre del archivo]"`
10. Finalmente, llama a tu función pasándole tu lista `inventario` como parámetro.

---

### 🟢 Conceptos Permitidos (Lo único que puedes usar)
* `import os`
* `os.getcwd()`
* `os.listdir()`
* Asignación de variables (`=`)
* Listas y bucles (`for elemento in lista:`)
* Funciones (`def nombre_funcion(parametro):`)
* Condicionales (`if` / `else`)
* Índices para sacar letras (`texto[0]`)

### 🔴 Prohibido
* Copiar y pegar código de internet.
* Usar módulos que no sean `os`.
* Usar herramientas que no hemos visto como list comprehensions o conceptos avanzados de rutas (`os.path`, `pathlib`).

---

### 🎯 Resultado esperado en la terminal
*(Nota: El orden exacto de los archivos puede variar según tu computadora, pero el formato debe verse así)*

```text
Mi ruta secreta es: /ruta/hacia/tu/carpeta/51-os-rutas
Solo es basura: teoria.md
¡Tesoro especial encontrado: ejemplo.py!
Solo es basura: README.md
Solo es basura: reto.md
```

¡Mucha suerte, inspector! Recuerda dar pasitos pequeños y probar tu código constantemente.
