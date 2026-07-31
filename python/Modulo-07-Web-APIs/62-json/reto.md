# Reto 02: Ruido de Clases 📡

**URL del reto:** `https://nerve.community.aleniastudios.me/laberinto/8f4c/k3.html`

La página muestra una meditación diaria: texto zen, colores suaves, tranquilidad... Pero dentro del HTML hay elementos **ocultos visualmente** con CSS (`opacity: 0`, `position: absolute`). El scraper no distingue entre lo visible y lo invisible: lo lee todo.

Tu misión es encontrar la **dirección IP** escondida entre el ruido visual de la página.

## Instrucciones Paso a Paso:

1. Importa `requests` y `BeautifulSoup`.
2. Haz un `requests.get()` a la URL del reto.
3. Parsea el HTML con BeautifulSoup.
4. El dato real está en un elemento con una clase específica (busca en el HTML `hidden-data` o similar).
5. Extrae el texto de ese elemento y muéstralo.

> **Pista:** Hay varios elementos que parecen candidatos, pero solo uno tiene la clase exacta `hidden-data`. Los otros son señuelos visuales. Un humano no los ve, pero `find()` con la clase correcta te lleva directo al dato.

## Reglas Estrictas:
✅ **Conceptos Permitidos:** `requests`, `BeautifulSoup`, `.find()`, `.find_all()`, atributo `class`.
❌ **Conceptos Prohibidos:** Selenium, expresiones regulares complejas para parsear HTML directamente.

## Resultado Esperado en tu Terminal:

```text
[+] Código de estado: 200
[+] Dirección IP encontrada: 192.168.1.42
```

Escribe tu código en `reto.py`. Recuerda: el CSS engaña al ojo, pero no al parser.
