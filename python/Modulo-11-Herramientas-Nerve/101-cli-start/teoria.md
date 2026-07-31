# Teoría: La CLI y el Ojo que Todo lo Ve 👁️

Imagina que Nerve es un motor de automóvil. Los cables y engranajes están ocultos debajo del capó. Cuando instalaste `alenia-nerve`, no solo obtuviste herramientas para usar en tus scripts de Python, también instalaste una **CLI** (Command Line Interface o Interfaz de Línea de Comandos).

La CLI es como el panel de control del automóvil. Te permite encender el motor desde tu terminal escribiendo comandos que empiezan con la palabra `nerve`.

## Anatomía de `nerve start`

Cuando abres una terminal y escribes:

```bash
nerve start
```

Estás dando una orden directa al sistema: **"Enciende la Oficina de Correos Central (El Hub)"**.
- `nerve`: Llama al programa maestro de Nerve.
- `start`: Es la acción o sub-comando. Le dice a Nerve que inicie el enrutador principal en tu computadora.

Una vez que presionas Enter, el Hub cobra vida y se queda esperando a que los programas (clientes) se conecten a él.

## El Modo Espía: `--verbose`

Normalmente, el Hub trabaja en silencio. No te avisa de cada pequeña carta que reparte porque, si recibes 10,000 cartas por segundo, la pantalla se llenaría de texto inútil y la computadora se pondría lenta.

Pero a veces, cuando estamos construyendo programas, *queremos ver* qué está pasando exactamente. Queremos ver si el mensaje llegó y qué contenía. Para eso usamos las **banderas** (flags).

```bash
nerve start --verbose
```

- `--verbose`: Viene de la palabra "verborrea" (hablar mucho). Le dice al Hub: *"Quiero que me cuentes ABSOLUTAMENTE TODO lo que haces en voz alta"*.

Cuando enciendes el Hub en modo `--verbose`, verás en la pantalla un registro (log) cada vez que un programa se conecta, se desconecta o envía un mensaje. Es nuestra herramienta de rayos X para saber si nuestra red funciona.

## ¿Qué pasa si me equivoco?

**El error más común:** Intentar ejecutar el archivo `ejemplo.py` *antes* de haber encendido el Hub con `nerve start`. 
**¿Qué verás?** Python lanzará un error rojo gigante que dice `ConnectionRefusedError`. 

**La regla de oro:** El Hub siempre debe ser el primero en despertar, y el último en ir a dormir. Si cierras la terminal donde corre el Hub (presionando `Ctrl+C`), el corazón se detiene y todos tus programas Python se quedarán sin poder comunicarse.
