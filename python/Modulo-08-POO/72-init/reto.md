# Reto 72: Tu Primera Cuenta Bancaria 🏦

Acabas de ser contratado por el Banco Central de Python. Tu tarea es programar el sistema central de las cuentas bancarias usando el poder del método mágico `__init__`.

## 📝 Instrucciones

1. Crea una clase llamada `CuentaBancaria`.
2. Escribe su constructor (`__init__`). Debe recibir a `self` y el nombre del `titular`.
3. Dentro del constructor:
   - Guarda el `titular` dentro del objeto (`self.titular`).
   - Crea un dato interno llamado `self.saldo` y asígnale el valor `0` (cero). Toda cuenta nueva debe empezar sin dinero. **No pidas este valor en los parámetros**.
4. Crea una función dentro de la clase llamada `depositar(self, cantidad)`.
   - Esta función debe sumar la `cantidad` recibida al `self.saldo` actual. (Recuerda que puedes usar `self.saldo = self.saldo + cantidad`).
   - Luego, debe imprimir: `"Depositaste [cantidad]. Saldo actual: [saldo]"` (reemplazando los valores reales).
5. Fuera de tu clase (sin espacios a la izquierda), abre una cuenta bancaria a nombre de `"Batman"` y guárdala en una variable llamada `cuenta_batman`.
6. Haz que Batman deposite `500`.
7. Haz que Batman deposite `1000`.

## ⛔ Reglas estrictas
- **SÍ puedes:** Usar `class`, `def`, `__init__`, `self`, y sumar números (`+`). 
- **NO puedes:** Usar diccionarios, bucles, o pedir el `saldo` en los parámetros del `__init__`. El saldo inicial debe ser fijo de fábrica (cero).

## 🎯 Resultado esperado en la terminal

Cuando ejecutes tu código, deberías ver exactamente esto en tu pantalla:

```text
Depositaste 500. Saldo actual: 500
Depositaste 1000. Saldo actual: 1500
```

¡Es hora de programar! Sé meticuloso con los dobles guiones bajos `__`.
