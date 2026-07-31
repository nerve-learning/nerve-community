# Nivel 113: Clones Trabajadores (Multiprocessing) 👯

Hasta ahora, todos los programas que has escrito son de "un solo carril". Ejecutan la línea 1, luego la línea 2, luego la línea 3... Si la línea 2 es un proceso súper pesado (como analizar millones de datos o procesar un video), la línea 3 tiene que sentarse a esperar horas hasta que termine.

Pero las computadoras modernas tienen múltiples "cerebros" (llamados núcleos o *cores*). Si tu programa solo usa un carril, está desperdiciando el 90% del poder de tu computadora.

En este nivel aprenderás a usar `multiprocessing`. Esta herramienta te permite "clonar" tu programa para que pueda hacer dos o más tareas pesadas **exactamente al mismo tiempo**, utilizando todos los cerebros de tu computadora. Es el primer paso real hacia la Arquitectura Avanzada de Sistemas.

### Ruta de aprendizaje

1. **Teoría (`teoria.md`)**: Descubriremos la analogía del "Chef Clonado" y cómo usar la sintaxis de múltiples procesos, incluyendo el escudo protector de clones.
2. **Ejemplo (`ejemplo.py`)**: Veremos a dos clones trabajando en tareas pesadas de forma simultánea.
3. **Reto (`reto.md`)**: Escribirás un script que lance un ataque de procesamiento en paralelo.
