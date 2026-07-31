# Reto 75: El Cine para Adultos 🍿

Trabajas programando el sistema de entradas de un cine para una película de terror clasificación "Para mayores de 18 años". Tu trabajo es asegurar que nadie pueda engañar al sistema usando el poder de las propiedades.

## 📝 Instrucciones

1. Crea una clase llamada `Cine`.
2. En el `__init__`, crea una variable **privada** llamada `self.__edad_cliente` e inicialízala con `0`.
3. Crea un "cadenero lector" usando `@property` seguido de la función `def edad(self):`. Esta función solo debe devolver (`return`) el valor de `self.__edad_cliente`.
4. Crea un "cadenero guardador" usando `@edad.setter` seguido de la función `def edad(self, nueva_edad):`.
5. Dentro de esta función `setter`, haz un `if`/`else`:
   - Si `nueva_edad` es menor a 18, imprime: `"Acceso denegado. Eres menor de edad."` (No guardes nada).
   - Si es 18 o mayor, guarda el valor en la variable privada (`self.__edad_cliente = nueva_edad`) e imprime: `"Acceso concedido. Disfruta la película."`.
6. Fuera de tu clase (sin espacios a la izquierda), crea el objeto: `mi_cine = Cine()`.
7. Un niño de 15 años intenta entrar. Asígnale la edad usando: `mi_cine.edad = 15`. (Nota cómo usamos el `=`, el *setter* hará el resto).
8. Un adulto de 20 años intenta entrar. Asígnale la edad usando: `mi_cine.edad = 20`.

## ⛔ Reglas estrictas
- **SÍ puedes:** Usar `@property`, `@edad.setter`, `__init__`, variables con `__` y bloques lógicos de `if/else`.
- **NO puedes:** Tocar directamente `__edad_cliente` por fuera de la clase.
- **NO puedes:** Ponerle paréntesis a `.edad()` cuando estés fuera de la clase. Debe usarse como si fuera una variable normal con un signo igual `=`.

## 🎯 Resultado esperado en la terminal

Cuando ejecutes tu código, deberías ver esto:

```text
Acceso denegado. Eres menor de edad.
Acceso concedido. Disfruta la película.
```

¡Es hora de ponerte el sombrero mágico de decorador y escribir un código hermoso y seguro!
