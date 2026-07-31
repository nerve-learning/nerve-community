# Reto 04: Listas Anidadas 📜

**URL del reto:** `https://nerve.community.aleniastudios.me/laberinto/v2n/layout_b.html`

La página muestra un poema existencial sobre el código. Bonito, reflexivo... y completamente una distracción. Enterrada dentro de la estructura HTML hay una lista anidada oculta con `display: none` que contiene el dato real.

Tu misión es navegar por la jerarquía de listas (`ul > li > ul > li`) para extraer el **código de identificación** escondido en las profundidades.

## Instrucciones Paso a Paso:

1. Importa `requests` y `BeautifulSoup`.
2. Haz un `requests.get()` a la URL del reto.
3. Parsea el HTML con BeautifulSoup.
4. Localiza el contenedor con clase `secret-structure` (está con `display: none`).
5. Dentro de ese contenedor, navega por la estructura de listas anidadas hasta encontrar el elemento con el dato.
6. Extrae el texto y muéstralo.

> **Pista:** Usa `select()` con selectores CSS como `.secret-structure li` para encontrar todos los items de lista dentro del contenedor secreto. El valor que buscas sigue el patrón `XXXX-999-X`.

## Reglas Estrictas:
✅ **Conceptos Permitidos:** `requests`, `BeautifulSoup`, `.find()`, `.find_all()`, `.select()` con selectores CSS, `.get_text()`.
❌ **Conceptos Prohibidos:** Selenium (el dato está en el HTML estático).

## Resultado Esperado en tu Terminal:

```text
[+] Código de estado: 200
[+] Código de identificación: ZETA-991-A
```

Escribe tu código en `reto.py`. Las listas anidadas son un laberinto, pero los selectores CSS son tu mapa.
