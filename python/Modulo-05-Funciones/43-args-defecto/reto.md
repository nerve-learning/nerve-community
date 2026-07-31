# Reto 43: La Cafetería Espacial ☕

Has sido contratado en la cafetería de la Estación Espacial. La mayoría de los alienígenas piden café con exactamente 2 cucharadas de azúcar cósmica. Pero algunos prefieren sin azúcar, y otros con muchísima. Además, el tamaño normal siempre es "Mediano", a menos que pidan lo contrario.

Para atender rápido, vas a crear una función que asuma el comportamiento normal, pero que permita cambios si el cliente lo exige.

## 📝 Instrucciones

1. Crea un archivo llamado `reto.py`.
2. Define una función llamada `preparar_cafe`.
3. Tu función debe tener 3 parámetros en este exacto orden:
   - `tipo` (obligatorio, ej: "Expreso", "Capuchino").
   - `azucar` (opcional, por defecto debe ser `2`).
   - `tamano` (opcional, por defecto debe ser `"Mediano"`).
4. Dentro de la función, haz que imprima el siguiente mensaje uniendo los datos:
   `"Preparando un [tipo] de tamaño [tamano] con [azucar] cucharadas de azúcar."`
5. Fuera de la función, vas a simular la atención de 3 clientes llamando a tu función de 3 maneras distintas:
   - **Cliente 1:** Quiere un "Latte" y no dice nada más. (Solo pásale 1 argumento).
   - **Cliente 2:** Quiere un "Expreso" con `0` de azúcar. (Pásale 2 argumentos, no le pases el tamaño para que use el defecto).
   - **Cliente 3:** Quiere un "Moca" con `5` de azúcar, tamaño `"Grande"`. (Pásale los 3 argumentos).

### 🚦 Reglas Estrictas
- **Conceptos permitidos:** `def`, parámetros opcionales (`=`), `print`.
- **Prohibido:** Crear funciones distintas para cada cliente. DEBES usar una sola función `preparar_cafe` aprovechando los argumentos por defecto.

## 🎯 Resultado Esperado en Terminal

Cuando ejecutes tu código, la terminal debería mostrar algo exactamente como esto:

```text
Preparando un Latte de tamaño Mediano con 2 cucharadas de azúcar.
Preparando un Expreso de tamaño Mediano con 0 cucharadas de azúcar.
Preparando un Moca de tamaño Grande con 5 cucharadas de azúcar.
```
