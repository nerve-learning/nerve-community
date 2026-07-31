# Nivel 79: Singleton (El Único) 👑

En la programación, a veces necesitamos crear reglas estrictas no solo sobre *cómo* es un objeto, sino sobre *cuántos* objetos pueden existir.

Imagina un país con dos Presidentes dando órdenes distintas al mismo tiempo. ¡Sería un caos total! 
En el mundo del software, hay cosas que **deben ser únicas**: 
- La conexión a la base de datos principal.
- La configuración general de tu videojuego.
- El sistema que reproduce el audio.

Si tuviéramos múltiples copias de estas cosas, la memoria de la computadora colapsaría o tendríamos datos contradictorios.

Para solucionar esto, los arquitectos de software inventaron un truco maestro llamado **Singleton** (que se traduce como "Solitario" o "Único"). Es un *Patrón de Diseño* (una receta probada) que garantiza que una clase solo pueda dar a luz a **un único objeto** en toda su vida.

## 🗺️ Ruta de Aprendizaje
1. **`teoria.md`**: Conoceremos a la cigüeña de Python (`__new__`) y cómo engañarla.
2. **`ejemplo.py`**: Coronaremos al único Rey y veremos qué pasa si intentamos crear un impostor.
3. **`reto.md`**: Construirás la Bóveda Central de un banco donde todas las sucursales comparten el mismo dinero.
