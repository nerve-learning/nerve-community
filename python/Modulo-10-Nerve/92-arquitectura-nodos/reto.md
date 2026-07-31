# Reto 92: La Central de Alarmas 🚨

Ya sabes cómo escuchar. Ahora, vamos a crear un "Nodo de Seguridad" que se quede eternamente vigilando la red de Nerve en busca de cualquier señal de peligro.

## Instrucciones Paso a Paso

1. Crea un archivo llamado `alarma.py`.
2. Importa `NexusClient` desde `nerve`.
3. Crea tu cliente y conéctate a la red con el nombre (gafete) `"central_alarmas"`.
4. Define una función (tu recepcionista) llamada `vigilante`. Esta función debe recibir un parámetro (ej. `datos`).
5. DENTRO de la función `vigilante`, verifica si existe la llave `"peligro"` dentro del diccionario `datos`. (Pista: `if "peligro" in datos:` o usando `.get()`).
6. DENTRO del `if`, si el `"peligro"` es `"fuego"`, imprime `"¡ALERTA ROJA! Activando aspersores de agua."`.
7. Si el `"peligro"` es `"ladron"`, imprime `"¡ALERTA AZUL! Llamando a la policía local."`.
8. Si no hay peligro, o es otra cosa, imprime `"Situación normal. Seguimos vigilando."`.
9. DE VUELTA al flujo principal de tu código (fuera de la función), dile a tu cliente que escuche usando `listen()` y pasándole la receta de tu `vigilante`.
10. Usa un `input()` al final con el mensaje `"Central de Alarmas activada. Esperando reportes...\n"` para evitar que el programa se cierre.

## 📜 Reglas de la Misión

**🟢 Conceptos Permitidos:**
- Funciones `def` (Módulo 05).
- Condicionales `if`, `elif`, `else` (Módulo 02).
- Diccionarios `{}` (Módulo 03).
- `input()` y `print()`.
- `NexusClient`, `.connect()`, `.listen()`

**🔴 Prohibido:**
- Ponerle paréntesis a tu función dentro del `.listen()`.
- Usar clases u objetos complejos.
- Olvidar que Nerve necesita el comando `nerve start` corriendo en otra terminal.

## 🏆 Resultado Esperado en la Terminal

Al ejecutar `alarma.py`, tu nodo se quedará congelado esperando.

```text
Central de Alarmas activada. Esperando reportes...
```

*Si usaras OTRO script (como el del nivel 91) para enviarle un diccionario `{"peligro": "fuego"}` a `"central_alarmas"`, en esta terminal debería aparecer automáticamente:*

```text
¡ALERTA ROJA! Activando aspersores de agua.
```
