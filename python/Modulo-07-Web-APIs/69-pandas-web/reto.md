# Reto 09: Gráficos SVG 🎨

**URL del reto:** `https://nerve.community.aleniastudios.me/laberinto/0w1/vector.html`

Una galería de arte moderno presenta "Geometría Oculta". Formas, líneas, colores. Dentro de la galería hay un gráfico SVG. Y dentro del SVG hay un elemento `<text>` con el dato que buscas.

El problema: muchos scrapers buscan en `div`, `p`, `span`... y nunca miran dentro de los `<svg>`. BeautifulSoup sí puede leer SVG si sabes dónde buscar.

Tu misión es extraer el **código vectorial** escondido en el texto del SVG.

## Instrucciones Paso a Paso:

1. Importa `requests` y `BeautifulSoup`.
2. Haz un `requests.get()` a la URL del reto.
3. Parsea el HTML con BeautifulSoup. Usa el parser `'html.parser'` o `'lxml'`.
4. Encuentra el elemento `<svg>` en la página:
   ```python
   svg = soup.find('svg')
   ```
5. Dentro del SVG, busca el elemento `<text>` (o todos los `<text>`) que contienen el dato:
   ```python
   texto_svg = svg.find('text')
   print(texto_svg.get_text())
   ```
6. Muestra el código encontrado.

> **Pista:** Puede haber múltiples elementos `<text>` en el SVG (para etiquetas decorativas). Busca el que contiene el patrón `VECTOR-XX`. Usa `.find_all('text')` y filtra si es necesario.

## Reglas Estrictas:
✅ **Conceptos Permitidos:** `requests`, `BeautifulSoup`, `.find()`, `.find_all()`, búsqueda dentro de etiquetas SVG.
❌ **Conceptos Prohibidos:** Ignorar los SVG, buscar solo en texto visible del body.

## Resultado Esperado en tu Terminal:

```text
[+] Código de estado: 200
[+] Código vectorial encontrado: VECTOR-99
```

Escribe tu código en `reto.py`. El arte también puede tener secretos en su código fuente.
