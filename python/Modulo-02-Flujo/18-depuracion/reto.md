# Reto 18: El Cajero Automático Roto 🏧💥

El cajero automático de la esquina está volviéndose loco. Un cliente tiene 500 dólares en su cuenta y quiere retirar 100. El cajero debería decirle "Retiro exitoso", pero en lugar de eso le dice "Fondos insuficientes". 

Hay un error (un *bug*) en la lógica, pero a simple vista no es obvio.

## Instrucciones

1. Crea el siguiente código en tu editor exactamente como está escrito aquí (tiene un bug a propósito):

```python
saldo = 500
retiro = 100

# Se nos cobra una comisión fantasma y se resta un cargo extra
comision = retiro + 50
saldo_disponible = saldo - retiro - comision

if retiro <= saldo_disponible:
    print("Retiro exitoso.")
else:
    print("Fondos insuficientes.")
```

2. Tu misión no es solo adivinar el error, sino usar **prints de depuración** para encontrarlo científicamente.
3. Agrega `print()` antes del `if` para ver el valor exacto de `saldo_disponible` y el valor de `comision`. Agrégales el prefijo `"DEBUG - "` para saber que son tuyos.
4. Una vez que corras el código y veas en la terminal los valores reales, analiza por qué falló.
5. Finalmente, corrige las fórmulas matemáticas para que el código funcione correctamente y apruebe el retiro (el retiro total con comisión debe ser 150, dejando el saldo disponible correcto para evaluar).

### Conceptos permitidos
- Variables y operadores matemáticos.
- `print()` para diagnóstico y para mensajes finales.
- Condicionales `if-else`.

### Conceptos prohibidos
- Funciones, ciclos, librerías u otros conceptos no vistos.
- El debugger de Python integrado en el IDE (queremos aprender la técnica manual básica primero).

### Resultado esperado en terminal ANTES de arreglarlo
```text
DEBUG - Comisión calculada: 150
DEBUG - Saldo disponible para evaluar: 250
Fondos insuficientes.
```
*(Nota: Al ver que el saldo evaluado era 250 y el retiro 100, el retiro de hecho SÍ es menor o igual al saldo disponible. El bug está en la condición matemática de cómo se compara o calcula el límite real)*

### Resultado esperado en terminal DESPUÉS de arreglarlo (y tras borrar los DEBUG)
```text
Retiro exitoso.
```
*(Tip: La lógica correcta es comparar si el total a sacar `(retiro + comision)` es menor o igual al `saldo` original).*
