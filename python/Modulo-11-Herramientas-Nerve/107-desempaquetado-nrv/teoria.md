# Teoría: Enseñándole Trucos a tu Computadora 🧠

Tu computadora no sabe por defecto qué hacer cuando ve un archivo que termina en `.nrv`. Cuando haces doble clic, te pregunta: *"¿Con qué programa quieres abrir esto?"*. 

Nerve tiene dos comandos especiales pensados exclusivamente para darle comodidad a los humanos (y no solo a los programadores).

## 1. La Asociación (El Doble Clic)

Podemos darle una orden a nuestro mayordomo Nerve para que hable con tu sistema operativo (Windows, Mac o Linux) y le diga: *"Oye, los archivos .nrv son míos. Ponles mi ícono y cuando alguien les haga doble clic, llámame"*.

`nerve associate`

### 🧠 Anatomía del Comando
* `nerve`: Nuestro querido mayordomo.
* `associate`: La orden que significa "Asociar" o "Vincular".

Una vez que haces esto, puedes usar el ratón para abrir tus cajas fuertes sin tocar código. *(Nota: Si alguna vez quieres deshacer esto, existe su hermano gemelo: `nerve unassociate`)*.

## 2. La Apertura Interactiva (La Puerta Amable)

A veces no quieres hacer doble clic, pero tampoco quieres escribir la clave directo en el código (porque alguien podría espiar tu pantalla). Para eso existe el comando "Abrir".

`nerve open mi_archivo.nrv`

### 🧠 Anatomía del Comando
* `open`: Significa "Abrir". 
* `mi_archivo.nrv`: El cofre que quieres desencriptar.

¡Ojo! Aquí **no** pusimos la variable de entorno con la contraseña. Al usar `open`, Nerve detecta que eres un humano y pausará todo. Si estás en una terminal, te pedirá que escribas la clave ahí mismo de forma segura. Si tienes entorno gráfico, abrirá una ventanita bonita pidiendo la clave. 

## 🚨 ¿Qué pasa si me equivoco?

El error más común al usar `nerve open` es desesperarse cuando pide la clave. Nerve te dará exactamente **3 intentos**. Si te equivocas las 3 veces, Nerve cerrará el programa de golpe para proteger el archivo de ataques. Además, cuando escribas tu clave en la terminal, los caracteres no se verán en pantalla (¡parecerá que el teclado está roto, pero es por tu seguridad!). Tú escribe y presiona Enter.
