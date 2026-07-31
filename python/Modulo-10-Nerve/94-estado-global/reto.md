# Reto 94: El Banco Descentralizado 🏦

Eres el nuevo gerente del Banco Descentralizado de tu computadora. Tu trabajo es mantener un servidor encendido que administre la bóveda de dinero. Cada vez que otro programa en tu red solicite un retiro, debes descontarlo del saldo total.

## Instrucciones Paso a Paso

1. Crea un archivo llamado `banco.py`.
2. Importa la clase `NexusClient` de `nerve`.
3. Crea tu **Estado Global** fuera de cualquier función: una variable llamada `saldo_boveda` que empiece con el número `1000`.
4. Define a tu recepcionista (una función llamada `cajero` que reciba `datos`).
5. DENTRO de la función `cajero`, pide permiso para modificar el saldo usando la palabra mágica `global`.
6. Extrae la cantidad a retirar del diccionario usando: `retiro = datos.get("retiro", 0)`.
7. Si el `retiro` es mayor que cero, réstalo del `saldo_boveda`. (Pista: `saldo_boveda = saldo_boveda - retiro`).
8. Imprime en pantalla: `"💸 Retiro procesado de: [retiro]. Saldo actual: [saldo_boveda]"`. Sustituyendo los valores reales.
9. FUERA de la función, crea tu antena, conéctala con el nombre `"banco_central"` y pon a escuchar a tu `cajero` usando `.listen()`.
10. Crea un `input("Banco abierto. Presiona ENTER para cerrar...\n")` para mantener el programa vivo.

## 📜 Reglas de la Misión

**🟢 Conceptos Permitidos:**
- `NexusClient`, `.connect()`, `.listen()`
- Variables globales y la palabra `global`.
- Matemáticas básicas (`-`).
- `input()` y `print()`.
- Diccionarios `{}` y el método `.get()`.

**🔴 Prohibido:**
- Intentar restar dinero sin usar `global`.
- Olvidar el parámetro en tu función `cajero`.
- Ponerle paréntesis a tu función dentro del `.listen()`.

## 🏆 Resultado Esperado en la Terminal

Al ejecutar `banco.py`, la terminal se quedará esperando:

```text
Banco abierto. Presiona ENTER para cerrar...
```

*Si usaras otro script para enviarle el mensaje `{"retiro": 200}` al nodo `"banco_central"`, verías aparecer mágicamente:*

```text
💸 Retiro procesado de: 200. Saldo actual: 800
```
