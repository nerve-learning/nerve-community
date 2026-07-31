# Teoría: Puertas secretas dentro de cuartos secretos

Hasta ahora sabemos abrir una puerta usando `if`. Si la condición es `True`, entramos a la habitación (identificada por los 4 espacios de sangría).
Pero, ¿qué pasa si queremos hacer una nueva pregunta **solo a las personas que lograron entrar a esa primera habitación**?

Usamos la **lógica anidada**, que simplemente es poner un bloque `if`/`else` completo *adentro* de la sangría de otro.

### El arte de la doble sangría (8 espacios)
Si el primer `if` requiere 4 espacios de sangría, cualquier cosa que sea la consecuencia de ese `if` debe ir a 4 espacios. 
Si dentro de esos 4 espacios decides poner un *nuevo* `if`, la consecuencia de ese **segundo** `if` tendrá que empujarse otros 4 espacios (llegando a 8 espacios en total).

* **Analogía**: Es como un índice de un libro.
```text
1. Capítulo principal (Sin sangría)
    1.1. Subtema (1 tabulador / 4 espacios)
        1.1.1. Detalle específico (2 tabuladores / 8 espacios)
```

---

## Anatomía (Sintaxis)

```python
if primera_condicion:
    print("Pasaste el primer filtro")
    
    if segunda_condicion:
        print("Pasaste el segundo filtro, ¡Estás en la zona más exclusiva!")
    else:
        print("Pasaste el primer filtro, pero te quedaste en el segundo")

else:
    print("Ni siquiera pasaste el primer filtro")
```

* Fíjate bien en cómo el `else` de adentro se alinea con el `if` de adentro (a 4 espacios).
* El `else` de afuera se alinea con el `if` de afuera (sin espacios).
* Todo lo que está a 8 espacios pertenece **únicamente** al `if` interno.

---

## ¿Qué pasa si me equivoco?

**1. El caos de las sangrías perdidas**
El error más destructivo aquí es alinear mal un `else`. Si pones el `else` del segundo filtro pegado a la pared izquierda, Python creerá que ese `else` le pertenece al primer filtro. La lógica de tu programa hará cosas loquísimas.
* **Solución**: Tu código es visual. Dibuja una línea imaginaria hacia abajo desde la 'i' de tu `if`. Su `else` correspondiente debe caer exactamente sobre esa misma línea.

**2. La Pirámide de la Perdición (Anti-patrón)**
Aunque puedes meter un `if` dentro de otro, y otro dentro de ese, y otro más... **¡no lo hagas a menos que sea estrictamente necesario!**. Si metes 5 niveles de profundidad, tu código será ilegible. A veces es mejor usar un simple `and` (ej. `if filtro_1 and filtro_2:`). Usa la lógica anidada solo cuando el plan B del filtro 2 sea muy distinto al plan B del filtro 1.
