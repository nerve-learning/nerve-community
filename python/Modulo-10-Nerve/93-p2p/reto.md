# Reto 93: Walkie-Talkies en la Base Lunar 🌕

¡La Agencia Espacial te necesita otra vez! Has aterrizado en la luna y necesitas establecer comunicación bidireccional (P2P) con el control de misión. 

Para que esta comunicación sea un éxito, crearás el software de las radios de comunicación que permite a los astronautas enviar y recibir alertas en tiempo real.

## Instrucciones Paso a Paso

1. Crea un archivo nuevo llamado `radio_lunar.py`.
2. Importa la clase `NexusClient` de `nerve`.
3. Construye tu antena y conéctate a la red con el nombre `"astronauta"`.
4. Define una función (tu recepcionista) llamada `auricular` que reciba el parámetro `datos`.
5. DENTRO del `auricular`, extrae la llave `"mensaje"` del diccionario `datos`.
6. Imprime el mensaje recibido así: `"\n[Tierra]: " + mensaje_recibido`.
7. FUERA de la función, contrata a tu recepcionista usando `.listen()`. **No uses paréntesis.**
8. Crea un bucle infinito usando `while True:`.
9. DENTRO del bucle, pídele al usuario que escriba un mensaje usando `input("Luna: ")` y guárdalo en una variable.
10. Aún DENTRO del bucle, arma un diccionario con la llave `"mensaje"` que contenga lo que el usuario escribió.
11. Envía ese diccionario directamente al nodo `"tierra"` usando `.send()`.

## 📜 Reglas de la Misión

**🟢 Conceptos Permitidos:**
- `NexusClient`, `.connect()`, `.listen()`, `.send()`
- Bucle infinito `while True:`
- `input()` y `print()`
- Diccionarios `{}`.
- Funciones `def` simples.

**🔴 Prohibido:**
- Poner el `.listen()` dentro del `while True:` (¡Causarías un colapso en la memoria de la base lunar!).
- Olvidar tener `nerve start` encendido en otra terminal.

## 🏆 Resultado Esperado en la Terminal

Al ejecutar `radio_lunar.py`, la terminal debería quedarse esperando a que escribas. Si otro compañero crea un programa similar pero conectado como `"tierra"`, ¡podrían chatear entre ustedes en tiempo real!

```text
Luna: Houston, hemos aterrizado.
Luna: Todo en orden por aquí.
Luna: 
[Tierra]: Recibido, astronauta. Buen trabajo.
Luna: 
```
