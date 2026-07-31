# Reto 105: El Mensajero Cifrado 🕵️

Te han contratado como mensajero de máxima seguridad. Tu misión es enviar un reporte confidencial, asegurarte de que está protegido y luego verificar que el destinatario pueda leerlo.

## 📝 Instrucciones

Crea un archivo llamado `reto.py` y escribe código que haga exactamente lo siguiente:

1. Crea una carpeta llamada `mision`.
2. Dentro de esa carpeta, crea un archivo llamado `coordenadas.txt` que diga "Latitud 40, Longitud -3". (Recuerda que puedes usar `os.system` o abrir un archivo normal en Python con `open()`, ambas opciones son válidas).
3. Usa el comando `nerve pack` para empacar la carpeta `mision` en un archivo llamado `paquete_seguro.nrv`. La contraseña DEBE ser `"agente007"`.
4. Finalmente, usa `nerve unpack` para abrir `paquete_seguro.nrv` y volcar su contenido en una carpeta llamada `base_aliada`.

### 🛑 Reglas Estrictas
* **Conceptos permitidos**: `import os`, variables de texto, funciones `print()`, y `os.system()`.
* **Prohibido**: Usar librerías raras de criptografía (nada de importar `cryptography`), clases o funciones complejas. Mantén el código lineal y simple, como en nuestra lección.

### 🎯 Resultado Esperado en Terminal
Cuando ejecutes tu script, debería verse algo así (los mensajes de print los eliges tú, pero las acciones de Nerve se verán en la pantalla automáticamente cuando uses os.system):

```text
Preparando la misión...
Carpeta creada.
Empacando con Nerve...
Desempacando en la base...
Misión completada.
```
*Y en tu carpeta de proyecto deberías ver las carpetas `mision`, `base_aliada` y el archivo `paquete_seguro.nrv`.*
