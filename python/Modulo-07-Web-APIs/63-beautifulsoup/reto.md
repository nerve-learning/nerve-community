# Reto 03: Tabla Falsa 🍪

**URL del reto:** `https://nerve.community.aleniastudios.me/laberinto/tz99/data-401.html`

El usuario ve una receta de galletas con chispas de chocolate. Ingredientes, pasos, todo muy apetitoso. Pero dentro del HTML hay una estructura tabular **completamente oculta** (`position:absolute; left:-9999px`), disfrazada con `div` en lugar de `<table>`.

Tu misión es extraer el **número secreto** de esa tabla falsa que el usuario jamás verá.

## Instrucciones Paso a Paso:

1. Importa `requests` y `BeautifulSoup`.
2. Haz un `requests.get()` a la URL del reto.
3. Parsea el HTML con BeautifulSoup.
4. La tabla falsa está hecha con `div` que tienen clases como `row` y `cell`. Busca el `div` contenedor `table-wrap` o navega buscando la celda con el valor oculto.
5. Extrae el número que está en la celda de datos y muéstralo.

> **Pista:** En un `<table>` real usarías `find('table')`. Aquí la tabla está construida con `<div class="row">` y `<div class="cell">`. Usa `.find_all()` para localizar las celdas. El dato real es un número de 2 dígitos.

## Reglas Estrictas:
✅ **Conceptos Permitidos:** `requests`, `BeautifulSoup`, `.find()`, `.find_all()`, `.get_text()`, `.string`, navegación por clases CSS.
❌ **Conceptos Prohibidos:** Selenium, pandas para este reto.

## Resultado Esperado en tu Terminal:

```text
[+] Código de estado: 200
[+] Dato extraído de la tabla oculta: 42
```

Escribe tu código en `reto.py`. Los `div` también pueden ser tablas si sabes leer el CSS.
