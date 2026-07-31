# Reto 116: La Panadería Automática 🥖

Vas a construir una cadena de montaje (Pipeline) de 3 pasos para hacer pan usando la magia de Nerve.

La secuencia es: `Amasadora` -> `Horno` -> `Vitrina`.

### 📝 Instrucciones:

1. Crea un archivo de Python, importa `NexusHub`, `NexusClient` y `time`.
2. Enciende tu `NexusHub`.
3. Crea 3 clientes y conéctalos con los nombres: `"amasadora"`, `"horno"` y `"vitrina"`.
4. Crea la función para el **Horno**. Debe recibir el payload, imprimir que está horneando, cambiar la etiqueta `"estado"` del payload a `"Pan Horneado"`, y enviarlo (usando `send`) a la `"vitrina"`.
5. Crea la función para la **Vitrina**. Debe recibir el payload, imprimir el mensaje de éxito y mostrar cómo quedó el payload final. No envía nada a nadie (es el final de la cadena).
6. Pon a escuchar al `horno` y a la `vitrina` usando `.listen()`.
7. Arranca el pipeline: Usa la `amasadora` para crear un diccionario `{"ingredientes": "Harina, Agua y Levadura", "estado": "Masa Cruda"}` y envíalo (`send`) directamente al `"horno"`.
8. Usa `time.sleep(3)` al final para darles tiempo de trabajar antes de cerrar todo.

### ⛔ Reglas Estrictas:
* **Permitido**: Múltiples instancias de `NexusClient`, diccionarios, `.send()`, `.listen()`.
* **Prohibido**: Que el Horno hornee el pan y se olvide de enviárselo a la Vitrina (Callejón sin salida). 
* **Prohibido**: Enviar el pan de la Vitrina de regreso al Horno (Bucle de la muerte, pan quemado).

### 🎯 Resultado Esperado en la Terminal:
```text
🥣 [AMASADORA] Mezclando ingredientes y enviando masa al horno...
🔥 [HORNO] Recibi Masa Cruda. Horneando a 200 grados...
🍞 [VITRINA] ¡Pan fresco listo para la venta! {'ingredientes': 'Harina, Agua y Levadura', 'estado': 'Pan Horneado'}
```
*(Nota: Añade tus propios `print` en la amasadora y el horno para que se parezca al resultado esperado)*
