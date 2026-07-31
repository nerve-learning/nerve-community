# Reto 107: El Regalo de Cumpleaños 🎂

Has programado un script en Python para enviarle un regalo digital a tu mejor amigo. Quieres que el proceso sea lo más interactivo posible, para que él mismo tenga que introducir la clave correcta.

## 📝 Instrucciones

Crea un archivo llamado `reto.py` y escribe código que realice estos pasos:

1. Crea una carpeta llamada `regalo`.
2. Dentro, crea un archivo que se llame `mensaje.txt` con el texto "¡Feliz Cumpleaños!".
3. Usa `nerve pack` para proteger la carpeta `regalo` en un archivo llamado `regalo_seguro.nrv`, usando la contraseña `"pastel"`.
4. Borra la carpeta original `regalo` usando un comando de terminal (para que solo quede el archivo `.nrv`). *Pista: puedes usar `rm -rf regalo` si estás en Linux/Mac, o similar*.
5. Imprime un mensaje bonito en pantalla invitando a tu amigo a abrir su regalo.
6. Usa `nerve open` para que el script se pause y le pida a tu amigo que introduzca su contraseña interactivamente.
7. Al final, ejecuta el comando `nerve unassociate` para dejar la computadora limpia y ordenada, demostrando que puedes deshacer la vinculación.

### 🛑 Reglas Estrictas
* **Conceptos permitidos**: `import os`, variables de texto, funciones `print()` y `os.system()`.
* **Prohibido**: Pasarle la variable `NERVE_NRV_PASSWORD=` al comando `nerve open` en el paso 6. El objetivo de este reto es forzarte a escribir la clave con tus propios deditos en la terminal durante la ejecución.

### 🎯 Resultado Esperado en Terminal
Cuando ejecutes tu código, deberías ver la creación del paquete y luego tu programa se detendrá esperando acción. Si escribes "pastel", continuará hasta el final:

```text
Preparando tu regalo...
¡Regalo envuelto en regalo_seguro.nrv!
Amigo, ¡es hora de abrir tu regalo! Por favor escribe la contraseña.
> [Aquí Nerve te pedirá la contraseña. Tú escribes "pastel"]
¡Felicidades, regalo abierto!
Limpiando configuración (desasociando)...
Terminado.
```
