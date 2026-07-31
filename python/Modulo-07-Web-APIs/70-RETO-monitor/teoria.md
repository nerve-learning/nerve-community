# Teoría: La Anatomía de un Monitor 👁️

Imagina a un guardia de seguridad nocturno en un museo. 
No mira un cuadro una sola vez y se va a su casa. Su trabajo consiste en hacer "rondas": camina por el pasillo, revisa las puertas, espera un rato, y vuelve a empezar.

Un **Monitor Web** hace exactamente lo mismo. Está compuesto por 4 piezas fundamentales que hemos ido aprendiendo a lo largo de este curso:

### 1. El Motor Eterno (`while True`)
Viene del Módulo 4. Un monitor nunca debe detenerse a menos que nosotros lo apaguemos manualmente. El bucle `while True:` crea un ciclo infinito que repetirá nuestra lógica por siempre.

### 2. Los Ojos (`requests.get`)
Viene del Módulo 7. Necesitamos que nuestro bot pueda "ver" el estado actual del mundo. Hace peticiones a una URL para traer los datos más frescos.

### 3. El Cerebro (`if / else`)
Viene del Módulo 2. El bot debe comparar lo que acaba de ver con lo que consideramos "normal". Si el `status_code` es 200, todo está bien. Si es otro, suena la alarma.

### 4. El Freno (`time.sleep`)
Viene de los Niveles 65 y 67. **ESTA ES LA PIEZA MÁS CRÍTICA.** 
Si haces un `while True:` haciendo peticiones a un servidor SIN usar `time.sleep()`, tu computadora enviará miles de peticiones por segundo. ¡Estarías cometiendo un ataque cibernético (DDoS) sin querer! El freno le da paz al servidor y a tu CPU.

---

## ¿Qué pasa si me equivoco? (El Panel de Errores)

**Error 1: Tu computadora empieza a sonar fuerte (los ventiladores) y te banean la IP**
- **Por qué pasa:** Olvidaste poner el `time.sleep()` dentro del `while True`. Tu script está atacando la página web a la velocidad de la luz.
- **Solución:** ¡Presiona `Ctrl + C` en tu terminal inmediatamente para matar el programa! Revisa tu código y asegúrate de que el freno de tiempo exista y esté bien indentado.

**Error 2: El script hace una sola revisión y se queda dormido para siempre**
- **Por qué pasa:** Pusiste el `time.sleep()` pero olvidaste poner la lógica dentro de un bucle `while True` o un `for`. 
- **Solución:** Revisa tu indentación. Todo el proceso (ojos, cerebro y freno) debe estar "metido" (tabulado) dentro del `while`.
