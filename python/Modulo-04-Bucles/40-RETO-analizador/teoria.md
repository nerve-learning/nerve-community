# Teoría: Pensar como un Programador

Este nivel es tu Proyecto Final del módulo. Cuando nos enfrentamos a un problema grande, no empezamos a escribir código a lo loco. Usamos una técnica llamada **Descomposición**.

## Anatomía de un Analizador

Casi todos los programas que "analizan" datos tienen la misma estructura de tres pasos:

1. **Preparación (Las cajas vacías)**:
   Antes del bucle, preparamos las variables donde guardaremos los resultados. Puede ser un contador (número que empieza en 0), una lista vacía `[]`, o un diccionario con contadores en cero `{"exitos": 0, "errores": 0}`.
   
2. **El Motor (El bucle)**:
   Un `for` o un `while` que va sacando los datos uno por uno.
   Adentro del bucle, usamos los "porteros de discoteca" (`if`, `elif`, `else`) para hacerle preguntas al dato actual: "¿Eres mayor a 10?", "¿Eres una palabra prohibida?".
   
3. **La Reacción (Actualizar las cajas)**:
   Dependiendo de lo que diga el condicional, modificamos nuestras cajas de la fase 1. Sumamos 1 a nuestro diccionario, o agregamos un elemento a nuestra lista nueva. Si encontramos un error catastrófico, usamos `break` para apagar el motor.

## ¿Qué pasa si me equivoco?

El error más común en los proyectos finales es la **Parálisis por Análisis**. Intentas escribir todo el código de una sola vez, le das a "Ejecutar", y la pantalla se llena de letras rojas (errores).

**¿Cómo evitarlo?**
¡Programa paso a paso!
1. Crea tu lista de datos y haz un bucle `for` que solo imprima cada dato. Ejecuta. ¿Funciona? Bien.
2. Agrega un solo `if` adentro. Ejecuta. ¿Funciona? Bien.
3. Agrega tu diccionario contador. Ejecuta.

Si vas un paso a la vez, cuando algo se rompa sabrás exactamente qué línea fue la culpable.
