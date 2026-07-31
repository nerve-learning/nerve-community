# Reto 120: El Sistema de Defensa Planetaria 🚀🌍

¡Este es tu examen final de Arquitectura de Software! Has sido contratado por la Agencia Espacial para diseñar un sistema distribuido que detecte asteroides peligrosos y avise a las estaciones terrestres.

Para que el sistema sea resistente a fallas, debe estar dividido en **3 archivos diferentes** y un **cerebro central** (`nerve start`).

### Instrucciones

Tu misión es crear 3 archivos Python desde cero:
1. `radar.py`
2. `filtro.py`
3. `alarma.py`

**Paso 1: El Radar (Sensor)**
Este script debe conectarse a Nerve con el nombre `"radar"`.
En un bucle infinito, debe generar un número aleatorio entre 1 y 100 cada segundo (simulando el tamaño de un asteroide en metros) y enviarlo usando `broadcast()`.

**Paso 2: El Filtro (Procesador)**
Este script debe conectarse a Nerve con el nombre `"filtro"`.
Debe escuchar (`listen`) todos los mensajes del radar.
- Si el tamaño del asteroide es **menor a 50**, hace un `print("Roca inofensiva.")`.
- Si el tamaño es **50 o mayor**, debe enviar un *nuevo mensaje* dirigido específicamente al nombre `"alarma"` usando `send(to="alarma", payload=...)`.

**Paso 3: La Alarma (Pantalla)**
Este script debe conectarse a Nerve con el nombre `"alarma"`.
Debe escuchar (`listen`). Cuando reciba un mensaje (que vendrá del filtro), debe hacer un print gigante: `print("🚨 ¡PELIGRO! Asteroide gigante detectado de X metros 🚨")`.

**Paso 4: La Ejecución**
1. Abre Terminal 1 y escribe `nerve start` (El cerebro de comunicaciones).
2. Abre Terminal 2 y corre `python radar.py`.
3. Abre Terminal 3 y corre `python filtro.py`.
4. Abre Terminal 4 y corre `python alarma.py`.

### Reglas
- **Conceptos permitidos**: `import time`, `import random`, diccionarios `{}`, bucles `while True`, condicionales `if/else`, y los métodos `connect()`, `broadcast()`, `send()`, `listen()` de `NexusClient`.
- **Prohibido**: Juntar la lógica en un solo archivo. ¡Tienen que ser 3 programas separados!

### Resultado Esperado en la Terminal de la Alarma

```text
--- INICIANDO SISTEMA DE ALARMA ---
Esperando alertas de asteroides...
🚨 ¡PELIGRO! Asteroide gigante detectado de 87 metros 🚨
🚨 ¡PELIGRO! Asteroide gigante detectado de 52 metros 🚨
🚨 ¡PELIGRO! Asteroide gigante detectado de 99 metros 🚨
```
