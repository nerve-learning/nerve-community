# Reto 110: El Limpiador (Desinstalador) 🧹

Todo buen programa que configura algo en la computadora del usuario, debe saber cómo desconfigurarlo. A esto se le llama ser un programador "educado".

Tu misión es crear un script llamado `desinstalador.py` que elimine la asociación de los archivos `.nrv` y borre el archivo de prueba que creamos en el ejemplo.

## Instrucciones:

1. Crea un archivo llamado `desinstalador.py`.
2. Importa el módulo necesario para hablar con el sistema operativo.
3. Muestra un mensaje amigable al usuario diciendo que estás empezando a limpiar.
4. Usa `os.system()` para ejecutar el comando de Nerve que **elimina** la asociación (`nerve unassociate`).
5. (Opcional) Usa un comando de terminal para borrar el archivo `mi_caja_fuerte_de_prueba.nrv`. *(Pista: en Windows es `del nombre_archivo` y en Linux/Mac es `rm nombre_archivo`. Si no quieres complicarte, puedes pedirle al usuario que lo borre a mano).*
6. Despídete amablemente del usuario.

### Conceptos Permitidos:
- Funciones (`print`)
- Módulo OS (`import os`, `os.system()`)

### Conceptos Prohibidos:
- Librerías externas como `shutil` o `pathlib`
- Bloques `try/except` (aún no los conocemos a fondo)

### Resultado Esperado en la Terminal:
```text
--- Iniciando el Desinstalador ---
Eliminando configuración de Nerve...
[Mensajes automáticos de nerve unassociate aquí...]
¡Limpieza completada! Gracias por usar nuestro software.
```
