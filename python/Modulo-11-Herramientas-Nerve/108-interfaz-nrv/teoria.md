# Teoría: Monitores y Procesos Infinitos 📺

Nerve tiene dos comandos especiales para monitorear tu red. Pero a diferencia de comandos como `nerve pack` (que empacan y terminan su trabajo rápido), las herramientas de monitoreo son **Procesos Continuos**. Es decir, se quedan encendidos infinitamente para mostrarte cambios en vivo.

## 1. El Monitor de Terminal (El Panel Hacker)

`nerve monitor`

Si usas este comando, tu terminal dejará de ser una pantalla donde escribes comandos y se transformará en un tablero en vivo. Verás una lista de todos los programas conectados, cuánto tiempo llevan encendidos y cuántos datos (KB o MB) están moviendo.

## 2. El Dashboard Web (El Mapa Visual)

`nerve dashboard`

Si eres más visual, este comando levanta una pequeña página web dentro de tu propia computadora (sin internet). Solo tienes que ir a tu navegador favorito (Chrome, Firefox) y escribir: `http://localhost:8080`. 
Ahí verás una **Topología**, que es básicamente un grafo (un dibujo) con puntos conectados. En el centro estará Nerve y a su alrededor todos tus programas conectados. 

## 🧠 La Tecla Mágica: Ctrl + C

Como estos comandos nunca terminan por sí solos, tu programa de Python se quedará "trabado" (pausado) esperando a que terminen. 

¿Cómo le dices a un programa infinito que se detenga? ¡Con un freno de mano de emergencia! En todas las terminales del mundo, presionar las teclas **Ctrl y la letra C al mismo tiempo** (`Ctrl + C`) significa *"Corta y Cierra este proceso ahora mismo"*. 

## 🚨 ¿Qué pasa si me equivoco?

El error más común de los estudiantes aquí es ejecutar `nerve dashboard` y pensar que Python se rompió porque ya no sale código nuevo en la pantalla. ¡No está roto! Simplemente está ocupado manteniendo viva la página web. Si alguna vez sientes que la terminal se congeló, haz clic en ella y presiona `Ctrl + C` para recuperar el control.

Otro error es abrir el Dashboard y ver un mensaje de error que dice `Puerto ocupado`. Eso significa que tienes otra ventana o programa usando el puerto 8080. ¡Asegúrate de ejecutar un solo Dashboard a la vez!
