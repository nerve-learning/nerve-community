# Reto Nivel 97: El Cerebro Matemático 🧠

Has visto cómo delegar la cocina de un restaurante. Ahora vamos a delegar el trabajo cerebral pesado. Tu computadora personal a veces se satura haciendo muchos cálculos, así que vamos a crear un microservicio que *solo* sirva para hacer matemáticas.

## Instrucciones

1. Crea un script llamado `reto.py`.
2. Conéctalo a la red de Nerve con el nombre `"cerebro_matematico"`.
3. Registra una función de escucha.
4. Si el mensaje que recibe tiene `"accion": "sumar"`, debe extraer los valores `"a"` y `"b"` del diccionario de datos.
5. Realiza la suma de `a + b`.
6. Usa `.send()` para devolver el resultado al `remitente` (quien sea que le haya preguntado). El mensaje de vuelta debe tener `"accion": "resultado"` y `"total": la_suma`.
7. Mantén el programa vivo con un `while True: time.sleep(1)`.

## Reglas Estrictas

- **Permitido:** Diccionarios, `if`, `get()`, `.connect()`, `.listen()`, `.send()`, sumar con `+`.
- **Prohibido:** Usar clases, funciones complicadas de matemáticas, o usar `.broadcast()` (el cerebro matemático es privado, solo le responde a quien le preguntó).

## El Escenario de Prueba

Abre una terminal con tu código de `reto.py` corriendo.
Abre otra terminal o un script rápido llamado `estudiante.py`, que se conecte como "estudiante", y ejecute:
`cliente.send("cerebro_matematico", {"accion": "sumar", "a": 10, "b": 15})`

En la terminal de la calculadora, deberías imprimir que recibiste la petición.
En la terminal del estudiante (si pusiste un `.listen()`), deberías recibir:

```text
--- MODO CALCULADORA ---
[*] Cerebro encendido.
[!] Petición de 'estudiante' recibida: sumar 10 y 15.
[✓] Resultado calculado y enviado.
```
