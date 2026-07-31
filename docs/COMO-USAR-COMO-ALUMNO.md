# Cómo usar este ecosistema como Alumno

Bienvenido al ecosistema de Alenia Studios / Nerve Community. Este espacio está diseñado como un entorno de aprendizaje práctico, no como un lugar para leer: está hecho para que hagas, rompas y descubras.

> **IMPORTANTE: No hagas Fork de este repositorio público.**
> Para garantizar un entorno de evaluación automática correcto, debes generar tu propio repositorio a partir de nuestra plantilla oficial.

---

## 1. Cómo empezar: el template

Tu punto de partida es el repositorio template `nerve--template`, no este repo. El template te genera un repositorio privado con:

- La estructura de módulos ya configurada.
- Los workflows de CI listos para evaluar tu código automáticamente.
- El Módulo 01 desbloqueado desde el inicio.

Para obtener acceso al template, entra al servidor de Discord y pide el enlace en el canal correspondiente. Un administrador te lo compartirá.

---

## 2. El ciclo de aprendizaje

El flujo está inspirado en cómo trabajan los ingenieros de software en la vida real:

1. **Genera tu repo desde el template** — crea tu repositorio privado (o público, según prefieras) desde `nerve--template`.
2. **Clona tu repositorio** — descarga los archivos a tu computadora con `git clone`.
3. **Elige el módulo activo** — navega a la carpeta correspondiente, por ejemplo `python/Modulo-01-Fundamentos`.
4. **Estudia la teoría** — lee `README.md` para entender el objetivo del módulo, luego `teoria.md` para los conceptos técnicos, y analiza `ejemplo.py` para ver cómo se aplican.
5. **Enfrenta el reto** — abre `reto.md`. Aquí encontrarás un problema práctico sin la respuesta. Tu tarea es resolverlo.
6. **Valida con los tests** — ejecuta `pytest test_main.py` en tu terminal local. Si un test falla, lee el error: el error es tu guía, no un obstáculo.
7. **Sube tu avance** — cuando todos los tests pasen, haz commit y push a tu repositorio. El CI de GitHub Actions correrá los mismos tests automáticamente.
8. **Desbloqueo automático** — al pasar la validación de CI, el siguiente módulo queda disponible en tu rama.

---

## 3. Cómo funciona el CI automático

Cuando haces push a tu repositorio, GitHub Actions ejecuta automáticamente:

- Los tests del módulo (`pytest`) para verificar que tu código es correcto.
- El linter de estilo (`black`) para verificar que el formato es consistente.

Si todo pasa, verás un check verde en tu commit. Si algo falla, el check será rojo y los logs del workflow te mostrarán exactamente qué falló y en qué línea.

El CI no te penaliza por intentar. Puedes hacer push cuantas veces necesites.

---

## 4. El glosario de Python

En `glosario/python/` encontrarás explicaciones en español de los términos técnicos que aparecen en cada módulo. El glosario está dividido por módulo para que puedas consultarlo de forma específica, no como lectura lineal.

Índice completo: [glosario/python/README.md](../glosario/python/README.md)

---

## 5. Si te atascas

Es completamente normal atascarse. La frustración es parte de reprogramar la forma en que tu cerebro resuelve problemas. Antes de pedir ayuda directamente:

- Lee el error completo. Python te dice exactamente en qué línea falló y por qué.
- Rompe el código a propósito: cambia una variable, quita un `return`, corre los tests. Observa qué pasa.
- Busca en la documentación oficial de Python o en los archivos del glosario.

Cuando lo anterior no sea suficiente:

- Pregunta en el canal de **Discord** de la comunidad. Describe qué intentaste, qué error obtienes y qué parte no entiendes. No compartas la solución completa.
- Lee [RETOS-SOCRATICOS.md](RETOS-SOCRATICOS.md) para entender la filosofía detrás de la evaluación.

---

← [Volver al repositorio](../README.md)
