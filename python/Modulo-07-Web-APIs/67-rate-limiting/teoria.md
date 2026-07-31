# Teoría: El Cantinero Enojado 🍻

Imagina que una API es un cantinero en un bar.
Si te acercas a la barra y le pides un vaso de agua, te lo sirve feliz (Código `200 OK`). Si vuelves a los 5 minutos por otro, no hay problema.

Pero si te paras frente a él y le gritas: *"¡Dame agua! ¡Dame agua! ¡Dame agua!"* 100 veces en un solo segundo, el cantinero se va a enojar. Te pondrá la mano en la cara y te dirá: *"¡Cálmate! Siéntate en esa silla 5 minutos antes de volver a pedir algo"*.

En Internet, ese castigo tiene un número oficial.

### El temido Código 429
Cuando sobrepasas el límite de peticiones permitidas por un servidor, este rechaza tu conexión y te devuelve un `status_code` igual a **429 (Too Many Requests / Demasiadas Peticiones)**.

Si sigues enviando peticiones ignorando el `429`, el servidor podría banear tu IP permanentemente.

### La Solución: Pausas Tácticas (`time.sleep`)
En el Módulo 6 vimos de pasada la herramienta `time`. En el Nivel 65 la usamos para que Selenium no fuera tan rápido. Aquí es nuestra herramienta principal de cortesía.

La regla de oro del Web Scraping y el consumo de APIs es: **Siempre pon a dormir a tu programa al menos 1 segundo entre cada petición dentro de un bucle.**

```python
import time
import requests

for i in range(5):
    requests.get("https://mi-api.com")
    time.sleep(1) # ¡El programa se congela 1 segundo y el servidor respira!
```

---

## ¿Qué pasa si me equivoco? (El Panel de Errores)

**Error 1: Obtienes un código de estado `403 Forbidden` después de recibir varios `429`**
- **Por qué pasa:** El servidor te advirtió que ibas muy rápido (`429`), pero tu bucle `for` no tenía pausas y seguiste martillando el servidor. El cantinero se hartó y te expulsó del bar permanentemente (`403`).
- **Solución:** ¡Nunca lances un bucle `for` de peticiones sin probarlo primero con pocas repeticiones y usando `time.sleep()`!
