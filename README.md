# Nerve Community

Bienvenido a **nerve-community**, el repositorio público del ecosistema de aprendizaje de programación de Alenia Studios. Aquí reside el currículum completo, la teoría, los ejemplos y las pruebas que conforman los cursos.

Para entender el propósito y enfoque pedagógico del proyecto, lee nuestra filosofía: **[Aprender a Programar de Verdad](docs/Porque.md)**.

---

## Dos formas de usar este repositorio

### Como Alumno — no hagas Fork de este repo

Si estás tomando el programa o quieres hacer los cursos, **no debes hacer un Fork de este repositorio**. El flujo de aprendizaje parte de un template oficial que te genera un entorno aislado, automatizado y privado.

- Instrucciones paso a paso: [Cómo usar como Alumno](docs/COMO-USAR-COMO-ALUMNO.md)
- Metodología de evaluación: [Filosofía de los Retos Socráticos](docs/RETOS-SOCRATICOS.md)

En tu repositorio privado (generado desde el template):

- Al inicio solo tendrás disponible el Módulo 01.
- Cada módulo tiene teoría (`teoria.md`), código de referencia (`ejemplo.py`) y un desafío (`reto.md`).
- Para cada reto, leerás el código, interpretarás los errores y resolverás el problema con el apoyo de los tests automáticos.
- Al pasar la validación de CI con un check verde, se desbloquea el siguiente módulo.

### Como Contribuidor — Open Source

Si quieres mejorar la calidad del material del curso:

- Haz **Fork** de este repositorio (`nerve-community`).
- Mejora el contenido (documentación, ejemplos, retos) y envía un **Pull Request**.
- Toda la comunidad se beneficia de tus mejoras.

Guías para contribuir:

- [Guía de Contribución](.github/CONTRIBUTING.md)
- [Cómo hacer tu primer PR](COMO-HACER-TU-PRIMER-PR.md)

---

## Estructura del repositorio

```text
python/               ← Currículum completo del curso de Python (Módulos 01 a 12 + intermedios)
retos/                ← Retos socráticos clasificados por lenguaje y nivel de dificultad
docs/                 ← Documentación del proyecto, filosofía y guías de uso
.github/              ← Workflows de GitHub Actions, plantillas de Issues/PRs y guía de contribución
glosario/             ← Diccionario técnico de términos clave, organizado por tema y lenguaje
```

> **Regla de Oro:** La estructura de carpetas dentro de los lenguajes (ej. `python/Modulo-XX`) no debe alterarse en nomenclatura. Estos archivos alimentan los templates de los alumnos y la evaluación automática.

---

## Qué puedes mejorar

- Aclarar explicaciones en los archivos `teoria.md`.
- Añadir comentarios o casos alternativos en los `ejemplo.py`.
- Corregir bugs o robustecer pruebas en los `test_main.py`.
- Proponer nuevos Retos Socráticos dentro de `retos/`.

---

## Comunidad y Contacto

- **Discord**: [Únete a nuestra comunidad](https://discord.gg/xFptGAr7t) para resolver dudas, compartir proyectos y hablar con otros estudiantes y desarrolladores.
- **Licencia**: GNU GPL v3.
