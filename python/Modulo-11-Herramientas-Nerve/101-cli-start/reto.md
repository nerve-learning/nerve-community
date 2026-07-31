# Reto 101: Ojos en la Espalda 👀

Es hora de comprobar si puedes operar tanto el Hub como tus programas Python al mismo tiempo, y usar las herramientas del sistema para rastrear lo que sucede bajo la superficie.

## Instrucciones

1. Abre tu **primera terminal** (esta será tu sala de servidores).
2. Asegúrate de tener activado tu entorno virtual (donde instalaste `alenia-nerve`).
3. Inicia el Hub en modo espía usando la bandera `--verbose`.
4. Deja esa terminal abierta y visible en una mitad de tu pantalla.
5. Abre una **segunda terminal**.
6. Escribe un script en Python llamado `mi_reto.py` que haga lo siguiente:
   - Se conecte a la red con el nombre `"estudiante_curioso"`.
   - Utilice un bucle `while` para enviar **10** mensajes al destino `"servidor_central"`.
   - Cada mensaje debe ser un diccionario que diga `{"mensaje": "Hola Hub", "numero_de_intento": i}`.
   - Debe usar `time.sleep(2)` para esperar 2 segundos entre cada envío.
7. Ejecuta tu script en la segunda terminal.
8. ¡Mantén tus ojos en la **primera terminal**! Deberás ver cómo el Hub detecta la conexión de `estudiante_curioso`, imprime en pantalla los paquetes JSON que estás enviando, y luego detecta cuando el programa se cierra.

### Conceptos Permitidos
- Importar `NexusClient` y `time`.
- Bucles `while` y variables.
- Diccionarios `{}`.
- Comandos CLI: `nerve start --verbose`.

### Conceptos Prohibidos
- Usar clases o POO.
- Ejecutar los programas sin tener dos terminales abiertas.

### Resultado Esperado (Terminal 1 - El Hub)

```text
[Nerve] Hub inicializado. Escuchando conexiones...
[Nerve] Nuevo cliente registrado: estudiante_curioso
[Nerve] [Ruteo] De estudiante_curioso -> A servidor_central: {"mensaje": "Hola Hub", "numero_de_intento": 1}
[Nerve] [Ruteo] De estudiante_curioso -> A servidor_central: {"mensaje": "Hola Hub", "numero_de_intento": 2}
...
[Nerve] Cliente desconectado: estudiante_curioso
```
