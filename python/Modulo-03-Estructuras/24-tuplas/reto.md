# Reto 24: El Sistema de Seguridad 🚨

Estás programando el sistema de seguridad de un museo. Necesitas guardar el código secreto de la bóveda y la ubicación de las cámaras. ¡Esta información es tan crítica que ningún hacker (ni tú por accidente) debe poder modificarla!

## Instrucciones

1. Crea un archivo llamado `reto.py`.
2. Crea una variable llamada `codigo_boveda` que sea una **Tupla** con 3 números (por ejemplo: `7`, `4`, `1`).
3. Crea una variable llamada `estado_camaras` que sea una **Tupla** con dos textos: `"Encendidas"`, `"Grabando"`.
4. Imprime el mensaje: `"--- ESTADO DEL SISTEMA ---"`.
5. Imprime la tupla `codigo_boveda`.
6. Extrae e imprime SOLO la primera palabra del estado de las cámaras (el índice `0`) de tu tupla `estado_camaras`. (Agrega un texto que diga `"Estado de cámara 1:"` antes).

### Conceptos Permitidos
- Tuplas (creación con paréntesis `()`).
- Acceso por índice (lectura con corchetes `[]`).
- La función `print()`.

### Conceptos PROHIBIDOS
- Usar corchetes `[]` para crear las variables iniciales (eso haría que fueran Listas, ¡y los ladrones podrían modificarlas!).
- Intentar usar `.append()` o `.remove()`.

## Resultado Esperado en la Terminal

Al ejecutar tu código, la terminal debería mostrar EXACTAMENTE esto (tus números pueden variar):

```text
--- ESTADO DEL SISTEMA ---
(7, 4, 1)
Estado de cámara 1:
Encendidas
```

¡Felicidades, el museo está a salvo!
