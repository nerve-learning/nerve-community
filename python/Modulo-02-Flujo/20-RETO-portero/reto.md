# Reto 20: El Implacable Portero de la Discoteca 🦍🚪

El club más exclusivo de la ciudad necesita un sistema informático para decidir quién entra y quién se va a casa. Han despedido al antiguo programador porque la gente se estaba colando. ¡Tú eres su única esperanza!

## Las Reglas del Club
Vas a crear un script que evalúe a un cliente basándose en estas reglas estrictas, **en este orden exacto**:

1. **Edad:** Si el cliente tiene menos de 18 años, es rechazado inmediatamente (Mensaje: `"Rechazado: Eres menor de edad."`).
2. **Día de la semana:** El club abre de "jueves" a "domingo". Si es "lunes", "martes" o "miércoles", nadie entra (Mensaje: `"Rechazado: El club está cerrado hoy."`).
3. **VIP:** Si el cliente está en la lista VIP, entra gratis, sin importar cómo venga vestido. (Mensaje: `"¡Bienvenido, VIP! Pase usted."`).
4. **Código de vestimenta:** Si no es VIP, su ropa debe ser "elegante" o "casual". Si viene de "deportiva" o "traje_de_baño", se va. (Mensaje: `"Rechazado: No cumples el código de vestimenta."`).
5. **Entrada normal:** Si es mayor de edad, el club está abierto, no es VIP, pero viene "elegante" o "casual", paga su entrada y entra. (Mensaje: `"Bienvenido. Son 20 dólares de cover."`).

## Instrucciones

1. Crea las variables iniciales para hacer la prueba:
   * `edad_cliente = 19`
   * `dia_actual = "viernes"`
   * `es_vip = False`
   * `ropa = "deportiva"`

2. Construye la lógica usando TODO lo que sabes (`if`, `elif`, `else`, `match-case`, `and`, `or`, etc.). ¡Usa la herramienta que mejor se adapte a cada regla!
   * *Tip:* Un `match` puede ser excelente para evaluar el día de la semana.
   * *Tip:* La regla de la edad debería ser lo primerito que evaluemos (usando `if` y lógica anidada).

### Conceptos permitidos
- ¡Todos los conceptos del Módulo 02!
- Lógica anidada.
- Optimización.

### Conceptos prohibidos
- Funciones (`def`), ciclos (`for`, `while`), listas, diccionarios.

### Resultado esperado en terminal (con los datos de prueba del paso 1)
Como tiene 19, es viernes, NO es VIP, y viene con ropa "deportiva", el resultado debe ser:
```text
Rechazado: No cumples el código de vestimenta.
```

*Juega cambiando las variables. Ponle 17 años y ve qué pasa. Ponle ropa "casual" y ve qué pasa. ¡Demuestra que eres el maestro del Flujo!*
