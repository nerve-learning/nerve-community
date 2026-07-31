# Teoría: La Caja Fuerte y el Mayordomo 🎩

Cuando instalaste `alenia-nerve`, también trajiste a tu computadora una herramienta poderosa en la terminal (tu mayordomo). Puedes pedirle que empiece a escuchar (`nerve start`), pero también puedes pedirle que proteja cosas (`nerve pack`).

Para proteger una carpeta, usamos un comando especial en la terminal. Como ya sabes usar el módulo `os` de Python (¡del Módulo 6!), podemos darle órdenes a la terminal directamente desde nuestro código.

## 🧠 Anatomía del Comando

El comando en la terminal se ve así:

`NERVE_NRV_PASSWORD="mi_clave" nerve pack mi_carpeta cofre.nrv`

Vamos a desmontarlo pieza por pieza:

* `NERVE_NRV_PASSWORD=` : Esto es una **Variable de Entorno**. Imagina que le susurras la contraseña al oído a la terminal *solo* por un segundo. Esto es mucho más seguro que escribirla donde todos puedan verla en la pantalla por siempre. El signo `=` indica que le estamos guardando (asignando) un valor a esa palabra.
* `"mi_clave"` : Las comillas dobles rodean tu contraseña. Siempre usa comillas por si tu clave tiene espacios adentro, así la terminal sabe exactamente dónde empieza y dónde termina.
* `nerve` : Llamamos a nuestro mayordomo de Alenia.
* `pack` : La orden exacta. Significa "empaca" o "comprime y encripta".
* `mi_carpeta` : La caja de cartón que tiene los archivos que queremos proteger (el **origen**).
* `cofre.nrv` : El nombre de la caja fuerte impenetrable que Nerve va a crear (el **destino**). La extensión `.nrv` es simplemente la etiqueta que le dice a tu computadora "esto es un archivo seguro de Nerve".

Para abrir el cofre, el comando es casi igual, pero al revés:

`NERVE_NRV_PASSWORD="mi_clave" nerve unpack cofre.nrv carpeta_salida`

Aquí `unpack` significa "desempaca". Primero ponemos la caja fuerte y luego la carpeta donde queremos sacar todo.

## 🚨 ¿Qué pasa si me equivoco?

El error más común aquí de los estudiantes es olvidar la contraseña. Si intentas desempacar (`unpack`) un archivo `.nrv` y la variable `NERVE_NRV_PASSWORD` no es *exactamente* la misma que usaste para empacar, Nerve te devolverá un error. 
En la terminal verás un aviso de "fallo de desencriptación" o, si te equivocas al escribir el comando, la terminal te pedirá la contraseña de forma interactiva esperando que la escribas. ¡Guarda bien esa llave y escríbela con cuidado!
