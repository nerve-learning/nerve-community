# Reto 07: Base64 Atributos 🔐

**URL del reto:** `https://nerve.community.aleniastudios.me/laberinto/c8c/crypt.html`

La página presenta citas históricas sobre criptografía clásica. Todo muy culto. Pero hay un elemento HTML que carga en silencio un atributo `data-secret` con un valor que **no es texto legible**: está codificado en Base64.

Tu misión es encontrar ese atributo oculto, decodificarlo y revelar el **token secreto**.

## Instrucciones Paso a Paso:

1. Importa `requests`, `BeautifulSoup`, y `base64`.
2. Haz un `requests.get()` a la URL del reto.
3. Parsea el HTML con BeautifulSoup.
4. Busca el elemento que tiene el atributo `data-secret` (inspecciona el HTML para identificarlo).
5. Extrae el valor del atributo: `elemento['data-secret']`.
6. Decodifica el valor de Base64 a texto normal:
   ```python
   texto = base64.b64decode(valor_b64).decode('utf-8')
   ```
7. Imprime el token decodificado.

> **Pista:** El atributo `data-secret` es un atributo personalizado HTML5. BeautifulSoup lo accede igual que cualquier atributo. El resultado decodificado es texto ASCII puro.

## Reglas Estrictas:
✅ **Conceptos Permitidos:** `requests`, `BeautifulSoup`, `base64`, `.get()` o `['attr']` para atributos, `base64.b64decode()`.
❌ **Conceptos Prohibidos:** Selenium (el atributo está en el HTML estático), decodificación manual caracter por caracter.

## Resultado Esperado en tu Terminal:

```text
[+] Código de estado: 200
[+] Atributo data-secret encontrado (raw): U1VQRVJFU0VDUkVUX1RPS0VOXzQy
[+] Token decodificado: SUPER_SECRET_TOKEN_42
```

Escribe tu código en `reto.py`. Los datos confidenciales raramente están en texto plano.
