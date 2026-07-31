# Nivel 118: El Cadenero del Antro (Restricciones Rate Limit) 🛑

Imagina que abres una pizzería y permites hacer pedidos por teléfono. ¿Qué pasa si un robot malicioso te llama 1,000 veces por segundo? Tu línea telefónica colapsa, los clientes reales no pueden llamar y tu negocio se detiene. En el mundo del software, esto se llama **Ataque DoS (Denial of Service)**.

Incluso sin malicia, un error en tu propio código (como un `while True` descontrolado) puede saturar tu propio sistema en cuestión de milisegundos. Para evitar esto, inventamos el **Rate Limiting** (Límite de Tasa).

En este nivel aprenderás a configurar un "cadenero" en tu sistema Nerve que rechace automáticamente a cualquiera que hable demasiado rápido, protegiendo así tu infraestructura para que no colapse.

### Ruta de aprendizaje

1. **Teoría (`teoria.md`)**: El concepto de Rate Limit y cómo usar los parámetros secretos del Hub.
2. **Ejemplo (`ejemplo.py`)**: Deteniendo a un Spammer que intenta inundarnos de publicidad.
3. **Reto (`reto.md`)**: Configurar la ventanilla del banco que odia a los clientes impacientes.
