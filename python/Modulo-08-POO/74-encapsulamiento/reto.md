# Reto 74: La Caja Fuerte 🔐

¡Has sido contratado para programar la seguridad de un banco! Tienes que crear una Caja Fuerte digital donde el dinero esté completamente protegido (encapsulado) y solo se pueda acceder con la contraseña correcta.

## 📝 Instrucciones

1. Crea una clase llamada `CajaFuerte`.
2. Escribe su constructor (`__init__`). Debe recibir `self` y una variable `contraseña`.
3. Dentro del `__init__`, guarda la contraseña en una variable **privada** llamada `self.__contraseña`.
4. Crea otra variable **privada** llamada `self.__dinero` y asígnale el valor inicial de `1000`. (Nadie de afuera debe poder ver cuánto dinero hay sin permiso).
5. Crea una función pública dentro de la clase llamada `abrir_caja(self, intento)`.
   - Dentro de esta función, haz un `if`/`else`. Si el `intento` es exactamente igual a la `self.__contraseña`, imprime: `"🔓 Caja abierta. Tienes [dinero] dólares."` (imprime el valor de la variable privada).
   - Si no son iguales, imprime: `"🚨 ¡Alarma! Intruso detectado."`.
6. Fuera de tu clase (sin espacios a la izquierda), crea un objeto `CajaFuerte` con la contraseña `"secreto123"`.
7. Haz que un ladrón intente abrirla llamando a la función `abrir_caja` con la contraseña `"0000"`.
8. Haz que el dueño la abra llamando a la función `abrir_caja` con la contraseña `"secreto123"`.

## ⛔ Reglas estrictas
- **SÍ puedes:** Usar los dobles guiones bajos `__` para proteger variables, y bloques `if`/`else`.
- **NO puedes:** Intentar hacer un `print(mi_caja.__dinero)` por fuera de la clase. Recuerda, si lo haces, ¡Python fingirá que no existe!

## 🎯 Resultado esperado en la terminal

Cuando ejecutes tu código, deberías ver exactamente esto:

```text
🚨 ¡Alarma! Intruso detectado.
🔓 Caja abierta. Tienes 1000 dólares.
```

¡Es hora de proteger tus datos como un verdadero arquitecto de software!
