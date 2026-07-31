# Reto 55: El Falsificador de Arte 🎨

Eres un espía internacional infiltrado en un museo. Tu objetivo es hacer una copia exacta de la pintura original de la Mona Lisa para dejarla en su lugar, ¡y luego esconder la original cambiándole el nombre!

### Instrucciones paso a paso:

1. Importa la caja de herramientas de mudanzas (`shutil`).
2. Crea una función (con `def`) llamada `falsificar_arte(nombre_original, nombre_falso)` que reciba esos dos parámetros de texto.
3. Dentro de la función, usa tu herramienta de clonación (`.copy()`) para hacer una copia del archivo `nombre_original` y que se guarde con el nombre `nombre_falso`.
4. Ahí mismo, dentro de la función, imprime tu mensaje malvado: `"¡Muajaja! He creado una copia falsa llamada: [nombre_falso]"`. Sustituye `[nombre_falso]` por la variable de tu parámetro.
5. **Fuera de la función**, vamos a preparar el terreno: usa tu guardián `with open(...)` en modo `"w"` para crear el archivo del museo llamado `"monalisa.txt"`. Escribe adentro el texto: `"Soy la pintura original"`.
6. Ahora sí, llama a tu función `falsificar_arte()` pasándole `"monalisa.txt"` como el original y `"monalisa_falsa.txt"` como la copia.
7. Corre el código para ver tu plan maestro en acción.
8. **(Bono Opcional)**: Abajo de tu llamada a la función, usa la herramienta de movimiento (`.move()`) para cambiarle el nombre a `"monalisa.txt"` (la original) y esconderla llamándola `"cuadro_robado.txt"`.

---

### 🟢 Conceptos Permitidos (Lo único que puedes usar)
* `import shutil`
* Clonar: `shutil.copy(origen, destino)`
* Renombrar/Mover: `shutil.move(origen, destino)`
* Crear/Escribir archivos (`with open(...)`)
* Funciones (`def`) y parámetros.
* Imprimir a la terminal (`print()`)

### 🔴 Prohibido
* Usar `os.rename()` (¡hoy es el día del camión de mudanzas `shutil`!).
* Copiar y pegar código de internet.
* Olvidar crear el archivo "monalisa.txt" antes de intentar copiarlo (recuerda el error del fantasma).

---

### 🎯 Resultado esperado en la terminal
*(Solo verás el mensaje malvado. El trabajo real de la copia y el renombramiento sucederá silenciosamente en la carpeta de tu computadora).*

```text
¡Muajaja! He creado una copia falsa llamada: monalisa_falsa.txt
```

¡Es hora de perpetrar el atraco del siglo!
