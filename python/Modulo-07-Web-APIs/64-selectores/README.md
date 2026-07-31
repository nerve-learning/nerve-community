# Nivel 64: Cazando con Precisión (Selectores) 🎯

En el nivel anterior, usamos `.find('p')` para encontrar un párrafo. Pero piensa en el mundo real: una página de noticias no tiene un solo párrafo, ¡tiene miles! 

Si usas `.find('p')`, BeautifulSoup te devolverá el primer párrafo que vea (que probablemente sea algo aburrido como "Derechos reservados 2026"). 

Para extraer los datos valiosos (como los precios de una tienda, o los titulares de noticias), necesitamos decirle a la tijera mágica *exactamente* dónde cortar. Para eso, las páginas web usan "etiquetas secretas" llamadas **Selectores** (`id` y `class`).

Además, hoy aprenderemos cómo pedirle a la herramienta que no nos traiga un solo recorte, ¡sino **todos** los que encuentre en la página!

## Tu ruta de aprendizaje hoy:
1. **Teoría (`teoria.md`)**: El supermercado HTML y la diferencia entre un código de barras (`id`) y un pasillo (`class`).
2. **Ejemplo (`ejemplo.py`)**: Saquearemos una tienda mágica falsa usando filtros precisos y bucles `for`.
3. **Reto (`reto.md`)**: Te conectarás a una página web real diseñada para hackers y extraerás todas sus frases célebres.

¡Apunta, filtra y extrae!
