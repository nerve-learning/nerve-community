# 12 - Arquitectura Avanzada

### `microservicio`

**¿Qué es?**
Un enfoque para desarrollar una aplicación como un conjunto de pequeños servicios independientes, donde cada uno ejecuta un proceso único y tiene una sola responsabilidad bien definida.

**¿Para qué se usa?**
Para que aplicaciones gigantes (como Netflix o Amazon) puedan ser construidas, escaladas y actualizadas por partes. Si la parte que maneja los pagos (un microservicio) se cae, el resto de la página web sigue funcionando.

**Ejemplo:**
```python
# En lugar de tener un archivo main.py de 10,000 líneas:
# Tienes: usuario_service.py, pagos_service.py, email_service.py
```

**Errores comunes de principiante:**
- Intentar usar microservicios para un proyecto extremadamente pequeño, complicándolo innecesariamente (añadiendo problemas de red donde antes solo había llamadas a funciones).

**Términos relacionados:** [`monolito vs distribuido`](#monolito-vs-distribuido)

### `orquestador`

**¿Qué es?**
Un programa o sistema (como Kubernetes en el mundo real, o un script central en Nerve) que se encarga de gestionar, monitorear y organizar automáticamente otros programas o microservicios.

**¿Para qué se usa?**
Para saber quién está haciendo qué. Si un microservicio muere, el orquestador se da cuenta y lo reinicia. También puede decirle a varios servicios en qué orden deben procesar la información.

**Ejemplo:**
```python
# El orquestador nota que un worker murió y lanza uno nuevo
if not worker.esta_vivo():
    lanzar_nuevo_proceso("worker_de_respaldo")
```

**Errores comunes de principiante:**
- Hacer que el orquestador procese datos él mismo. El orquestador solo debe dirigir el tráfico o gestionar los demás, no hacer el trabajo pesado.

**Términos relacionados:** [`microservicio`](#microservicio), [`tolerancia a fallos / failover`](#tolerancia-a-fallos--failover)

### `tolerancia a fallos` / `failover`

**¿Qué es?**
La capacidad de un sistema para seguir operando correctamente incluso en caso de que uno o más de sus componentes fallen. Un *failover* (conmutación por error) es cuando un sistema de respaldo entra a funcionar automáticamente al caerse el principal.

**¿Para qué se usa?**
Para sistemas que no se pueden permitir caer (como bancos o servidores de hospitales). Si el servidor A se quema, el servidor B toma su lugar instantáneamente sin que el usuario lo note.

**Ejemplo:**
```python
try:
    conectar_base_de_datos_principal()
except ErrorDeConexion:
    # Failover a una base de datos de solo lectura o secundaria
    conectar_base_de_datos_respaldo()
```

**Errores comunes de principiante:**
- Asumir que el hardware o la red nunca fallarán y escribir código que colapsa por completo ante el primer error de conexión.

**Términos relacionados:** [`orquestador`](#orquestador)

### `async/await`

**¿Qué es?**
Una sintaxis de Python para escribir código concurrente (hacer múltiples cosas a la vez) de manera sencilla. `async` define una función como "asíncrona" y `await` indica "pausa esta función y haz otra cosa mientras esperamos que esto termine".

**¿Para qué se usa?**
Es vital para tareas de Entrada/Salida (I/O) como leer archivos grandes, descargar cosas de internet o comunicarse por red (Nerve). Mientras el código espera una respuesta de internet, el procesador puede ir haciendo otra cosa.

**Ejemplo:**
```python
import asyncio

async def descargar_datos():
    print("Iniciando descarga...")
    await asyncio.sleep(2) # Simula esperar por la red
    print("Descarga terminada")
```

**Errores comunes de principiante:**
- Llamar a una función `async` normalmente, como `descargar_datos()`, olvidando poner el `await` antes, lo cual devuelve una "corutina" y no ejecuta la función.
- Usar una operación bloqueante (como `time.sleep()`) dentro de una función asíncrona, bloqueando a todo el sistema.

**Términos relacionados:** [`event loop`](#event-loop)

### `event loop`

**¿Qué es?**
El "bucle de eventos". Es el motor central que hace funcionar al código asíncrono. Está constantemente dando vueltas revisando si alguna tarea asíncrona ya terminó de esperar (ej: si ya llegó el paquete de red) para reanudarla.

**¿Para qué se usa?**
Es el responsable de organizar y ejecutar todas las tareas concurrentes en un solo hilo de ejecución de manera increíblemente eficiente (como un malabarista manteniendo muchos platos girando a la vez).

**Ejemplo:**
```python
# Para correr tu función asíncrona principal y encender el motor:
import asyncio
asyncio.run(mi_programa_principal())
```

**Errores comunes de principiante:**
- Tratar de iniciar múltiples *event loops* al mismo tiempo dentro de un mismo hilo, lo cual genera un error de "RuntimeError".

**Términos relacionados:** [`async/await`](#asyncawait)

### `semáforo` / `Lock`

**¿Qué es?**
Mecanismos de control (primitivas de sincronización) que evitan que varios procesos o hilos intenten modificar o acceder a un mismo recurso (como un archivo o una variable) al mismo tiempo, lo que causaría corrupción de datos. Un **Lock** es como la llave de un baño (solo uno pasa a la vez), un **Semáforo** es como un estacionamiento con varios lugares fijos.

**¿Para qué se usa?**
Para evitar las "condiciones de carrera" (race conditions). Si dos procesos intentan sumar +1 a la cuenta de banco al mismo milisegundo sin usar un Lock, es probable que la cuenta termine subiendo solo +1 en lugar de +2.

**Ejemplo:**
```python
import asyncio

candado = asyncio.Lock()

async def modificar_datos():
    async with candado:
        # Solo una función puede entrar a este bloque a la vez
        # Modificar los datos críticos de forma segura
        pass
```

**Errores comunes de principiante:**
- Crear un "deadlock" (abrazo mortal): La Tarea A tiene la Llave 1 y espera la Llave 2. La Tarea B tiene la Llave 2 y espera la Llave 1. Ambas se quedan esperando infinitamente y el programa se congela.

**Términos relacionados:** [`async/await`](#asyncawait)

### `topología de red`

**¿Qué es?**
Es el diseño, mapa o estructura física/lógica de cómo están conectados los diferentes nodos (computadoras, scripts, microservicios) entre sí.

**¿Para qué se usa?**
Para entender cómo fluye la información. Una topología de "estrella" significa que todos los nodos se comunican solo con el centro (como Nerve usando el NexusHub). Una topología "malla" (mesh) significa que todos se conectan con todos directamente.

**Ejemplo:**
```python
# Topología de Estrella (Star)
# Script_A ---> HUB <--- Script_B
#                ^
#                |
#             Script_C
```

**Errores comunes de principiante:**
- Diseñar sistemas caóticos donde cada script debe conocer la dirección IP y puerto de todos los demás (topología de malla total), lo cual es imposible de mantener al escalar.

**Términos relacionados:** [`NexusHub`](../10-nerve-ipc.md#nexushub)

### `monolito` vs `distribuido`

**¿Qué es?**
Dos filosofías opuestas para construir aplicaciones. Un **monolito** es un sistema gigante en el que todo el código (interfaz, base de datos, lógica) vive en un solo programa. Un sistema **distribuido** es un conjunto de componentes independientes dispersos en varias máquinas que parecen un solo programa para el usuario final.

**¿Para qué se usa?**
Se suele empezar con un monolito porque es más fácil de crear, probar y desplegar. Se migra a un sistema distribuido (como microservicios) cuando el monolito se vuelve demasiado grande y el equipo de desarrollo necesita dividir el trabajo para no estorbarse.

**Ejemplo:**
```python
# Monolito: Un archivo Django gigante o un super-script de Python.
# Distribuido: 5 scripts separados por red usando Nerve o Kubernetes.
```

**Errores comunes de principiante:**
- Pensar que los sistemas distribuidos siempre son "mejores" o "más modernos". En realidad añaden una inmensa complejidad de red y depuración; si un monolito resuelve el problema rápida y eficientemente, es la elección correcta.

**Términos relacionados:** [`microservicio`](#microservicio), [`topología de red`](#topología-de-red)
