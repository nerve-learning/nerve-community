# Reto 103: Mudanza Extrema 🚚

Vamos a construir nuestra propia casa en una dirección de red completamente diferente, y probaremos que la magia externa funciona.

## Instrucciones

1. Crea un archivo llamado `nerve.config` **manualmente** (usando tu editor de código o terminal) en esta misma carpeta.
2. Dentro de ese archivo, escribe la siguiente configuración usando el formato JSON:
   - Haz que el puerto (`port`) sea `11111`.
   - Haz que la dirección IP (`host`) sea `"127.0.0.1"`.
   - Cierra el JSON correctamente con llaves `{}`.
3. Abre una **primera terminal**. Asegúrate de estar posicionado en esta misma carpeta (`103-configuracion-externa`) y ejecuta `nerve start`. Fíjate bien en el texto que imprime la terminal: debería decirte que está escuchando en el puerto 11111.
4. Escribe un script llamado `mi_mudanza.py`.
   - Crea un cliente Nerve.
   - Conéctalo con el nombre `"caja_fuerte"`.
   - Envíale un mensaje a `"yo_mismo"` con el texto `"¡Llegamos a la nueva casa!"`.
5. Abre una **segunda terminal** (también en esta carpeta) y ejecuta tu script.

### Conceptos Permitidos
- Formato JSON con `{}` y `" "`.
- Importar `NexusClient`.
- Enviar mensajes básicos.
- Ejecutar el Hub.

### Conceptos Prohibidos
- Pasar la dirección IP o el puerto directamente como parámetros de `NexusClient()` en Python. ¡Tu código Python debe permanecer ignorante de la dirección física!

### Resultado Esperado (Terminal 2 - Al ejecutar tu código)

Si no hay errores, tu programa se ejecutará sin imprimir nada (o lo que tú hayas decidido imprimir), pero en la **Terminal 1 (El Hub)** verás el evento de conexión en tu nuevo puerto personalizado. Si eliminaste el archivo `nerve.config`, fallaría la conexión porque tu cliente y el Hub estarían buscándose en lugares diferentes.
