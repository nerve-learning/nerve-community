# Nivel 74: Encapsulamiento 🛡️

Hasta ahora, nuestras clases han tenido sus puertas de par en par. Cualquiera podía acceder a los datos de un objeto y modificarlos libremente desde afuera. 

Imagina que programas el sistema de un banco y escribes: `mi_cuenta = CuentaBancaria()`. 
Si alguien desde afuera de la clase escribe `mi_cuenta.saldo = 1000000`, ¡acaba de hacerse millonario sin hacer un depósito real! O peor aún, podría poner `mi_cuenta.saldo = -500` y romper el sistema.

El **Encapsulamiento** es la técnica de ponerle un candado a los datos sensibles de tu objeto. Ocultamos las variables internas para que nadie pueda tocarlas directamente. Si alguien quiere interactuar con esos datos, tendrá que pedirlo por favor usando las funciones (métodos) que nosotros permitamos.

## Ruta de aprendizaje
1. **Teoría (`teoria.md`)**: Usaremos la analogía de la máquina expendedora para entender lo público vs lo privado, y desarmaremos el símbolo del doble guion bajo (`__`).
2. **Ejemplo (`ejemplo.py`)**: Programaremos un Diario Íntimo a prueba de chismosos.
3. **Reto (`reto.md`)**: Tu misión será programar una Caja Fuerte inviolable. ¡A programar!
