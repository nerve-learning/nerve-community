# Nivel 116: La Fábrica de Ensamblaje (Pipelines de Datos) 🏭

En el mundo real, los datos casi nunca vienen listos para usarse. Si extraes información de una página web, suele venir sucia, con errores o en el formato incorrecto. 
No puedes (ni debes) crear una sola función gigante que haga TODO el trabajo de limpiar, calcular y guardar los datos. Si esa función gigante falla, todo el sistema se cae y es imposible encontrar el error.

La solución arquitectónica a este problema es el **Pipeline de Datos** (Tubería de datos).
Es como una fábrica de ensamblaje de autos: una máquina pone el chasis y se lo pasa a la siguiente; la segunda pone el motor y lo pasa a la tercera; la tercera lo pinta.

En este nivel aprenderás a conectar múltiples bots de Nerve en cadena, creando una verdadera línea de ensamblaje donde la salida de uno es la entrada del siguiente.

### Ruta de aprendizaje

1. **Teoría (`teoria.md`)**: El concepto de Nodos Especializados y el peligro del Bucle Infinito.
2. **Ejemplo (`ejemplo.py`)**: Construiremos una Planta Purificadora de Agua de tres pasos.
3. **Reto (`reto.md`)**: Programarás la cadena de montaje de la Panadería Automática.
