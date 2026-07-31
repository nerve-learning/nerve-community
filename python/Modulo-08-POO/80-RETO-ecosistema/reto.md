# Reto 80: La Agencia Espacial 🚀

Tu misión final para graduarte del Módulo de Programación Orientada a Objetos es simular el lanzamiento de una flota espacial. Tienes que usar **TODAS** las herramientas que conoces en un solo archivo.

## 📝 Instrucciones Paso a Paso

1. **Singleton (Centro de Control):**
   - Crea la clase `CentroControl` usando el patrón Singleton (`__new__`).
   - El centro de control debe tener un método `iniciar_lanzamiento()` que simplemente imprima: `"🎙️ Centro de Control: Iniciando secuencia de despegue..."`.

2. **Abstracción y Métodos de Clase (Molde de Nave):**
   - Importa `ABC` y `abstractmethod`.
   - Crea la clase abstracta `Nave(ABC)`.
   - Crea una variable de clase llamada `_naves_creadas = 0`.
   - Crea un `@classmethod` llamado `total_naves(cls)` que devuelva ese número.

3. **Encapsulamiento e Inicialización:**
   - En `__init__` de `Nave`, recibe `nombre` y `combustible`.
   - Guarda el combustible como privado (`__combustible`).
   - Aumenta `_naves_creadas` en 1.
   - Crea un `@property` llamado `combustible` que devuelva el nivel de combustible.

4. **El Contrato y la Voz:**
   - Crea un método abstracto llamado `despegar(self)` dentro de `Nave`.
   - Crea el método mágico `__str__(self)` que retorne el texto: `"🛸 Nave [Nombre] - Combustible: [Combustible]%"`.

5. **Herencia (Los Cohetes reales):**
   - Crea la clase `Explorador` que herede de `Nave`. Su método `despegar` debe imprimir: `"🛰️ [Nombre] encendiendo motores ligeros. ¡Hacia las estrellas!"`.
   - Crea la clase `Carguero` que herede de `Nave`. Su método `despegar` debe imprimir: `"🚀 [Nombre] encendiendo propulsores pesados. ¡Levantando carga!"`.

6. **Ejecución Final:**
   - Crea el `CentroControl` y llama a `iniciar_lanzamiento()`.
   - Crea un `Explorador` llamado "Voyager" con 100 de combustible.
   - Crea un `Carguero` llamado "Titan" con 80 de combustible.
   - Imprime cuántas naves se crearon llamando al método de clase.
   - Imprime cada nave (para probar `__str__`).
   - Haz que ambas naves despeguen.

## 🚫 Reglas Estrictas
- ¡Usa todo lo aprendido! `__new__`, `__init__`, `ABC`, `__`, `@property`, `@classmethod`, `__str__`, etc.

## 🎯 Resultado Esperado en la Terminal

```text
🎙️ Centro de Control: Iniciando secuencia de despegue...
Total de naves listas: 2
🛸 Nave Voyager - Combustible: 100%
🛸 Nave Titan - Combustible: 80%
🛰️ Voyager encendiendo motores ligeros. ¡Hacia las estrellas!
🚀 Titan encendiendo propulsores pesados. ¡Levantando carga!
```

*Nota: Si lograste que esto corra sin errores, ponte de pie, aplaude y tómate un café. Eres oficialmente un Programador Orientado a Objetos.*
