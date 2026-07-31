# Teoría: El Recepcionista Bilingüe (Nerve Bridge) 🌐

Imagina que Nerve Hub es una oficina de alta seguridad. Dentro de esta oficina, todos los trabajadores (tus scripts de Python) hablan un idioma ultra-rápido y secreto (Unix Sockets o TCP en el puerto 50505). Se pasan mensajes a la velocidad del rayo.

De repente, un cliente externo quiere comunicarse con la oficina. Este cliente es una **página web** que se ejecuta en el navegador Chrome. Los navegadores web tienen reglas de seguridad muy estrictas y solo hablan ciertos idiomas oficiales, como HTTP o **WebSockets**. Un navegador web tiene prohibido intentar hablar el idioma secreto de los Unix Sockets de tu oficina.

Si el navegador intenta entrar directamente a la oficina, la puerta de seguridad (Nerve Hub) no le entenderá y lo rechazará.

### La Solución: El Puente (Bridge)

Para solucionar esto, Alenia creó **`nerve bridge`**.

Cuando ejecutas el comando `nerve bridge` en tu terminal, estás contratando a un "recepcionista bilingüe". 
Este recepcionista se sienta en una puerta pública (el puerto **50506**).

1. El navegador web llega a la puerta pública (50506) hablando su idioma (WebSockets).
2. El recepcionista (`nerve bridge`) entiende WebSockets. Toma el mensaje del navegador.
3. El recepcionista se da la vuelta, traduce el mensaje al idioma secreto, y se lo entrega al `Nerve Hub` (en el puerto 50505 o archivo `.sock`).
4. El Hub reparte el mensaje a los trabajadores (tus scripts en Python).
5. Cuando los trabajadores responden, se lo dan al recepcionista, y él se lo traduce de vuelta al navegador.

### ¿Por qué es útil?

Gracias a este puente, puedes construir interfaces gráficas (pantallas con botones, colores y gráficos) en una página web normal usando HTML y JavaScript, y hacer que esa página web controle tus programas de Python locales, todo en tiempo real y sin necesidad de internet (porque el puente sigue estando dentro de tu computadora, es local).

### Resumen de la Arquitectura

```text
[Navegador Web] <--- (WebSockets / Puerto 50506) ---> [Nerve Bridge] <--- (UDS/TCP) ---> [Nerve Hub] <---> [Tus Scripts Python]
```

Para que esto funcione, primero debes encender la oficina (`nerve start`), y luego encender al recepcionista (`nerve bridge`). ¡Son dos programas separados trabajando juntos!

> **Nota:** Para que el puente funcione, la documentación de Nerve indica que necesitas tener instalado el paquete `websockets` en tu entorno (venv).

Ve a `ejemplo.py` para ver cómo un cliente de Python recibe los mensajes que podrían venir desde el puente.
