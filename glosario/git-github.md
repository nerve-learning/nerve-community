# Glosario: Git y GitHub

Todo lo que necesitas saber sobre control de versiones y la plataforma GitHub para contribuir en cualquier proyecto Open Source, incluyendo Nerve Community.

---

## Conceptos Fundamentales

| Término | Qué es | Para qué sirve | Ejemplo | Error común |
| :--- | :--- | :--- | :--- | :--- |
| **Git** | Programa de control de versiones | Guarda el historial completo de todos los cambios que hiciste, quién los hizo y cuándo. Como una máquina del tiempo para tu código. | `git --version` | — |
| **GitHub** | Plataforma web para alojar código | Donde subes tu código con Git y colaboras con otros. Nerve Community vive aquí. | `https://github.com/Kaia-Alenia/nerve-community` | — |
| **Repositorio (Repo)** | Carpeta de proyecto con historial | Contiene todos los archivos del proyecto más el historial completo de cambios. Es lo que clonas para trabajar. | `https://github.com/Kaia-Alenia/nerve-community` | — |
| **Open Source** | Código abierto y público | Software cuyo código fuente es visible para todos y puede ser modificado y distribuido libremente. | Licencia GNU GPL v3 que usa este repo | — |

---

## Flujo de Trabajo Básico

| Término | Qué es | Para qué sirve | Ejemplo | Error común |
| :--- | :--- | :--- | :--- | :--- |
| **Fork** | Copia personal de un repositorio ajeno | Crea una copia exacta en tu cuenta de GitHub para poder modificarla sin tocar el original. | Botón "Fork" en GitHub | — |
| **git clone** | Descarga del repo a tu computadora | Trae los archivos de GitHub a tu máquina local. Siempre clonas tu fork. | `git clone https://github.com/TU-USUARIO/nerve-community.git` | — |
| **Branch (Rama)** | Línea de trabajo independiente | Crea una dimensión paralela de tu código para no tocar ni romper la rama `main`. | `git checkout -b solucion-python-M01` | — |
| **Checkout** | Cambiar de rama | Te mueve entre ramas. Con `-b` crea una nueva. | `git checkout main` | — |
| **git add** | Preparar archivos para el commit | Marca qué archivos quieres incluir en el próximo punto de guardado. | `git add .` | — |
| **Commit** | Punto de guardado permanente | Guarda los cambios preparados con un mensaje descriptivo. | `git commit -m "feat: agregar solución al módulo 01"` | — |
| **Push** | Subir commits a GitHub | Envía los commits de tu computadora hacia tu repositorio en GitHub. | `git push origin solucion-python-M01` | — |
| **Pull** | Bajar actualizaciones desde GitHub | Descarga los cambios más recientes de GitHub hacia tu máquina local. | `git pull origin main` | — |
| **Pull Request (PR)** | Solicitud de integración de cambios | Le dices al dueño del repo: "hice estos cambios en mi fork, ¿los quieres en el proyecto oficial?" | Clic en "Compare & pull request" en GitHub | — |
| **Merge** | Fusionar código | Aceptar un Pull Request y unir el código nuevo con el proyecto principal. Lo hacen los maintainers. | "PR merged" | — |

---

## Sincronización y Resolución de Problemas

| Término | Qué es | Para qué sirve | Ejemplo | Error común |
| :--- | :--- | :--- | :--- | :--- |
| **origin** | Nombre del repo remoto por defecto | El "apodo" que Git le da a tu repositorio en GitHub cuando clonas. | `git push origin main` | — |
| **upstream** | El repositorio original del que hiciste fork | Se usa para mantener tu fork sincronizado con los cambios del proyecto original. | `git remote add upstream https://github.com/Kaia-Alenia/nerve-community.git` | — |
| **git status** | Estado actual de tu trabajo | Muestra qué archivos modificaste, cuáles están staged y cuáles no. | `git status` | — |
| **Conflict (Conflicto)** | Dos versiones del mismo código chocan | Ocurre cuando tú y otra persona editaron la misma línea del mismo archivo. Git no sabe cuál elegir. | `CONFLICT (content): Merge conflict in archivo.py` | — |
| **Rebase** | Reorganizar historial de commits | Mueve tus commits encima de otra rama. Más avanzado que merge. | `git rebase main` | — |
| **git log** | Historial de commits | Lista todos los commits de la rama actual con autor, fecha y mensaje. | `git log --oneline` | — |
| **git diff** | Ver qué cambió exactamente | Muestra las diferencias línea por línea entre tu versión actual y el último commit. | `git diff mi_archivo.py` | — |
| **git stash** | Guardar cambios temporalmente | Guarda tus cambios sin hacer commit para que puedas cambiar de rama y recuperarlos después. | `git stash` y luego `git stash pop` | — |
| **git commit --amend** | Corregir el último commit | Modifica el mensaje o los archivos del último commit. Solo funciona antes de hacer push. | `git commit --amend -m "Mensaje corregido"` | — |

---

## GitHub: Conceptos de Plataforma

| Término | Qué es | Para qué sirve | Ejemplo | Error común |
| :--- | :--- | :--- | :--- | :--- |
| **Issue** | Ticket o tarea dentro de GitHub | Donde se reportan bugs, se piden funciones o se hacen preguntas. | [Issues de Nerve Community](https://github.com/Kaia-Alenia/nerve-community/issues) | — |
| **Maintainer** | Mantenedor del proyecto | La persona con permisos para hacer merge de PRs y tomar decisiones sobre el proyecto. | `@Alenia-Studios` | — |
| **Contribuidor** | Persona que ha enviado código aceptado | Cualquier persona cuyo PR haya sido merged en el proyecto. | Ver `docs/COMO-USAR-COMO-ALUMNO.md` | — |
| **Label (Etiqueta)** | Categoría de un Issue o PR | Tags de colores que clasifican un Issue. | `good-first-issue`, `bug`, `disponible` | — |
| **Squash and Merge** | Fusionar aplastando commits en uno | Todos los commits del PR se unen en un solo commit limpio en `main`. | "Squashed and merged pull request #47" | — |
| **gh CLI** | GitHub CLI | Herramienta oficial de GitHub para operar la plataforma desde la terminal. | `gh pr create`, `gh auth login`, `gh pr list` | — |
| **GitHub Actions** | Automatizaciones del repositorio | Scripts que se ejecutan cuando ocurre algo en el repo (ej: alguien abre un PR). | El Linter Compasivo que formatea Python con `black` | — |
| **README.md** | El archivo de presentación del repo | El primer archivo que GitHub muestra al entrar a un repositorio. | Este mismo archivo que estás leyendo | — |
| **Sparse-Checkout** | Clonar solo una carpeta específica | Descarga únicamente la parte del repo que necesitas. Útil con datos limitados (ej: en Termux). | `git sparse-checkout set python/Modulo-01-Fundamentos` | — |
| **.gitignore** | Archivo de ignorados | Le dice a Git qué archivos o carpetas no debe rastrear ni subir. | Archivo llamado `.gitignore` | — |

---

> El ciclo básico que necesitas memorizar para tu primera contribución es: **fork → clone → branch → commit → push → PR**. El resto lo aprenderás con la práctica.

---

← [Volver al Índice del Glosario](README.md)
