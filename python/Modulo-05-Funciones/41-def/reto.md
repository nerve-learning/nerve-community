# Reto 41: El Sistema de Alertas Cósmicas 🚀

Tu nave espacial está recibiendo múltiples advertencias, y estás cansado de escribir manualmente todo el formato de la alerta de peligro en la consola de la nave cada vez que un asteroide se acerca.

Vas a automatizar esto creando tu propio comando de alerta.

## 📝 Instrucciones

1. Crea un archivo llamado `reto.py`.
2. Usando la palabra mágica `def`, inventa una función llamada `alerta_peligro()`.
3. Dentro de tu función (con la indentación correcta), escribe al menos tres `print()` que muestren un mensaje de peligro muy llamativo (puedes usar emojis y símbolos como `!`, `*`, `[!]`).
4. Fuera de la función (sin indentación), simula que la nave está analizando un sector. Usa un bucle `for` o `while` (de los módulos anteriores) que se repita 3 veces.
5. En cada repetición del bucle, muestra un texto como `"Analizando sector..."` y luego **llama a tu función `alerta_peligro()`**.

### 🚦 Reglas Estrictas
- **Conceptos permitidos:** `def`, `print`, `for` o `while`.
- **Prohibido:** Poner texto directamente en tu bucle sin usar la función. Está prohibido usar argumentos o parámetros dentro de los paréntesis `()` de tu función (todavía no sabemos usarlos, así que déjalos vacíos).

## 🎯 Resultado Esperado en Terminal

Cuando ejecutes tu código, la terminal debería mostrar algo exactamente como esto:

```text
Analizando sector...
[!] ¡¡ALERTA ROJA!! [!]
[!] IMPACTO INMINENTE [!]
[!] PREPARAR ESCUDOS [!]

Analizando sector...
[!] ¡¡ALERTA ROJA!! [!]
[!] IMPACTO INMINENTE [!]
[!] PREPARAR ESCUDOS [!]

Analizando sector...
[!] ¡¡ALERTA ROJA!! [!]
[!] IMPACTO INMINENTE [!]
[!] PREPARAR ESCUDOS [!]
```

¡Demuestra que ya no eres un simple pasajero de la nave, sino el ingeniero principal! 🛠️
