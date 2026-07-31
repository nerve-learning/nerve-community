# Reto 115: El Tamagotchi de Red 🦖

Tu empresa de juguetes te ha pedido programar el cerebro de un nuevo Tamagotchi conectado por Nerve.
El Tamagotchi recibe comandos por red de sus dueños, pero necesita un **Estado** para no morir de hambre o aburrimiento.

### 📝 Instrucciones:

1. Crea un archivo Python. (Recuerda tener `alenia-nerve` instalado).
2. Afuera de cualquier función, crea el "cerebro" del Tamagotchi: un diccionario llamado `estado_tamagotchi`. 
   - Debe tener la etiqueta `"hambre"` iniciando en `50`.
   - Debe tener la etiqueta `"felicidad"` iniciando en `50`.
3. Crea una función `procesar_comando(payload)`. El `payload` que llegará será un simple texto (String), por ejemplo `"alimentar"` o `"jugar"`.
4. Dentro de la función, si el payload es `"alimentar"`, réstale `10` al hambre de tu estado e imprime: `🍕 Tamagotchi comio. Hambre actual: [numero]`.
5. Si el payload es `"jugar"`, súmale `10` a la felicidad de tu estado e imprime: `⚽ Tamagotchi jugo. Felicidad actual: [numero]`.
6. Crea el Hub, crea el Cliente (llámalo `"tamagotchi"`), conéctalo y ponlo a escuchar (`listen`).
7. Usando el mismo cliente, simula enviarte mensajes a ti mismo (`cliente.send(to="tamagotchi", payload="alimentar")`). 
   - Envíale: `"alimentar"`, luego `"alimentar"`, y luego `"jugar"`.
   - Usa `time.sleep(1)` entre los envíos para que no se atropellen los mensajes en pantalla.

### ⛔ Reglas Estrictas:
* **Permitido**: Crear diccionarios globales, condicionales `if`, sumas/restas, funciones, instancias de `NexusHub` y `NexusClient`.
* **Prohibido**: Poner el diccionario `estado_tamagotchi` ADENTRO de la función. Si lo haces, tu mascota sufrirá de amnesia y su hambre se reiniciará en cada mensaje.

### 🎯 Resultado Esperado en la Terminal:
```text
🍕 Tamagotchi comio. Hambre actual: 40
🍕 Tamagotchi comio. Hambre actual: 30
⚽ Tamagotchi jugo. Felicidad actual: 60
```
