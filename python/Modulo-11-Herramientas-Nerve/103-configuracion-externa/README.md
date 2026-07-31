# Nivel 103: El Plano de la Casa (Configuración) 🗺️

Hasta ahora, cuando encendías `nerve start`, el Hub elegía automáticamente dónde construir la Oficina de Correos (por defecto en el puerto 50505 o en un archivo temporal `/tmp/nerve.sock`). Pero, ¿qué pasa si ese puerto ya está ocupado por otro programa en tu computadora? 

En la vida real de la programación, **nunca debes mezclar las configuraciones con tu código**. Si cambias de casa (servidor), no deberías tener que reescribir tu ADN (código). 

En este nivel aprenderemos a usar un archivo mágico llamado `nerve.config`. Este archivo actúa como los planos de la casa: le dice a Nerve exactamente dónde construir la red, sin que tengas que modificar ni una sola línea de tu código Python.

## Ruta de Aprendizaje

1. **Teoría (`teoria.md`)**: Descubriremos cómo aislar configuraciones usando archivos `.config`.
2. **Ejemplo (`ejemplo.py`)**: Crearemos nuestra propia configuración personalizada y veremos cómo Nerve obedece ciegamente.
3. **Reto (`reto.md`)**: Mudarás toda tu red a una "dirección" completamente diferente.
