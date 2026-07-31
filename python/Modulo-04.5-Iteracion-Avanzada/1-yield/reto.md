# Reto 1: La Máquina de Turnos 🎟️

El hospital del barrio necesita un sistema de turnos. Cada vez que el médico llama a un paciente, la máquina entrega el siguiente número. La máquina no genera todos los turnos de golpe (no sabe cuántos pacientes vendrán), sino que los produce **uno a la vez, bajo demanda**.

## Instrucciones Paso a Paso:

1. Crea una función llamada `maquina_turnos` que reciba un número llamado `inicio`.
2. Dentro de la función, crea una variable `turno` que empiece con el valor de `inicio`.
3. Crea un bucle `while True:` (recuerda: esto significa "repite para siempre").
4. Dentro del `while`, usa `yield turno` para entregar el turno actual.
5. Después del `yield`, suma 1 a `turno` para que el próximo sea el siguiente número.
6. En tu programa principal, crea la máquina llamando a `maquina_turnos(1)` y guárdala en una variable llamada `consultorio`.
7. Usa `next()` exactamente **5 veces** para simular que llegan 5 pacientes, imprimiendo cada turno con el formato del resultado esperado.

> **Pista:** Un `while True:` con `yield` adentro nunca lanza `StopIteration` porque nunca termina la función. El `yield` la pausa indefinidamente hasta que le pidas el siguiente. Como un rollo de turnos infinito.

## Reglas Estrictas:
✅ **Conceptos Permitidos:** `def`, `yield`, `while`, `next()`, variables, suma con `+`, `print()`, f-strings.
❌ **Conceptos Prohibidos:** Clases, `import`, `range()` como solución principal, listas para guardar los turnos.

## Resultado Esperado en tu Terminal:

```text
🏥 Sistema de Turnos — Consultorio 1

Llamando al paciente con turno: 1
Llamando al paciente con turno: 2
Llamando al paciente con turno: 3
Llamando al paciente con turno: 4
Llamando al paciente con turno: 5
```

Crea tu código en un archivo llamado `reto.py`. Si tu máquina puede seguir entregando turnos más allá del 5 con solo agregar más `next()`, lo hiciste bien.
