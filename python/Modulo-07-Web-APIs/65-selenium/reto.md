# Reto 05: Trampas Visuales ✈️

**URL del reto:** `https://nerve.community.aleniastudios.me/laberinto/q9/honeypot_1.html`

Una agencia de viajes con cielos azules y palmeras. El usuario ve un precio bonito, pero el scraper ingenuo cae en una trampa: hay **múltiples elementos** con la clase `real-price` que contienen valores falsos. Solo uno, identificado por la clase adicional `actual-value`, tiene el precio correcto.

Este es un **honeypot**: una técnica real usada por sitios web para detectar y engañar a scrapers mal programados.

Tu misión es extraer el **precio real** sin caer en las trampas.

## Instrucciones Paso a Paso:

1. Importa `requests` y `BeautifulSoup`.
2. Haz un `requests.get()` a la URL del reto.
3. Parsea el HTML con BeautifulSoup.
4. **No uses** `.find_all(class_='real-price')` directamente, porque obtendrás múltiples resultados falsos.
5. Busca el elemento que tiene **ambas** clases: `real-price` y `actual-value`.
6. Extrae el texto de ese elemento específico.

> **Pista:** Puedes pasar una lista de clases a BeautifulSoup: `soup.find(class_=['real-price', 'actual-value'])`, o usar un selector CSS: `soup.select_one('.real-price.actual-value')`. El valor es un número decimal.

## Reglas Estrictas:
✅ **Conceptos Permitidos:** `requests`, `BeautifulSoup`, `.find()`, `.select_one()`, selección por múltiples clases CSS.
❌ **Conceptos Prohibidos:** Selenium, tomar el primer resultado sin verificar que es el correcto.

## Resultado Esperado en tu Terminal:

```text
[+] Código de estado: 200
[+] Precio real encontrado: 450.00
```

Escribe tu código en `reto.py`. El honeypot atrapa a los scrapers descuidados. Sé preciso.
