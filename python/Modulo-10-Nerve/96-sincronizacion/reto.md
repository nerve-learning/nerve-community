# Reto Nivel 96: La To-Do List Inmortal

Hasta ahora sincronizamos un simple texto (un color). Pero el verdadero poder de la sincronización brilla cuando usamos estructuras de datos más complejas, como las **listas**.

Tu misión es construir un programa de consola que mantenga una lista de tareas (To-Do List) compartida entre todos los nodos.

## Instrucciones

1. Crea un script llamado `reto.py`.
2. Define una variable global llamada `lista_tareas` y asígnale una lista vacía `[]`.
3. Al conectarse, tu nodo debe enviar un mensaje pidiendo sincronización:
   `{"accion": "pedir_tareas"}`
4. En tu función de escucha (`al_recibir_mensaje`):
   - Si recibes `"pedir_tareas"` y tu `lista_tareas` tiene al menos 1 elemento (usa `len()`), responde con `"enviar_tareas"` y pásale tu lista en los datos.
   - Si recibes `"enviar_tareas"`, actualiza tu `lista_tareas` global.
   - Si recibes `"nueva_tarea"`, agrega el texto a tu lista usando `.append()`.
5. En tu bucle infinito:
   - Imprime todas las tareas actuales (puedes usar un bucle `for`).
   - Pídele al usuario que escriba una nueva tarea.
   - Agrega la tarea a tu `lista_tareas` usando `.append()`.
   - Transmite un mensaje con `"accion": "nueva_tarea"` y los datos de la tarea escrita.

## El Escenario de Prueba

- Abre una terminal y corre el script. Agrega "Comprar leche" y "Pasear al perro".
- Abre **otra** terminal (mientras la primera sigue corriendo) y corre el script de nuevo con otro nombre.
- El segundo script debería decir: *"¡Sincronizando!"* y mágicamente imprimir "Comprar leche" y "Pasear al perro" sin que tú escribas nada en esa ventana.

¡Si logras esto, acabas de crear tu primera base de datos distribuida en memoria RAM!
