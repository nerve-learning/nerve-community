# Reto 08: JSON Incrustado 👤

**URL del reto:** `https://nerve.community.aleniastudios.me/laberinto/9x2/profile.html`

Una tarjeta de perfil de usuario. Todo parece normal: avatar, nombre, información básica. Pero el **dato real** no está en el DOM visible. Está dentro de un bloque `<script type="application/json">`: un JSON incrustado directamente en el HTML, un patrón común en sitios modernos que pre-cargan datos para JavaScript.

Tu misión es encontrar ese bloque de script, parsearlo como JSON, y extraer el **correo electrónico** del perfil.

## Instrucciones Paso a Paso:

1. Importa `requests`, `BeautifulSoup`, y `json`.
2. Haz un `requests.get()` a la URL del reto.
3. Parsea el HTML con BeautifulSoup.
4. Encuentra el `<script>` con `type="application/json"`:
   ```python
   script_tag = soup.find('script', type='application/json')
   ```
5. Extrae el texto del tag y parsea el JSON:
   ```python
   data = json.loads(script_tag.string)
   ```
6. Navega el diccionario para encontrar el campo `email` y muéstralo.

> **Pista:** El JSON tiene una estructura anidada. Puede ser algo como `data['user']['contact']['email']` o similar. Inspecciona el JSON completo primero con `print(data)` para entender la estructura.

## Reglas Estrictas:
✅ **Conceptos Permitidos:** `requests`, `BeautifulSoup`, `json`, `.find()` con `type`, `json.loads()`, acceso a diccionarios anidados.
❌ **Conceptos Prohibidos:** Selenium, expresiones regulares para parsear JSON (usa `json.loads` siempre).

## Resultado Esperado en tu Terminal:

```text
[+] Código de estado: 200
[+] Email encontrado en JSON incrustado: scraper@aleniastudios.me
```

Escribe tu código en `reto.py`. El JSON dentro del HTML es más común de lo que crees.
