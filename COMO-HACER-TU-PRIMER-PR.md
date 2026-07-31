# Cómo hacer tu primer Pull Request

> [!IMPORTANT]
> Si estás aquí para resolver los retos de aprendizaje como alumno, lee primero [COMO-USAR-COMO-ALUMNO.md](docs/COMO-USAR-COMO-ALUMNO.md) y [RETOS-SOCRATICOS.md](docs/RETOS-SOCRATICOS.md). Esta guía es para contribuidores que quieren mejorar el material del repositorio.

Si es la primera vez que escuchas sobre Git, GitHub o Pull Request, estás en el lugar correcto. Aquí explicamos paso a paso cómo contribuir a este —o a cualquier— proyecto open source.

Para entender los términos que aparecen en esta guía, consulta el [Glosario de Git y GitHub](glosario/git-github.md).

---

## El flujo completo (diagrama)

```text
[Repositorio Original]
       |
       | (1. Fork)
       v
[Tu copia en GitHub] ──────┐
       |                   | (6. Pull Request y Revisión)
       | (2. Clone)        |
       v                   |
[Tu computadora]           |
       | (3. Branch)       |
       | (4. Escribir)     |
       | (5. Commit/Push) ─┘
```

---

## Preparativos (solo se hace una vez)

**1. Instala Git**

- Windows: descarga [Git for Windows](https://gitforwindows.org/) e instálalo.
- macOS: abre la terminal y escribe `git --version`. Si no lo tienes, te pedirá instalarlo.
- Linux: `sudo apt install git`

**2. Identifícate ante Git**

Abre tu terminal y configura tu nombre y correo (el mismo que usas en GitHub):

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu_correo@ejemplo.com"
```

**3. Autentícate con GitHub**

GitHub no permite usar contraseñas normales desde la terminal. La forma más sencilla es instalar la [GitHub CLI](https://cli.github.com/) y ejecutar:

```bash
gh auth login
```

Sigue las instrucciones: elige `GitHub.com`, luego `HTTPS`, luego `Login with a web browser`. Se abrirá el navegador para autorizar el acceso.

Alternativa sin `gh`: ve a tu perfil de GitHub → Settings → Developer Settings → Personal access tokens → Tokens (classic). Genera un token marcando la casilla `repo` y úsalo como contraseña cuando la terminal te lo pida al hacer `git push`.

---

## Paso a paso

### 1. Fork

Ve a la página del repositorio y haz clic en el botón **Fork**. Esto crea una copia del proyecto en `https://github.com/TU-USUARIO/nerve-community`.

### 2. Clone

Abre tu terminal en la carpeta donde guardas tus proyectos y descarga tu fork:

```bash
git clone https://github.com/TU-USUARIO/nerve-community.git
cd nerve-community
```

### 3. Crear una rama

Nunca trabajes directamente en `main`. Crea una rama con un nombre descriptivo del cambio que vas a hacer:

```bash
git checkout -b mejora-glosario-git
```

### 4. Haz tus cambios

Usa tu editor preferido. Navega a los archivos que quieres mejorar y realiza los cambios.

Si estás resolviendo un reto socrático, ve a la carpeta correspondiente (por ejemplo `python/Modulo-01-Fundamentos/`) y escribe tu código. Verifica que los tests pasen localmente antes de continuar:

```bash
pytest test_main.py
```

### 5. Commit

Revisa qué archivos modificaste:

```bash
git status
```

Prepara los archivos y crea el punto de guardado:

```bash
git add .
git commit -m "feat: corrige explicación de git rebase en glosario"
```

Usa mensajes descriptivos. El prefijo `feat:` es para cambios nuevos, `fix:` para correcciones, `docs:` para documentación.

### 6. Push

Sube tu rama a tu copia en GitHub:

```bash
git push origin mejora-glosario-git
```

### 7. Abre el Pull Request

Ve a la página de tu fork en GitHub. Verás un banner que dice "Compare & pull request". Haz clic, rellena la plantilla del PR marcando las casillas correspondientes y envíalo.

---

## Errores comunes

**"Escribí código directamente en main por accidente."**
No pasa nada si aún no hiciste commit. Escribe `git checkout -b nueva-rama` y tus cambios se moverán a esa nueva rama.

**"Hice un commit pero me equivoqué en el mensaje."**
Escribe `git commit --amend -m "Mensaje corregido"`. Solo funciona antes de hacer push.

**"Dice que tengo conflictos de merge."**
Ocurre cuando alguien más editó los mismos archivos que tú. En VS Code, los archivos con conflictos muestran las diferencias resaltadas. Elige qué código mantener, guarda el archivo y luego:
```bash
git add .
git commit -m "fix: resuelve conflictos de merge"
```

---

← [Volver al repositorio](README.md)
