# Reto 119: La Torre de Control Separada 🗼

Es hora de graduarte y usar Nerve exactamente como se usa en servidores de producción profesionales. Ya no tendrás el cerebro y los músculos en el mismo archivo.

### 📝 Instrucciones:

1. En la misma carpeta donde estás trabajando, crea un archivo de texto simple (no `.py`, sino extensión `.config`) y llámalo EXACTAMENTE `nerve.config`.
2. Escribe adentro lo siguiente y guárdalo:
   `port=7777`
3. Abre una **nueva terminal** en esta misma carpeta y ejecuta el comando de la herramienta:
   `nerve start`
   *(Verás que la terminal te avisa que está usando el puerto 7777, porque leyó tu archivo mágico automáticamente).*
4. Crea tu archivo Python para el reto. Importa **SOLAMENTE** `NexusClient` y `time`. ¡Ni se te ocurra importar `NexusHub`!
5. Crea un cliente llamado `"torre_control"` y ponlo a escuchar (`listen`) con una función que imprima el payload.
6. Crea un cliente llamado `"avion_01"` y haz que envíe un mensaje a la torre: `{"mensaje": "Solicito permiso para aterrizar"}`.
7. Haz que tu código espere 2 segundos (`time.sleep`) y desconecta ambos clientes.
8. Corre tu código de Python en **OTRA terminal** (no en la que está corriendo el Hub).

### ⛔ Reglas Estrictas:
* **Permitido:** Crear `nerve.config`, usar `nerve start` en terminal, instanciar `NexusClient()`.
* **Prohibido:** Escribir `hub = NexusHub()` en tu código Python. Si lo haces, has roto la regla de oro de la Arquitectura Desacoplada y habrás reprobado.
* **Prohibido:** Correr el código de Python antes de iniciar el Hub. ¡El avión se estrellará por falta de conexión!

### 🎯 Resultado Esperado en la Terminal:
**En la Terminal 1 (La del Hub):**
```text
[NERVE CLI] Initializing Nerve Hub...
```
*(Verás un banner morado genial y registros de cómo los clientes se conectan y desconectan en tiempo real).*

**En la Terminal 2 (La de tu código Python):**
```text
🗼 [TORRE] Mensaje recibido: {'mensaje': 'Solicito permiso para aterrizar'}
```
