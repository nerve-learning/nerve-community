# Reto 73: El Taller de Vehículos 🚗🚲

¡Trabajas en un taller mecánico! Tienes distintos tipos de vehículos, pero todos comparten algo: tienen una marca y pueden arrancar. Vamos a usar Herencia y Polimorfismo para modelar esto sin repetir código.

## 📝 Instrucciones

1. Crea una clase padre llamada `Vehiculo`.
2. Dale a `Vehiculo` un constructor (`__init__`) que reciba `self` y la `marca`. Guárdala en `self.marca`.
3. Dale a `Vehiculo` una función `arrancar(self)` que imprima: `"El vehículo [marca] está encendido."`.
4. Crea una clase hija llamada `Coche` que herede de `Vehiculo`.
5. Dentro de `Coche`, sobrescribe (aplasta) la función `arrancar(self)` para que imprima: `"¡Brum brum! El coche [marca] ha arrancado."`. (No escribas el `__init__` aquí, ¡deja que lo herede!).
6. Crea otra clase hija llamada `Bicicleta` que herede de `Vehiculo`.
7. Dentro de `Bicicleta`, sobrescribe la función `arrancar(self)` para que imprima: `"¡Ring ring! La bicicleta [marca] está en marcha."`.
8. Fuera de las clases, crea un objeto `Coche` de la marca `"Toyota"`.
9. Crea un objeto `Bicicleta` de la marca `"Trek"`.
10. Llama a la función `arrancar()` de tu coche y luego a la de tu bicicleta.

## ⛔ Reglas estrictas
- **SÍ puedes:** Usar `class`, heredar usando `(Vehiculo)`, y sobrescribir métodos.
- **NO puedes:** Escribir `__init__` dentro de `Coche` o `Bicicleta`. Tienes que confiar ciegamente en que heredarán el del padre.

## 🎯 Resultado esperado en la terminal

Cuando ejecutes tu código, deberías ver exactamente esto:

```text
¡Brum brum! El coche Toyota ha arrancado.
¡Ring ring! La bicicleta Trek está en marcha.
```

¡Demuestra que puedes organizar el código de tu taller sin repetirte!
