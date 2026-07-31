# Reto 01: El ID Secreto 🔍

**URL del reto:** `https://nerve.community.aleniastudios.me/laberinto/a1b2/x9.html`

Estás en tu primer día como scraper. La página parece simple: un chiste del día y un panel de misión. Pero visualmente, el dato que buscas **no se ve**. Está ahí en el HTML, oculto con `display:none`.

Tu misión es extraer el **código de acceso secreto** que está escondido en un elemento con un ID específico.

## Instrucciones Paso a Paso:

1. Importa `requests` y `BeautifulSoup` (de `bs4`).
2. Crea una variable con la URL del reto.
3. Haz un `requests.get()` a la URL y verifica que el `status_code` sea 200.
4. Crea un objeto `BeautifulSoup` con el contenido HTML de la respuesta.
5. Inspecciona el HTML (en el navegador o leyendo la respuesta) para encontrar el elemento con el ID que contiene el dato real.
6. Extrae el texto de ese elemento y muéstralo en la terminal.

> **Pista:** El elemento que buscas tiene un `id` específico y está estilizado con `display:none` para que el usuario no lo vea. BeautifulSoup lo extrae sin problema porque no ejecuta CSS.

## Reglas Estrictas:
✅ **Conceptos Permitidos:** `import requests`, `from bs4 import BeautifulSoup`, `requests.get()`, `.text`, `.find()`, `.find_all()`, acceso por `id`.
❌ **Conceptos Prohibidos:** Selenium, Playwright, cualquier scraper dinámico. Este reto se resuelve con HTTP estático.

## Resultado Esperado en tu Terminal:

```text
[+] Código de estado: 200
[+] Código de acceso encontrado: XJ-900
```

Escribe tu código en un nuevo archivo llamado `reto.py`. ¡El dato existe en el HTML, solo hay que saber buscarlo!
