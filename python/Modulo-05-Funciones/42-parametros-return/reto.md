# Reto 42: La Calculadora de Daño ⚔️

Estás programando el sistema de combate de un videojuego RPG. Cada vez que un guerrero ataca, el daño real que recibe el enemigo depende del ataque del guerrero menos la armadura del enemigo.

Necesitas crear una función matemática inteligente que haga este cálculo para no tener que escribir la fórmula matemática en cada pelea.

## 📝 Instrucciones

1. Crea un archivo llamado `reto.py`.
2. Define una función llamada `calcular_dano`.
3. Tu función debe pedir (dentro de sus paréntesis) dos parámetros: `ataque` y `armadura`.
4. Dentro de la función, crea una variable llamada `dano_final` que sea igual al `ataque` menos la `armadura`.
5. Si el `dano_final` es menor a 0, haz que sea igual a 0 (porque los ataques no pueden curar al enemigo, ¿verdad? Usa un `if` que ya aprendiste en el módulo de flujo).
6. Usa la palabra `return` para escupir el `dano_final` hacia el exterior. ¡Cuidado! **No uses `print` dentro de la función para mostrar el resultado**.
7. Fuera de la función, imagina que un Orco ataca a un Elfo. Llama a tu función pasando `50` de ataque y `30` de armadura. Atrapa el resultado en una variable llamada `golpe_orco`.
8. Usa un `print()` (ahora sí, fuera de la función) para mostrar cuánto daño recibió el Elfo usando tu variable `golpe_orco`.
9. Llama de nuevo a la función para un duende que ataca con `10` a un caballero con `50` de armadura. Atrapa el resultado e imprímelo para probar que tu `if` funciona y el daño es 0, no un número negativo.

### 🚦 Reglas Estrictas
- **Conceptos permitidos:** `def`, `return`, parámetros, variables, matemáticas básicas (`-`), `if`, `print` (fuera del `def`).
- **Prohibido:** Usar `print()` DENTRO de la función para mostrar el número. La función DEBE ser puramente de cálculo usando `return`.

## 🎯 Resultado Esperado en Terminal

Cuando ejecutes tu código, la terminal debería mostrar algo como esto:

```text
El Orco ataca! Daño infligido: 20
El Duende ataca! Daño infligido: 0
```
