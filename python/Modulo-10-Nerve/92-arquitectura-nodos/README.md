# Nivel 92: Arquitectura de Nodos 🕸️

En el nivel anterior, logramos que nuestro programa gritara al vacío enviando un paquete por los tubos neumáticos de Nerve. ¡Eso fue increíble! Pero un programa que solo habla y no escucha es como un walkie-talkie con el botón de hablar atascado. 

En la vida real, los sistemas distribuidos (muchos programas trabajando juntos) funcionan como un equipo de trabajo: algunos envían órdenes, y otros *se quedan esperando* a escuchar instrucciones para ejecutarlas. A estos programas que saben escuchar y hablar les llamamos **Nodos**.

En este nivel aprenderemos a darle "oídos" a nuestro programa para que pueda reaccionar en tiempo real cada vez que alguien le envíe información por la red local.

## Ruta de Aprendizaje

1. **Teoría (`teoria.md`)**: El concepto del Recepcionista (Callbacks) y la Inmortalidad (el bucle de vida).
2. **Ejemplo (`ejemplo.py`)**: Construiremos nuestro primer Nodo completo que escucha y reacciona a mensajes.
3. **Reto (`reto.md`)**: Crearás un Nodo de Alarma que se queda vigilando la red local hasta que recibe una alerta crítica.
