# Teoría: Cazando los "Huecos" (NaN)

En Python normal, cuando algo está vacío o no existe, usamos la palabra `None` (Nada). Cuando le pasas un `None` a Pandas, él lo convierte en **`NaN`**, que significa *Not a Number* (No es un Número).

Los `NaN` son veneno para las matemáticas. Si intentas sumar `10 + NaN`, el resultado es `NaN`.

Pandas nos da dos herramientas súper rápidas para limpiar nuestra tabla:
1. **La barredora drástica (`dropna`)**: Si una fila tiene aunque sea UN solo hueco, la borra completa.
2. **El parche amistoso (`fillna`)**: Rellena todos los huecos con un valor por defecto que tú elijas (por ejemplo, un cero).

## Anatomía de la Limpieza

Supongamos que ya tenemos una tabla llamada `mi_tabla`.

```python
tabla_limpia = mi_tabla.dropna()
```
- **`mi_tabla.`**: A nuestra tabla...
- **`drop`**: "Suelta" o tira a la basura.
- **`na`**: Los valores `NaN`.
- **`()`**: Ejecuta la acción.
- **`tabla_limpia = `**: ¡Súper importante! Guardamos el resultado limpio en una variable nueva.

```python
tabla_parchada = mi_tabla.fillna(0)
```
- **`fill`**: Rellena.
- **`na`**: Los valores `NaN`.
- **`(0)`**: El valor que usaremos para rellenar los huecos. En este caso, ceros.

## ¿Qué pasa si me equivoco?

### El error más común: Olvidar guardar el resultado
**El error:**
```python
mi_tabla.dropna()
print(mi_tabla)
```
La terminal imprimirá tu tabla... **¡y seguirá sucia!** 

**¿Por qué?** Porque métodos como `dropna()` o `fillna()` **no modifican la tabla original**. Solo crean una "copia limpia" y te la devuelven. Si no atrapas esa copia en una variable (con el símbolo `=` de asignación), la copia limpia se pierde en el vacío.

**La solución:** Siempre atrapa el resultado, ya sea creando una variable nueva o sobreescribiendo la anterior: 
`mi_tabla_limpia = mi_tabla.dropna()` o `mi_tabla = mi_tabla.dropna()`.
