# Nivel 5: El Doble de Acción (Mocking) 🎭

## ¿Por qué aprender esto?

Imagina que estás programando un sistema de ventas. Escribes un test automático que llama a la función `cobrar_tarjeta_de_credito()`. Si corres ese test 100 veces, ¡le vas a cobrar a tu tarjeta real 100 veces! 😱

En el código real hay cosas "peligrosas" o impredecibles:
- Conectarse a internet.
- Cobrar dinero de verdad.
- Generar números al azar.

En el cine, cuando una escena es muy peligrosa para el actor principal, contratan a un **doble de acción** (alguien que se parece y hace el trabajo, pero sin poner en riesgo al actor real). En programación, a ese doble de acción le llamamos **Mock** (del inglés "simulación" o "burla").

## Ruta de Aprendizaje

1. 📖 Lee `teoria.md` — descubre qué es un Mock y cómo intercambiar al actor real por el doble.
2. 🐍 Estudia `ejemplo.py` — mira cómo engañamos al código para ganar un juego al azar.
3. 🔥 Completa `reto.md` — salva tu tarjeta de crédito usando un doble de acción.

## Conceptos que usarás aquí

`def`, pasar parámetros, funciones. Hoy aprenderás un concepto avanzado de calidad de código llamado "Inyección de Dependencias" (suena asustadizo, pero es ridículamente fácil de hacer).
