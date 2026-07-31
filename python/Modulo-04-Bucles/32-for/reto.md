# Reto 32: El Inspector de Equipaje 🧳

¡Bienvenido a tu nuevo trabajo en la aduana espacial! Los pasajeros están pasando sus maletas por el escáner y tu deber es revisar cada objeto que llevan dentro. Si encuentras un artículo peligroso, debes hacer sonar la alarma.

### Instrucciones paso a paso:
1. Crea una lista llamada `maleta` que contenga los siguientes 5 textos (cadenas): `"ropa"`, `"cepillo"`, `"bomba"`, `"zapatos"`, `"líquido"`.
2. Escribe un texto en pantalla que diga: `"Iniciando escaneo de equipaje..."`.
3. Crea un bucle `for` que recorra cada elemento de la lista `maleta`. Usa la variable temporal `objeto`.
4. **Dentro del bucle `for`** (primer nivel de indentación):
   - Imprime el texto `"Escaneando:"` seguido del valor de `objeto`.
   - Agrega un bloque `if` que compruebe si el `objeto` es exactamente igual (`==`) a `"bomba"`.
   - **Dentro de ese `if`** (segundo nivel de indentación), imprime: `"¡ALERTA ROJA! Objeto peligroso detectado."`.
5. **Fuera del bucle** (sin indentación), imprime: `"Escaneo finalizado."`.

### Reglas estrictas:
- **Conceptos permitidos**: Variables, cadenas de texto (`""`), listas (`[]`), bucle `for`, palabra `in`, condicional `if`, igualdad (`==`), función `print`, dos puntos (`:`), indentación.
- **Prohibido**: No puedes usar `while`, ni comandos que no hemos visto como `break`, `continue` o la palabra reservada `or`. Debes usar solo lo que sabes.

### Resultado esperado en la terminal:
```text
Iniciando escaneo de equipaje...
Escaneando:
ropa
Escaneando:
cepillo
Escaneando:
bomba
¡ALERTA ROJA! Objeto peligroso detectado.
Escaneando:
zapatos
Escaneando:
líquido
Escaneo finalizado.
```
