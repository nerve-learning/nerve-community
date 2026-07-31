# Reto 17: Conmutador Telefónico del Banco 📞🏦

Has sido contratado para modernizar el sistema telefónico de un banco. Cuando el cliente llama, la operadora automática le pide que ingrese un número del 1 al 4. Ya no usarán más el viejo y kilométrico sistema de `if-elif`, ahora usarán un elegante `match-case`.

## Instrucciones

1. Crea una variable llamada `opcion_teclado` y asígnale un número entero del `1` al `4` (o invéntate uno que no exista, como `9`).

2. Crea la estructura `match` para evaluar la variable `opcion_teclado`.

3. Crea los siguientes `case` con su debida sangría (4 espacios para el `case`, 8 espacios para el `print` interior):
   * `case 1:` Imprimir `"Lo estamos comunicando con el departamento de Ventas."`
   * `case 2:` Imprimir `"Lo estamos comunicando con Soporte Técnico."`
   * `case 3:` Imprimir `"Lo estamos comunicando con Cobranza."`
   * `case 4:` Imprimir `"Gracias por llamar. Colgando la llamada..."`

4. Crea el caso por defecto (el comodín `_`) por si el usuario presiona otro número diferente:
   * `case _:` Imprimir `"Opción inválida. Por favor, marque un número del 1 al 4."`

### Conceptos permitidos
- Variables (asignación con `=`).
- Tipos de datos (`int`).
- La estructura `match` y `case`.
- El caso por defecto `case _:`.
- `print()`.

### Conceptos prohibidos
- Totalmente prohibido usar `if`, `elif`, o `else`. El reto es dominar la nueva estructura.
- Funciones `def`.
- Lógica anidada.

### Resultado esperado en terminal
Si configuras `opcion_teclado = 2`, tu terminal debe verse así:

```text
Lo estamos comunicando con Soporte Técnico.
```

Si configuras `opcion_teclado = 9`, la terminal debe verse así:

```text
Opción inválida. Por favor, marque un número del 1 al 4.
```
