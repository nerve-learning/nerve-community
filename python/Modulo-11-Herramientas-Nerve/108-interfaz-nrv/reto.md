# Reto 108: El Centro de Comando 💻

Eres el supervisor nocturno de la red y te han pedido que programes el panel de monitoreo oficial para que los operadores puedan vigilar el tráfico de datos desde la terminal.

## 📝 Instrucciones

Crea un archivo llamado `reto.py` y escribe código que realice estos pasos:

1. Imprima un mensaje formal: "Iniciando Centro de Comando Local...".
2. Imprima un aviso para los operadores: "Para salir de este modo y volver a casa, presione Ctrl + C".
3. Use el módulo `os` para ejecutar el comando `nerve monitor`. 
4. Después de la orden de `os.system()`, imprime una línea final que diga: "Centro de comando cerrado. Buen trabajo.".

### 🛑 Reglas Estrictas
* **Conceptos permitidos**: `import os`, `os.system()`, y la función `print()`.
* **Prohibido**: Ejecutar `nerve start` en este código (no queremos encender el Hub de mensajes aquí, solo queremos ver el panel de monitoreo). Y por supuesto, mantén todo en un solo archivo plano sin trucos extraños.

### 🎯 Resultado Esperado en Terminal
Cuando ejecutes tu código, deberías ver los primeros prints, seguidos inmediatamente de un cambio visual extremo en tu terminal (el panel hacker de Nerve con tablas y colores).

Cuando decidas que tu turno terminó, harás clic en la terminal, presionarás **Ctrl + C**, el panel desaparecerá y verás tu último mensaje:

```text
Iniciando Centro de Comando Local...
Para salir de este modo y volver a casa, presione Ctrl + C
> [La pantalla se llena de tablas y colores del Monitor de Nerve]
> [Tú presionas Ctrl + C]
Centro de comando cerrado. Buen trabajo.
```
