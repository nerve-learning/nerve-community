# Nivel 91: El Despertar Local-First 🧠

¿Alguna vez te has preguntado cómo los diferentes programas en tu computadora logran hablar entre ellos tan rápido? Hasta ahora, cuando querías conectar dos programas, usabas internet (como las Web APIs que vimos en el Módulo 07). 

Pero usar internet para hablar con un programa que está *en tu misma computadora* es como salir de tu casa, darle la vuelta al vecindario y entrar por la puerta trasera solo para hablar con alguien que está en la misma habitación. Es lento, inseguro y si se cae el internet, tu programa se muere.

En este nivel aprenderemos sobre la filosofía **Local-First** usando el motor **Nerve**. Aprenderás a construir programas soberanos que hablan entre ellos en milisegundos, con total privacidad y sin salir jamás de tu disco duro.

## Instalación de Nerve

Antes de comenzar, necesitamos instalar el motor **Nerve** en nuestro entorno. Te recomendamos hacerlo usando un entorno virtual para no ensuciar tu sistema.

Abre tu terminal y ejecuta:

```bash
python3 -m venv alenia_env
source alenia_env/bin/activate   # En Windows: alenia_env\Scripts\activate
pip install alenia-nerve
```

## Ruta de Aprendizaje


1. **Teoría (`teoria.md`)**: Entenderemos qué es la comunicación Inter-Procesos (IPC) y cómo funciona el "tubo neumático" de Nerve.
2. **Ejemplo (`ejemplo.py`)**: Construiremos nuestro primer nodo local que envía mensajes al vacío.
3. **Reto (`reto.md`)**: Te convertirás en un agente secreto transmitiendo información confidencial a la red local.
