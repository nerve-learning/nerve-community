# Reto 06: Generación Dinámica ⚡

**URL del reto:** `https://nerve.community.aleniastudios.me/laberinto/m5v/dyn.html`

La página muestra una "Calculadora Cuántica" procesando la respuesta a la vida, el universo y todo lo demás. El resultado se **inyecta en el DOM mediante JavaScript** después de que la página carga. Un scraper estático como BeautifulSoup solo descargará el HTML inicial (con el `div` vacío), sin ver nunca el dato calculado.

Tu misión: extraer el **número calculado** usando una de dos estrategias válidas.

## Instrucciones Paso a Paso:

**Estrategia A — Parsear el bloque `<script>` (sin Selenium):**
1. Importa `requests` y `BeautifulSoup`.
2. Haz un `requests.get()` y parsea el HTML.
3. Encuentra la etiqueta `<script>` que contiene el número hardcodeado.
4. Lee el texto del script y extrae el número usando `.split()` o una expresión regular.

**Estrategia B — Usar Selenium (ejecución real de JS):**
1. Importa `selenium.webdriver` y `time`.
2. Abre la URL en un WebDriver headless.
3. Espera unos segundos a que el JS termine de ejecutarse (`time.sleep(2)`).
4. Extrae el texto del elemento `result-container`.

> **Pista (Estrategia A):** El script contiene una variable como `const secretNumber = 7749;`. Busca ese patrón en el texto del `<script>`.

## Reglas Estrictas:
✅ **Conceptos Permitidos:** `requests` + parseo de `<script>`, **o** `selenium` + espera. Elige una estrategia.
❌ **Conceptos Prohibidos:** Adivinar el número. Debes extraerlo programáticamente.

## Resultado Esperado en tu Terminal:

```text
[+] Número cuántico encontrado: 7749
```

Escribe tu código en `reto.py`. Este reto marca la diferencia entre scrapers novatos y profesionales.
