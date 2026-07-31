import time

# ---------------------------------------------------------
# Simulación de un LLM (Modelo de Lenguaje Grande)
# En la vida real, esta función usaría la librería 'requests'
# para conectarse a OpenAI, Anthropic o Google.
# ---------------------------------------------------------

def consultar_llm(prompt):
    """
    Recibe un texto (prompt) y devuelve una respuesta (completion).
    Actúa como nuestra 'caja negra' inteligente.
    """
    print("🧠 El LLM está analizando los tokens y prediciendo la respuesta...")
    time.sleep(2) # Pausamos el programa 2 segundos para simular el tiempo de respuesta
    
    # Convertimos el prompt a minúsculas para buscar palabras clave más fácil
    prompt_limpio = prompt.lower()
    
    # El LLM reacciona dependiendo de las palabras en el prompt
    if "hola" in prompt_limpio:
        return "¡Hola humano! ¿En qué te puedo ayudar hoy?"
    
    elif "resumir" in prompt_limpio:
        return "Claro, el resumen es: Los LLMs predicen texto usando mucha estadística."
    
    elif "código" in prompt_limpio or "python" in prompt_limpio:
        return "Aquí tienes: print('¡Hola Mundo desde el LLM!')"
    
    else:
        return "Soy un modelo simple. Por favor pregúntame sobre resúmenes o código en Python."


print("--- Iniciando conexión con el LLM ---")

# 1. Definimos nuestro Prompt (La instrucción)
mi_primer_prompt = "Hola, ¿estás ahí?"
print("👤 Usuario:", mi_primer_prompt)

# 2. Enviamos el prompt al modelo y guardamos el Completion
respuesta_1 = consultar_llm(mi_primer_prompt)
print("🤖 LLM:", respuesta_1)

print("\n--- Haciendo una petición más específica ---")

# Ahora somos más específicos (Prompt Engineering)
mi_segundo_prompt = "Necesito resumir cómo funciona tu cerebro"
print("👤 Usuario:", mi_segundo_prompt)

respuesta_2 = consultar_llm(mi_segundo_prompt)
print("🤖 LLM:", respuesta_2)
