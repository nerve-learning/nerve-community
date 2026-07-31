# Nivel 119: El Salto a Producción (Arquitectura Desacoplada) 🚀

Hasta ahora, has estado programando como si construyeras un castillo de cartas: ponías el `NexusHub()` (el cerebro central) y tus `NexusClient()` (los trabajadores) exactamente en el mismo archivo de Python. 

¿El problema? Si un trabajador comete un error fatal (como intentar dividir un número entre cero), tu archivo de Python entero "muere" (hace crash). Al morir el archivo, muere el Hub. Al morir el Hub, todos los demás trabajadores del sistema se desconectan abruptamente y tu aplicación colapsa. ¡Un desastre absoluto!

En la vida real ("Producción"), usamos **Arquitectura Desacoplada**. El cerebro corre en su propio espacio blindado y permanente, mientras que los trabajadores corren como programas independientes. Si un trabajador muere, el cerebro ni se inmuta y los demás continúan con su labor.

En este nivel aprenderás a usar Nerve como un profesional utilizando su CLI (Command Line Interface) nativa.

### Ruta de aprendizaje

1. **Teoría (`teoria.md`)**: El comando mágico de terminal y el archivo secreto de configuración.
2. **Ejemplo (`ejemplo.py`)**: Conectando trabajadores de Python a un cerebro externo.
3. **Reto (`reto.md`)**: Levantar tu propia Torre de Control separada.
