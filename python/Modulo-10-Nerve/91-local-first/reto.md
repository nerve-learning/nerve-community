# Reto 91: El Mensajero Secreto 🕵️‍♂️

¡Felicidades! Has descubierto cómo funciona la red local. Ahora, la Agencia Espacial Local necesita tus servicios para transmitir un paquete de datos súper secreto a la base central de comando, sin que salga de tu computadora.

## Instrucciones Paso a Paso

1. Crea un archivo nuevo en esta carpeta llamado `mensajero.py`.
2. Importa `NexusClient` desde la librería `nerve`. No olvides importar `time` también.
3. Imprime en pantalla `"Iniciando transmisor..."`.
4. Construye tu cliente de Nerve y conéctalo poniéndote el nombre (gafete) `"agente_007"`.
5. Imprime en pantalla `"Conectado como agente_007."`.
6. Crea un diccionario llamado `informe_secreto` que contenga:
   - `"mision"`: (el nombre que quieras darle a tu misión)
   - `"objetivo"`: (qué quieres lograr)
   - `"nivel_peligro"`: (un número del 1 al 10)
7. Imprime en pantalla `"Enviando informe secreto al cuartel_general..."`.
8. Usa tu cliente para enviar un mensaje DIRECTO (`send`) al destino `"cuartel_general"`. El paquete debe ser tu diccionario `informe_secreto`.
9. Imprime en pantalla `"Informe enviado."`.
10. Imprime en pantalla `"Avisando a la red local..."`.
11. Usa tu cliente para enviar un mensaje a TODOS (`broadcast`) con un diccionario que contenga la llave `"aviso"` y el texto `"Misión cumplida. Agente fuera."`.
12. Usa `time.sleep(1)` para darle tiempo a los cables de enviar los paquetes antes de apagar el programa.
13. Imprime en pantalla `"Misión cumplida. Agente fuera."`.

## 📜 Reglas de la Misión

**🟢 Conceptos Permitidos:**
- `import`, `time.sleep()`
- Diccionarios `{}` y variables `=`.
- `print()`
- `NexusClient`, `.connect()`, `.send()`, `.broadcast()`

**🔴 Prohibido:**
- Usar `requests` (nada de internet externo).
- Crear clases propias (POO).
- Funciones complejas o `while`/`for` (queremos que sea un código lineal y súper directo).

## 🏆 Resultado Esperado en la Terminal

Asegúrate de tener corriendo `nerve start` en OTRA terminal antes de ejecutar tu reto, o no funcionará. Al ejecutar tu `mensajero.py`, deberías ver exactamente esto:

```text
Iniciando transmisor...
Conectado como agente_007.
Enviando informe secreto al cuartel_general...
Informe enviado.
Avisando a la red local...
Misión cumplida. Agente fuera.
```
