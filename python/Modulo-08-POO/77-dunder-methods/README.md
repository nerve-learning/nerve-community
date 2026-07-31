# Nivel 77: Métodos Dunder (Doble Guion Bajo) 🪄

¿Alguna vez has intentado hacerle un `print()` a un objeto que tú mismo creaste? Si lo has hecho, seguramente viste algo muy feo en tu terminal, algo como esto:
`<__main__.Perro object at 0x7f8b9c2a10>`

Para una computadora, esa es la dirección de memoria donde vive tu objeto. Pero para nosotros los humanos, eso no significa nada. 

Aquí es donde entran los **Métodos Dunder** (del inglés *Double Underscore*, por el doble guion bajo `__`). Ya conoces a uno de ellos: el famoso `__init__`. Estos métodos son como hechizos mágicos que nos permiten "hackear" el comportamiento de Python. Hoy aprenderemos a usar `__str__` para darle una voz humana a nuestros objetos cuando intentamos imprimirlos.

## Ruta de aprendizaje
1. **Teoría (`teoria.md`)**: Entenderemos qué es `__str__`, por qué se considera mágico, y la regla de oro del `return`.
2. **Ejemplo (`ejemplo.py`)**: Crearemos una Biblioteca donde los libros saben cómo presentarse a sí mismos.
3. **Reto (`reto.md`)**: ¡Te encargarás de imprimir el menú de un restaurante! A programar.
