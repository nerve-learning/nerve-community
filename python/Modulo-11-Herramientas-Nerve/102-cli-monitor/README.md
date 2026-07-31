# Nivel 102: Las Cámaras de Seguridad 📹

¡Bienvenido de vuelta! Ya sabes cómo encender la Oficina de Correos (el Hub) con `nerve start` y cómo usar `--verbose` para escuchar todo lo que se dice.

Pero, ¿qué pasa cuando tienes 20 programas conectados enviando 1,000 mensajes por segundo? El modo `--verbose` imprimiría tanto texto que tu terminal parecería la película de Matrix; no podrías leer nada. En la vida real, los administradores de sistemas no leen cada mensaje, miran **métricas**.

En este nivel aprenderemos a usar `nerve monitor`, una herramienta que funciona como las cámaras de seguridad y pantallas de control de nuestra Oficina de Correos. Nos dirá quién está conectado, cuánto tiempo llevan vivos y cuántos datos están moviendo, todo en un panel visual muy limpio directamente en tu terminal.

## Ruta de Aprendizaje

1. **Teoría (`teoria.md`)**: Entenderemos qué es un monitor interactivo de terminal y por qué es mejor que leer logs de texto infinito.
2. **Ejemplo (`ejemplo.py`)**: Construiremos un generador de tráfico (un programa que envía muchos mensajes rápidos) para darle trabajo al monitor.
3. **Reto (`reto.md`)**: Levantarás la Trinidad de terminales: El Hub, el Monitor y tu Código Python.
