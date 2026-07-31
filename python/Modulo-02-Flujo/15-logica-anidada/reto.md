# Reto 15: La Agencia Espacial 🚀🧑‍🚀

Eres el reclutador jefe de la agencia espacial. Estás evaluando candidatos para ir a Marte. 
El proceso tiene dos fases muy estrictas. Primero evalúas la salud física. Solo si pasan esa prueba, los pasas al examen psicológico.

## Instrucciones

1. Crea las siguientes variables para tu candidato:
   * `salud_optima` (un booleano, ej. `True`).
   * `puntuacion_psicologica` (un número entero del 0 al 100, ej. `95`).

2. **Filtro 1 (Físico)**: Crea un `if` que verifique si `salud_optima` es verdadera (`True`).
   * Si es falsa, el `else` externo debe imprimir: `"Rechazado en fase 1: No cumple los requisitos físicos."`

3. **Filtro 2 (Psicológico - ¡Anidado!)**: Si el candidato sí tiene buena salud (adentro de tu primer `if`), crea **otro `if`** que verifique si su `puntuacion_psicologica` es mayor o igual a `90`.
   * Si es mayor o igual a 90, imprime (a 8 espacios de sangría): `"¡Felicidades! Eres el nuevo astronauta para ir a Marte."`
   * Si es menor (el `else` interno), imprime: `"Rechazado en fase 2: Excelente físico, pero no pasó el test psicológico."`

### Conceptos permitidos
- Variables (asignación con `=`).
- Tipos de datos (`int`, `bool`).
- Operadores de comparación (`>=`, `==`).
- Estructura condicional anidada (un `if`/`else` dentro de otro `if`/`else`).
- Indentación múltiple (4 y 8 espacios).
- `print()`.

### Conceptos prohibidos
- El operador `and`. Aquí queremos ver claramente los dos niveles de rechazo (fase 1 y fase 2), por lo que DEBES usar un `if` dentro de otro `if`.
- Ciclos (`for`, `while`).

### Resultado esperado en terminal
Si configuras `salud_optima = True` y `puntuacion_psicologica = 85`, al correr tu código la terminal debe mostrar exactamente esto:

```text
Rechazado en fase 2: Excelente físico, pero no pasó el test psicológico.
```

Si cambias a `salud_optima = False` (sin importar el puntaje psicológico), debe mostrar:

```text
Rechazado en fase 1: No cumple los requisitos físicos.
```
