# Reto 109: La Fábrica de Secretos 🏭

Has sido ascendido a Ingeniero de Automatización. Tu trabajo ya no es hacer cosas a mano, sino crear máquinas (código) que hagan el trabajo por ti. 

Debes crear un programa que automáticamente invente una clave, empiece a procesar archivos y verifique que todo funcionó, todo por sí solo en milisegundos.

## 📝 Instrucciones

Crea un archivo llamado `reto.py` y programa estos pasos:

1. Atrapa una llave de alta seguridad (modo `random`) usando `os.popen().read().strip()`. Guárdala en una variable.
2. Imprímela en pantalla con un mensaje que diga "La llave de hoy es: [TU LLAVE]".
3. Crea una carpeta llamada `produccion` y pon un archivo adentro usando `os.system()` (como aprendimos a hacer con `mkdir` y `echo`).
4. Empaca la carpeta `produccion` en un archivo llamado `producto_final.nrv` usando la variable donde atrapaste la llave. (Usa `os.system` para esta tarea, ya que no necesitamos atrapar la respuesta de `nerve pack`, solo queremos que lo haga).
5. Desempaca `producto_final.nrv` en una carpeta de prueba llamada `control_calidad`, usando la **MISMA** variable de tu llave. 

### 🛑 Reglas Estrictas
* **Conceptos permitidos**: `import os`, `os.system()`, `os.popen().read().strip()`, variables de texto (f-strings) y `print()`.
* **Prohibido**: Escribir la contraseña a mano en el código. ¡La contraseña debe venir 100% de la terminal a través de `os.popen`!

### 🎯 Resultado Esperado en Terminal
Cuando ejecutes tu código, deberías ver algo así:

```text
Iniciando fábrica...
La llave de hoy es: 3b#F9x!ZpQ8L@2
Carpeta creada.
Empacando producto...
Desempacando para control de calidad...
¡Todo funciona perfectamente!
```
*Revisa tus carpetas después de ejecutarlo para comprobar que `produccion`, `control_calidad` y `producto_final.nrv` existen.*
