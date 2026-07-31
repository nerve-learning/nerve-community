# Nivel 4: Superpoderes para tus Tests (Fixtures y Parametrize) 🦸‍♂️

## ¿Por qué aprender esto?

Imagina que estás probando si tu licuadora funciona. No quieres ir al mercado a comprar fruta, cortarla, licuarla y luego tener que lavar todo el desastre *para cada prueba diferente*. Quieres que alguien te dé la fruta ya cortada, y que limpie después por ti.

En el mundo del código, crear datos de prueba (como un usuario falso o una lista enorme) una y otra vez es aburrido y ensucia tu código. En `pytest`, los **Fixtures** son ayudantes invisibles que preparan las cosas (datos, configuraciones) antes de tu test para ahorrarte trabajo.

Por otro lado, ¿qué pasa si quieres probar tu código con 10 números diferentes? En vez de escribir 10 tests casi idénticos, usamos **Parametrize** para decirle a pytest: "Ejecuta este mismo test 10 veces, pero usando esta lista de valores". 

## Ruta de Aprendizaje

1. 📖 Lee `teoria.md` — descubre el símbolo `@` (decorador) y el concepto de `import`.
2. 🐍 Estudia `ejemplo.py` — mira cómo nos ahorramos repetir código.
3. 🔥 Completa `reto.md` — crea tus propios ayudantes de prueba.

## Conceptos que usarás aquí

`def`, `assert`, listas `[]`, diccionarios `{}`. Y hoy introducirás dos nuevos superpoderes: `@` (Decoradores) e `import`.
