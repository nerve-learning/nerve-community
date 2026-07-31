# Teoría: La Regla y el Interruptor

### 1. El Flotante (Float)
A los números que tienen decimales los llamamos **Floats** (porque el punto decimal puede "flotar" a diferentes posiciones).
*   **Analogía:** Un Integer (entero) es contar cuántos hermanos tienes. Un Float es usar una cinta métrica para saber tu estatura.
*   **La trampa mortal:** En español solemos usar la coma (1,5) para los decimales. En programación, **SIEMPRE usamos el punto** (`1.5`). Si usas una coma, la computadora se confundirá.

### 2. El Booleano (Boolean)
A veces las cosas son absolutas. ¿Estás despierto o dormido? ¿La luz está prendida o apagada? Para esto usamos los **Booleanos**.
*   **Analogía:** Es un interruptor de luz. Solo tiene dos posiciones: Encendido (`True`) o Apagado (`False`).
*   **¿Cómo se escriben?** Son palabras especiales para la computadora. Se escriben **SIN comillas** y la primera letra **TIENE que ser mayúscula**.

### ¿Qué pasa si me equivoco?

**Error con Floats:** Si escribes `peso = 70,5` (con coma), la computadora pensará que le estás pasando dos cosas diferentes (un 70 y un 5) en lugar de un solo número.

**Errores con Booleanos:**
1.  Si escribes `vivo = true` (con minúscula), la terminal dirá:
    `NameError: name 'true' is not defined`
    (La computadora pensará que 'true' es el nombre de otra caja que olvidaste crear, porque la palabra clave oficial es `True`).
2.  Si escribes `vivo = "True"` (con comillas), ¡ya no es un booleano! Es simplemente un dibujo de la palabra "True", un Texto normal y corriente. Pierde sus poderes mágicos de interruptor.
