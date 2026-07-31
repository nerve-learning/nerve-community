# Reto 19: El Limpiador de Código 🧹✨

Te han contratado como Ingeniero Senior en una empresa de videojuegos. Tu primer trabajo es revisar el código que dejó el becario. Él escribió un sistema para decidir si un jugador gana un trofeo especial, pero usó demasiadas líneas y es muy difícil de leer.

Tu misión es **optimizar** este código aplicando las tres reglas de oro:
1. Aplanar nidos.
2. Asignación directa.
3. Quitar el `== True`.

## Instrucciones

1. Este es el código del becario. Cópialo en tu archivo y obsérvalo.
```python
puntos = 150
tiempo_segundos = 45
enemigos_derrotados = True

# PARTE 1: Calcular si superó el nivel
if puntos > 100:
    if tiempo_segundos < 60:
        supero_nivel = True
    else:
        supero_nivel = False
else:
    supero_nivel = False

# PARTE 2: Entregar el trofeo
if supero_nivel == True:
    if enemigos_derrotados == True:
        print("¡Trofeo Dorado desbloqueado!")
```

2. Tu reto es **borrar ese código y reescribirlo de forma profesional**.
3. Deberías poder resolver la PARTE 1 usando **una sola línea** (Asignación directa con `and`).
4. Deberías poder resolver la PARTE 2 usando solo **dos líneas** (Aplanando el nido con `and` y quitando redundancias).

### Conceptos permitidos
- Variables y operadores.
- Operadores lógicos (`and`, `or`, `not`).
- Condicionales simples (`if`).

### Conceptos prohibidos
- Totalmente prohibido usar `if` dentro de otro `if` (lógica anidada).
- Prohibido usar `== True`.
- Prohibido hacer un `if-else` solo para asignar `True` o `False` a una variable.

### Resultado esperado en terminal
Al correr tu código limpio y optimizado, la consola debe mostrar exactamente lo mismo que el código del becario:

```text
¡Trofeo Dorado desbloqueado!
```
