# Reto 02: Microondas Asíncrono

Vas a simular calentar comida en un microondas.

### 📝 Instrucciones
1. Importa `asyncio`.
2. Crea una función asíncrona llamada `calentar_comida()`.
3. Imprime "Metiendo la comida al microondas...".
4. Usa `await asyncio.sleep(2)` para simular que tarda 2 segundos.
5. Imprime "¡Comida lista! (Beep beep)".
6. Crea otra función asíncrona llamada `main()` (la principal).
7. Dentro de `main()`, imprime "Tengo hambre".
8. Llama a `calentar_comida()` usando `await`.
9. Imprime "A comer".
10. Usa `asyncio.run()` para ejecutar `main()`.

### 🚫 Reglas
- **Permitido:** `import asyncio`, `async def`, `await`, `asyncio.sleep()`, `asyncio.run()`, `print()`.
- **Prohibido:** Usar `time.sleep()`.
- **Prohibido:** Olvidar el `await` antes de `asyncio.sleep()`.

### 🎯 Resultado Esperado en Terminal
*(Habrá una pausa de 2 segundos antes de que diga que la comida está lista)*
```text
Tengo hambre
Metiendo la comida al microondas...
¡Comida lista! (Beep beep)
A comer
```
