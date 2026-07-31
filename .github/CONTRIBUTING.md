# Guía de Contribución para `nerve-community`

¡Qué emoción que quieras contribuir a este proyecto! 

El objetivo principal de este repositorio es **aprender** y mantener un currículum de alta calidad para la comunidad. Sigue estos pasos y reglas para asegurarte de que tu contribución sea aceptada rápidamente.

---

## 🚫 Regla de Oro: La estructura es sagrada

La estructura de carpetas dentro de `python/` (`Modulo-01`, `Modulo-02`, etc.) es utilizada por sistemas automatizados.
- **NO cambies el nombre** de ninguna carpeta `Modulo-XX`.
- **NO cambies el nombre** de los archivos internos (`README.md`, `teoria.md`, `ejemplo.py`, `reto.md`, `test_main.py`).
- **NO agregues nuevos archivos** dentro de las carpetas de los niveles, a menos que un mantenedor lo apruebe.

---

## 💡 ¿Qué y cómo puedes contribuir?

Puedes ayudarnos a mejorar el contenido existente o crear nuevos retos socráticos.

### 1. Mejorar el contenido de aprendizaje
Puedes editar `teoria.md`, `ejemplo.py` o `README.md` de cualquier nivel si notas que:
- Una explicación es confusa o tiene faltas de ortografía.
- El código de ejemplo podría ser más claro o tener mejores comentarios.
- El reto está mal redactado.

### 2. Mejorar los tests automáticos
Si detectas que un `test_main.py` de algún reto es demasiado permisivo (deja pasar código malo) o es incorrecto (falla con código bueno), puedes mejorarlo. Asegúrate de probarlo bien antes de enviar el PR.

### 3. Crear nuevos Retos Socráticos
La carpeta `retos/` contiene retos abiertos (sin instrucciones paso a paso) para que los alumnos apliquen lo aprendido. Puedes crear uno nuevo en la carpeta correspondiente a su dificultad (`retos/python/MXX-MYY/nombre-del-reto/reto.md`).

**Plantilla para un nuevo reto socrático (`reto.md`):**

```markdown
# [Nombre del reto]

> **Nivel**: Módulos [X]–[Y] completados
> **Tiempo estimado**: [N] horas
> **Lenguaje**: Python

## Tu misión
[Descripción en 2-3 líneas de qué debe hacer el programa. Sin decir cómo.]

## Lo que debe hacer tu programa
- [Comportamiento observable 1]
- [Comportamiento observable 2]

## Restricciones (respétalas o el reto no cuenta)
- **Solo puedes usar** conceptos de los módulos [X] al [Y]
- **No puedes usar**: [librerías prohibidas]
- **Obligatorio**: [requisito técnico concreto]
- El programa debe correr con `python reto.py`

## Criterio de éxito
Tu solución es válida si:
1. [Verificación concreta 1]
2. [Verificación concreta 2]
```

---

## 🛠️ El proceso de contribución (Fork + PR)

1. **Haz un Fork**: Crea una copia exacta de este proyecto en tu propia cuenta de GitHub dándole al botón "Fork".
2. **Clona**: Descarga tu copia a tu computadora (`git clone https://github.com/TU-USUARIO/nerve-community.git`).
3. **Crea una rama (branch)**: Nunca trabajes en `main`. Crea una rama descriptiva (`git checkout -b mejora-teoria-mod1`).
4. **Haz el cambio**: Modifica los archivos siguiendo las reglas mencionadas arriba.
5. **Commit y Push**: Guarda tus cambios (`git commit -m "feat: mejora explicación de diccionarios en Módulo 04"`) y súbelos a tu fork (`git push origin mejora-teoria-mod1`).
6. **Pull Request (PR)**: Ve a GitHub y abre un Pull Request hacia el repositorio original.
   - En la descripción de tu PR, explica **qué** cambiaste y **por qué**.
   - Marca la casilla correspondiente en nuestra plantilla de PR.

¡Y listo! Los mantenedores revisaremos tu PR y te daremos feedback. ¡Gracias por ayudar a la comunidad!
