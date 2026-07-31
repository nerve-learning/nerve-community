# Reto Nivel 98: La Fortaleza 🏰

Es hora de poner en práctica las buenas costumbres del despliegue profesional. Vamos a asegurar nuestra red sin escribir contraseñas en nuestro código de Python.

## Instrucciones

1. En esta misma carpeta, crea un archivo nuevo de texto llamado **exactamente** `nerve.config`.
2. Adentro de ese archivo, escribe tu llave secreta, por ejemplo:
   `auth_token=patito_de_goma`
   (Guarda el archivo).
3. Crea un script llamado `hub_fortaleza.py`.
   - Importa `NexusHub`.
   - Instáncialo sin argumentos: `hub = NexusHub()`
   - Arranca el Hub: `hub.start()`
   - Como creaste el archivo `nerve.config`, el Hub automáticamente absorberá esa contraseña de ahí.
4. Crea otro script llamado `cliente_legal.py`.
   - Importa `NexusClient`.
   - Instáncialo sin argumentos: `cliente = NexusClient()`
   - Conéctate: `cliente.connect("infiltrado")`
   - Manténlo vivo con un bucle `while True: time.sleep(1)`.
5. Ejecuta el Hub en una terminal, y en otra ejecuta el cliente.

## Reglas Estrictas

- **Permitido:** Crear el archivo `nerve.config`, instanciar Hub y Client sin pasarles nada entre los paréntesis `()`.
- **Prohibido:** Usar `auth_token="..."` adentro de tu código de Python.

## El Escenario de Prueba

1. Corre el Hub (verás que se enciende).
2. Corre el Cliente (deberías conectarte con éxito, porque tu cliente también lee el mismo `nerve.config` que el Hub por estar en la misma carpeta).
3. **La prueba final:** Mueve el archivo `nerve.config` a otra carpeta temporalmente, o cámbiale el nombre a `nerve_roto.config`. Trata de correr el cliente de nuevo.
   
¡Deberías ser expulsado instantáneamente por el Hub porque ya no tienes el pase VIP!

```text
[NERVE] Connected to hub as 'infiltrado' failed (auth).
```
