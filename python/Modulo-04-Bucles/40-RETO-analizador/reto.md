# Reto 40: El Analizador de Sensores 🌡️

¡Te han contratado en la fábrica central! Tu trabajo es escribir un programa que analice un registro continuo de temperaturas que ha enviado un sensor de una máquina.

El objetivo es clasificar estas temperaturas en tres estados: "Normal", "Alerta" y "Peligro". Y lo más importante: si la máquina se calentó demasiado, el programa debe abortar el análisis de inmediato.

### Instrucciones paso a paso:
1. Crea una lista llamada `registro_temperaturas` con estos números exactos en este orden: `[22, 25, 31, 15, 29, 50, 20, 22]`
2. Crea un diccionario llamado `reporte_maquina` que tenga tres llaves (textos) empezando en 0 (números): `"Normal": 0`, `"Alerta": 0`, y `"Peligro": 0`.
3. Imprime el mensaje: `"--- Iniciando análisis del motor ---"`.
4. Crea un bucle `for` que recorra cada número en la lista `registro_temperaturas` usando la variable temporal `temp`.
5. Dentro del bucle, haz las siguientes preguntas (condicionales):
   - Si `temp` es **menor o igual a 29**: Suma 1 a la llave `"Normal"` del diccionario `reporte_maquina`.
   - Si `temp` está **entre 30 y 49** (puedes usar un `elif` sabiendo que ya no es menor o igual a 29): Suma 1 a la llave `"Alerta"`.
   - Si `temp` es **exactamente igual a 50**: Imprime `"¡FUSIÓN DEL NÚCLEO DETECTADA! Apagando..."`, suma 1 a la llave `"Peligro"`, y usa un comando para **romper y destruir el bucle inmediatamente**.
6. Fuera del bucle, imprime `"--- Análisis finalizado ---"`.
7. Fuera del bucle, imprime el diccionario `reporte_maquina`.

### Reglas estrictas:
- **Conceptos permitidos**: Listas, Diccionarios, bucles `for`, `if`, `elif`, matemáticas básicas de suma (`+ 1`), `break`, función `print`.
- **Prohibido**: Usar funciones prefabricadas que cuenten automáticamente (como `count()`), no hemos aprendido eso aún. Debes sumar `+ 1` manualmente al diccionario.

### Resultado esperado en la terminal:
```text
--- Iniciando análisis del motor ---
¡FUSIÓN DEL NÚCLEO DETECTADA! Apagando...
--- Análisis finalizado ---
{'Normal': 4, 'Alerta': 1, 'Peligro': 1}
```
*(Nota: Solo hay 4 normales y 1 alerta porque el bucle se detuvo al llegar al número 50. Los últimos dos números de la lista (20 y 22) nunca fueron leídos por culpa del apagado de emergencia).*
