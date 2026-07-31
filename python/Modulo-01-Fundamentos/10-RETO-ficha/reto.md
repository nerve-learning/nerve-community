# El Gran Reto: Creador de Fichas RPG 🐉

## Tu Misión

Vas a crear un generador automático de "Fichas de Personaje" para un juego de rol. El programa debe hacerle preguntas al jugador, calcular algunas estadísticas y luego imprimir una tarjeta de presentación espectacular.

## Pasos obligatorios

Crea un archivo llamado `ficha_rpg.py` y asegúrate de que tu programa haga exactamente lo siguiente:

1.  **Imprime** un título de bienvenida llamativo (ej. "--- GENERADOR DE HÉROES ---").
2.  **Pide al usuario (con `input`)** los siguientes datos:
    *   El nombre de su personaje.
    *   La clase de su personaje (ej. Mago, Guerrero, Ladrón).
    *   Su nivel actual (un número entero).
    *   Su dinero inicial en monedas de oro (un número que puede tener decimales).
3.  **Transforma** (casteo) el nivel a `int` y el dinero a `float`.
4.  **Haz algunos cálculos mágicos**:
    *   Crea una variable llamada `vida_maxima`. Se calcula multiplicando el `nivel` por 15.
    *   Crea una variable llamada `poder_magico`. Se calcula dividiendo el `nivel` entre 2.
    *   El personaje debe pagar una "Tasa de Inscripción al Gremio" de 10.5 monedas. Réstale eso a su dinero inicial y guárdalo en una variable llamada `dinero_restante`.
5.  **Usa comentarios (`#`)** en tu código para explicar qué estás haciendo en cada sección (pedir datos, calcular stats, imprimir ficha).
6.  **Imprime la Ficha Final** usando `f-strings`. Debe verse bonita y ordenada, algo así:

```text
====================================
      FICHA DE PERSONAJE
====================================
Nombre: [Su nombre]
Clase: [Su clase]
Nivel: [Su nivel]
------------------------------------
Estadísticas:
Vida Máxima: [Su vida]
Poder Mágico: [Su poder]
Oro Restante: [Su dinero restante]
====================================
```

## ¿Cómo saber si ganaste?
Ejecuta tu archivo. Si te hace todas las preguntas, no explota con errores rojos, calcula correctamente la vida, el poder y el oro, y muestra la tarjeta bonita al final... **¡FELICIDADES! HAS COMPLETADO EL MÓDULO 1 DE PYTHON.**
