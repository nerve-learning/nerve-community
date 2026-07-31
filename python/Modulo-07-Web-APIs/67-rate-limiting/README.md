# Nivel 67: Sé Educado (Rate Limiting) 🚦

Ahora que sabes usar `requests` para descargar datos de Internet, y dominas los bucles `for` del Módulo 4, podrías sentir la tentación de hacer esto:

```python
for i in range(10000):
    requests.get("https://api.ejemplo.com")
```

Para tu computadora, esto toma solo unos segundos. Pero para el servidor (la computadora que recibe el mensaje), ¡es un ataque! Si miles de estudiantes hacen lo mismo, el servidor podría colapsar y apagarse.

Para protegerse, los servidores de Internet tienen un mecanismo de defensa llamado **Rate Limiting** (Límite de velocidad). Si detectan que pides las cosas demasiado rápido, te bloquean temporalmente o banean tu dirección de Internet (IP) para siempre.

Hoy aprenderemos a ser "buenos ciudadanos" del Internet, programando nuestros códigos para que tengan paciencia y no molesten a los servidores.

## Tu ruta de aprendizaje hoy:
1. **Teoría (`teoria.md`)**: El cantinero enojado y el temido código `429`.
2. **Ejemplo (`ejemplo.py`)**: Veremos cómo un servidor nos castiga, y cómo programar un bucle "educado" que respira entre cada petición.
3. **Reto (`reto.md`)**: Programarás un semáforo inteligente que sepa exactamente cuándo detenerse si el servidor se enoja.

¡Aprende a frenar antes de que te multen!
