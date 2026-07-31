# Reto 79: La Bóveda Inquebrantable 🏦

Imagina que eres el programador jefe de un banco. Tienen sucursales en todo el país, pero TODO el dinero del banco se guarda lógicamente en una única Bóveda Central. 

Si la Sucursal A deposita dinero, la Sucursal B debe ver ese dinero reflejado de inmediato, porque en realidad no hay múltiples bóvedas, **solo hay una bóveda en todo el sistema**.

Tu misión es crear esa Bóveda usando el patrón Singleton.

## 📝 Instrucciones

1. Crea una clase llamada `BovedaCentral`.
2. Crea una variable de clase (fuera de los métodos) llamada `_unica_boveda` y dale el valor de `None`.
3. Crea el método `__new__(cls)` para interceptar el nacimiento:
   - Si `cls._unica_boveda` es `None`, créala usando `super().__new__(cls)`.
   - Recuerda retornar siempre `cls._unica_boveda`.
4. Crea el método `__init__(self)`:
   - Usa `if not hasattr(self, 'dinero_total'):` para verificar si es la primera vez que se configura.
   - Si es la primera vez, crea el atributo `self.dinero_total = 0`.
5. Crea un método normal `depositar(self, cantidad)` que sume esa cantidad a `self.dinero_total`.
6. En tu código principal (fuera de la clase):
   - Crea `sucursal_norte = BovedaCentral()`
   - Crea `sucursal_sur = BovedaCentral()`
   - Haz que la `sucursal_norte` deposite `500`.
   - Haz que la `sucursal_sur` deposite `300`.
   - Finalmente, imprime el dinero total leyendo a través de la `sucursal_sur` así:
     `print("Dinero en la sucursal sur:", sucursal_sur.dinero_total)`

## 🚫 Reglas Estrictas
- **SÍ PUEDES**: Usar `class`, `__new__`, `__init__`, `super()`, `hasattr()`, `if`, asignaciones y sumas.
- **NO PUEDES**: Crear variables globales fuera de la clase para guardar el dinero. Todo el dinero debe vivir DENTRO de la clase `BovedaCentral`.

## 🎯 Resultado Esperado en la Terminal
Al ejecutar tu código, la terminal debe mostrar exactamente esto (puedes agregar los prints que quieras dentro de los métodos para decorar, pero el total debe ser este):

```text
Dinero en la sucursal sur: 800
```

*¡Si lograste que el dinero se sumara (500 + 300) sin importar qué sucursal usaste, felicidades! Acabas de dominar tu primer Patrón de Diseño Arquitectónico.*
