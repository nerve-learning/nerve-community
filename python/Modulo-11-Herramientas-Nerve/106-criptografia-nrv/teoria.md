# Teoría: La Licuadora Matemática 🌪️

Cuando usas `nerve pack`, Nerve no solo mete tus archivos en una caja. Usa una técnica llamada **Criptografía** (esconder mensajes con matemáticas). Nerve usa dos guardianes con nombres raros, pero que son muy fáciles de entender:

1. **AES-256-GCM (La puerta irrompible)**: Imagina un candado con 256 pernos diminutos. Probar todas las combinaciones a mano o incluso con computadoras le tomaría a los malos millones de años.
2. **Argon2id (El guardián lento)**: Los hackers usan programas de "fuerza bruta" que prueban contraseñas a la velocidad de la luz. Argon2id es una trampa de arena: hace que probar cada contraseña sea súper agotador y lento para el programa atacante. En vez de probar un millón por segundo, lo frena en seco.

Pero nada de esto sirve si tu llave (tu contraseña) es `"perrito123"`. Necesitamos una llave fuerte.

## 🔑 Forjando la llave perfecta

Para crear llaves, usamos nuestro mayordomo de terminal con un comando nuevo de Nerve: `nerve genpass`.

### Anatomía del Comando

`nerve genpass --mode random`

* `nerve`: Nuestro mayordomo de siempre.
* `genpass`: La orden "Genera Password" (crea una contraseña).
* `--mode`: Una **Bandera (Flag)**. Los dos guiones medios (`--`) le dicen a la terminal: "Atención, voy a darte una instrucción extra sobre CÓMO quiero que hagas el trabajo". "Mode" significa "Modo".
* `random`: La opción que elegimos para el modo. Significa "Aleatorio". Generará algo como `x!8Kz9pL@2`.

¿Esos símbolos son muy difíciles de recordar? ¡Nerve tiene otro modo!

`nerve genpass --mode passphrase`

* `passphrase`: Significa "Frase secreta". Nerve tomará palabras de un diccionario especial y creará una pequeña historia al azar, como `gato-astronave-feliz-corriendo`. Es fácil de recordar para un humano, pero matemáticamente imposible de adivinar para un robot.

## 🚨 ¿Qué pasa si me equivoco?

El error más común es escribir `--mode` con un solo guión (`-mode`) o pegar palabras incorrectas en la orden. Si lo haces, la terminal dirá algo como "Comando no reconocido" o simplemente ignorará tu orden y usará su modo por defecto. ¡Recuerda siempre poner los dos guiones para las instrucciones especiales (banderas)!
