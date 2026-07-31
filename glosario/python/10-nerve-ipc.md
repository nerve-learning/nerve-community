# 10 - Nerve e IPC

### `IPC` (Inter-Process Communication)

**¿Qué es?**
Comunicación Entre Procesos. Es un conjunto de mecanismos que permite que distintos programas (procesos) que se están ejecutando en la misma computadora se envíen datos o mensajes entre sí.

**¿Para qué se usa?**
Para que diferentes partes de un sistema complejo, como pequeños scripts independientes, puedan coordinarse y trabajar juntos intercambiando información.

**Ejemplo:**
```python
# Un script de interfaz de usuario manda un mensaje por IPC
# a un script que maneja la base de datos para que guarde información.
```

**Errores comunes de principiante:**
- Pensar que dos scripts de Python en la misma computadora comparten variables mágicamente. Debes enviar la información explícitamente usando IPC.

**Términos relacionados:** [`Unix Socket`](#unix-socket-vs-tcp), [`canal / channel`](#canal--channel)

### `NexusHub`

**¿Qué es?**
En el ecosistema Nerve, es el servidor o núcleo central que se encarga de recibir, organizar y distribuir todos los mensajes que los diferentes programas se envían entre sí.

**¿Para qué se usa?**
Es el corazón de tu red local. En lugar de que todos tus scripts intenten hablarse entre ellos (lo cual es caótico), todos hablan con el NexusHub y él se encarga de entregar los mensajes al destinatario correcto.

**Ejemplo:**
```python
# Comando teórico para iniciar el hub
# nerve start hub
```

**Errores comunes de principiante:**
- Olvidar iniciar el NexusHub antes de iniciar los clientes, haciendo que nadie pueda conectarse ni enviar mensajes.

**Términos relacionados:** [`NexusClient`](#nexusclient)

### `NexusClient`

**¿Qué es?**
En Nerve, es la herramienta (cliente) que usa un programa individual para conectarse al NexusHub. Actúa como el puente entre tu código y la red del Hub.

**¿Para qué se usa?**
Para que tu script pueda enviar (publicar) y recibir (suscribirse a) mensajes a través de la red de Nerve de manera sencilla.

**Ejemplo:**
```python
from nerve import NexusClient
cliente = NexusClient("mi_script_1")
cliente.conectar()
```

**Errores comunes de principiante:**
- Instanciar un cliente pero olvidar llamar a la función de conectar.
- Darle el mismo nombre a dos clientes distintos, causando conflictos en el Hub.

**Términos relacionados:** [`NexusHub`](#nexushub)

### `canal / channel`

**¿Qué es?**
Un "tema" o "tópico" específico bajo el cual se agrupan los mensajes. Es como una sala de chat temática donde solo se habla de una cosa.

**¿Para qué se usa?**
Para organizar la información. Si un script solo necesita saber de "temperatura", se suscribe al canal `sensores/temperatura` y así no recibe mensajes irrelevantes del canal `sistema/errores`.

**Ejemplo:**
```python
# Publicar un mensaje en un canal específico
cliente.publicar(canal="alertas/criticas", mensaje="Error en el servidor")
```

**Errores comunes de principiante:**
- Escribir mal el nombre del canal al suscribirse (ej. "alerta" en vez de "alertas"), por lo que nunca llegan los mensajes esperados.

**Términos relacionados:** [`suscripción vs publicación`](#suscripción-vs-publicación)

### `suscripción` vs `publicación`

**¿Qué es?**
Es el modelo de comunicación básico en mensajería (Pub/Sub). **Publicar** (publish) es emitir un mensaje hacia un canal sin importar quién lo escucha. **Suscribirse** (subscribe) es decirle al Hub "avísame cuando alguien publique algo en este canal".

**¿Para qué se usa?**
Para desacoplar el código. El que publica no necesita saber cuántos están escuchando, y el que escucha no necesita saber quién mandó el dato, solo le importa el canal.

**Ejemplo:**
```python
# Publicar
cliente.publicar("clima", "Hará sol")

# Suscribirse
def recibir_clima(msg):
    print("El clima será:", msg)
cliente.suscribir("clima", recibir_clima)
```

**Errores comunes de principiante:**
- Intentar procesar la respuesta inmediatamente después de publicar, olvidando que este modelo es asíncrono y los mensajes fluyen sin detener el programa.

**Términos relacionados:** [`canal / channel`](#canal--channel)

### `Unix Socket` vs `TCP`

**¿Qué es?**
Son dos protocolos o formas de transporte para mandar los mensajes. Un `Unix Socket` manda los datos a través de un archivo especial en el sistema operativo (solo funciona en la misma máquina). `TCP` manda los datos a través de una dirección IP y un puerto (funciona por internet o red local).

**¿Para qué se usa?**
Los Unix Sockets son increíblemente rápidos para comunicar programas en la *misma computadora*. TCP se usa si los programas están en *computadoras diferentes* conectadas por red.

**Ejemplo:**
```python
# Un Unix Socket se ve como una ruta de archivo: /tmp/nerve.sock
# Una dirección TCP se ve así: 127.0.0.1:8080
```

**Errores comunes de principiante:**
- Intentar usar Unix Sockets para comunicar programas que están en distintas computadoras o en Windows (donde históricamente no son el estándar).

**Términos relacionados:** [`IPC`](#ipc-inter-process-communication)

### `offline-first`

**¿Qué es?**
Un principio de diseño donde el software se construye para funcionar correcta y fluidamente sin conexión a internet desde el primer momento, usando la red solo cuando esté disponible.

**¿Para qué se usa?**
Para hacer aplicaciones más rápidas, robustas y privadas, que no dependan de la nube para sus funciones principales. Nerve usa esta filosofía para mantener todo el procesamiento local.

**Ejemplo:**
```python
# Un agente de IA que corre modelos pequeños en tu propia computadora,
# en vez de llamar a una API de OpenAI a través de internet.
```

**Errores comunes de principiante:**
- Asumir que "local" significa "inútil", ignorando que hoy en día una computadora promedio tiene poder de sobra para tareas complejas sin enviar datos a la nube.

**Términos relacionados:** [`NexusHub`](#nexushub)

### `heartbeat`

**¿Qué es?**
Un "latido de corazón". Es un pequeño mensaje que un programa envía regularmente (por ejemplo, cada 5 segundos) al Hub para avisar "sigo vivo y funcionando".

**¿Para qué se usa?**
Para que el sistema (o el orquestador) sepa rápidamente si un proceso se colgó, crasheó o se desconectó, y pueda reiniciar ese servicio o alertar al usuario.

**Ejemplo:**
```python
import time
while True:
    cliente.publicar("sistema/latidos", "estoy_vivo")
    time.sleep(5)
```

**Errores comunes de principiante:**
- Poner un intervalo de *heartbeat* demasiado corto, saturando la red con mensajes inútiles, o demasiado largo, tardando mucho en detectar una falla.

**Términos relacionados:** [`IPC`](#ipc-inter-process-communication)
