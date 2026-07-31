# Teoría: El Loro Súper Inteligente

Un LLM no es magia, es pura estadística y probabilidad. Imagina una caja gigante llena de millones de textos. Cuando le haces una pregunta, la caja no "busca" la respuesta, simplemente calcula: *"Dado el texto que me acaban de dar, ¿cuál es la palabra más probable que sigue?"*.

Para trabajar con ellos, usamos tres conceptos clave:

1. **El Modelo**: Es el cerebro pre-entrenado (ej. GPT-4, Gemini).
2. **El Prompt**: Es el texto de entrada. La instrucción que le damos.
3. **El Completion**: Es la respuesta, el texto generado.

## Anatomía de una interacción

En la vida real, interactuamos con un LLM enviando un mensaje a través de internet (usando lo que aprendimos en el Módulo 07 de APIs).

```python
mensaje = "Traduce 'Hola' al inglés" # <- Esto es el PROMPT
respuesta = consultar_llm(mensaje)   # <- Esto envía el prompt al MODELO
print(respuesta)                     # <- Esto es el COMPLETION ("Hello")
```

- `mensaje = "..."`: Aquí guardamos nuestra instrucción en formato de texto.
- `consultar_llm()`: Representa la conexión (generalmente a través de internet) hacia los servidores donde vive el LLM.
- `respuesta`: La variable donde guardamos el texto que el modelo nos devuelve.

## ¿Qué pasa si me equivoco?

**Error común**: Dar un *Prompt* demasiado vago o ambiguo.
*Síntoma*: El LLM te responde cosas genéricas, alucinaciones (inventa datos) o algo que no pediste.
*Solución*: Debes ser muy específico en el prompt. En lugar de `"Resume el texto"`, usa `"Resume el siguiente texto en 3 puntos clave usando viñetas:"`. A esta habilidad se le llama **Prompt Engineering**.
