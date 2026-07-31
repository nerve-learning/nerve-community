# Reto 10: Fragmentación 📡

**URL del reto:** `https://nerve.community.aleniastudios.me/laberinto/p6p/omega.html`

La transmisión está interceptada. La pantalla muestra estática y ruido. Pero entre el caos, hay fragmentos de señal real. El mensaje ha sido **partido en múltiples piezas** con la clase `real-part`, dispersas entre docenas de elementos de ruido con la clase `noise`. Todo está oculto con `display: none`.

Tu misión: reunir todos los fragmentos reales en orden y reconstruir el **Protocolo Omega**.

## Instrucciones Paso a Paso:

1. Importa `requests` y `BeautifulSoup`.
2. Haz un `requests.get()` a la URL del reto.
3. Parsea el HTML con BeautifulSoup.
4. Usa `.find_all()` para encontrar **todos** los elementos con la clase `real-part`:
   ```python
   fragmentos = soup.find_all(class_='real-part')
   ```
5. Extrae el texto de cada fragmento y únelos en orden:
   ```python
   mensaje = ''.join(f.get_text() for f in fragmentos)
   ```
6. Imprime el mensaje reconstruido.

> **Pista:** El separador entre partes del mensaje forma parte del propio texto de cada fragmento. Cuando los concatenes en orden, el resultado será el protocolo completo. Ignora todo lo que tenga clase `noise`.

## Reglas Estrictas:
✅ **Conceptos Permitidos:** `requests`, `BeautifulSoup`, `.find_all()` con clase, `''.join()`, iteración con `for`.
❌ **Conceptos Prohibidos:** Selenium (los fragmentos están en el HTML estático), concatenar manualmente.

## Resultado Esperado en tu Terminal:

```text
[+] Código de estado: 200
[+] Fragmentos encontrados: 3
[+] Protocolo reconstruido: OMEGA-PROTOCOL-ACTIVATED
```

Escribe tu código en `reto.py`. Has llegado al final del laberinto. El Protocolo Omega está activado.

---

> **¿Completaste los 10 retos?** Visita el [Acceso a Fase Avanzada](https://nerve.community.aleniastudios.me/laberinto/store/cyberdeck.html) para continuar.
