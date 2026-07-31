# Nivel 94: El Estado Global 🌍

Hasta ahora hemos logrado que nuestros nodos hablen y escuchen (P2P). Pero hay un pequeño problema: **nuestros nodos sufren de amnesia**. 

Cada vez que llega un mensaje, el recepcionista lo lee, lo imprime en la pantalla y lo olvida para siempre. Si queremos construir un sistema real (como un chat que guarde el historial, un juego que lleve la puntuación, o un sensor que calcule promedios), necesitamos que el nodo tenga **Memoria**. 

En programación distribuida, a esta memoria a largo plazo que todos pueden consultar le llamamos **Estado Global**.

## Ruta de Aprendizaje

1. **Teoría (`teoria.md`)**: La Pizarra de la Oficina y la palabra mágica `global`.
2. **Ejemplo (`ejemplo.py`)**: Construiremos un servidor de "Likes" que lleva la cuenta de cuántos corazones ha recibido por la red.
3. **Reto (`reto.md`)**: Serás el cajero de un Banco Descentralizado, restando dinero de una bóveda compartida.
