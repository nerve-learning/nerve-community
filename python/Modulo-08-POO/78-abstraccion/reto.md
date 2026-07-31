# Reto 78: El Cajero Multimillonario 💳

Eres el ingeniero principal de una nueva tienda en línea. Tu jefe quiere que el sistema pueda aceptar diferentes formas de pago, pero es muy estricto: TODOS los métodos de pago deben tener obligatoriamente un botón interno (método) llamado `procesar_pago`.

Para garantizar que ningún programador novato arruine el sistema en el futuro creando un método de pago sin esa función, vas a usar Abstracción.

## 📝 Instrucciones

1. **Importa las herramientas necesarias** (`ABC` y `abstractmethod` del módulo `abc`).
2. Crea una clase abstracta llamada `MetodoPago` que herede de `ABC`.
3. Dentro de `MetodoPago`, define un método abstracto llamado `procesar_pago` que reciba `self` y `cantidad`. Recuerda usar `pass` por dentro.
4. Crea una clase `TarjetaCredito` que herede de `MetodoPago`. 
   - Debe implementar `procesar_pago(self, cantidad)`.
   - Cuando se llame, debe imprimir: `"💳 Cobrando $X de la tarjeta de crédito."` (donde X es la cantidad).
5. Crea una clase `Paypal` que herede de `MetodoPago`.
   - Debe implementar `procesar_pago(self, cantidad)`.
   - Cuando se llame, debe imprimir: `"📧 Transfiriendo $X desde la cuenta de Paypal."`.
6. Al final, crea un objeto de `TarjetaCredito`, otro de `Paypal`, y haz que procesen un pago de `150` y `50` respectivamente.

## 🚫 Reglas Estrictas
- **SÍ PUEDES**: Usar `class`, herencia `(Padre)`, `from abc import ABC, abstractmethod`, `@abstractmethod`, `print()`, y `pass`.
- **NO PUEDES**: Usar `__init__` (no lo necesitamos aquí), ni intentar crear un objeto directo de `MetodoPago`.

## 🎯 Resultado Esperado en la Terminal
Al ejecutar tu código, la terminal debe mostrar exactamente esto:

```text
💳 Cobrando $150 de la tarjeta de crédito.
📧 Transfiriendo $50 desde la cuenta de Paypal.
```

*Nota: Si te sientes valiente, intenta comentar el método `procesar_pago` dentro de la clase `Paypal` y ejecuta el código. ¡Verás cómo el fantasma de la abstracción te regaña!*
