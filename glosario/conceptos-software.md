# Glosario: Conceptos de Software

Términos generales de desarrollo de software que aparecen en los retos, la documentación y las conversaciones del día a día en Nerve Community.

---

## Tipos de Archivos y Formatos de Datos

| Término | Qué es | Para qué sirve | Ejemplo |
| :--- | :--- | :--- | :--- |
| **Markdown (.md)** | Lenguaje de marcado simple | Formato de texto con sintaxis sencilla (`**negrita**`, `# Título`) que se convierte en HTML. GitHub lo renderiza automáticamente. | Este archivo que estás leyendo |
| **TXT** | Archivo de texto plano | El formato más básico. Sin formato ni colores, solo caracteres. | `notas.txt`, `requirements.txt` |
| **YAML (.yml / .yaml)** | Yet Another Markup Language | Formato de configuración legible para humanos. Usado en CI/CD como GitHub Actions. | Los workflows en `.github/workflows/` |

---

## Arquitectura y Diseño de Software

| Término | Qué es | Para qué sirve | Ejemplo |
| :--- | :--- | :--- | :--- |
| **CLI (Command Line Interface)** | Interfaz de línea de comandos | Un programa que se usa desde la terminal escribiendo texto en vez de clicando botones. La mayoría de los retos son CLIs. | `python3 lista_tareas.py --agregar "Estudiar"` |
| **Librería / Biblioteca** | Código reutilizable empaquetado | Colección de funciones y clases escritas por otros que puedes importar sin reinventar la rueda. | `import requests` |
| **Framework** | Estructura base para construir apps | Un esqueleto con reglas y herramientas que te dice cómo organizar tu proyecto. Más opinionado que una librería. | FastAPI (para APIs), discord.py (para bots) |
| **Módulo** | Unidad básica de código reutilizable | Un archivo `.py` con funciones que puedes importar en otros archivos. | `from conversiones import celsius_a_fahrenheit` |
| **Dependencia** | Librería de la que depende tu código | Una librería externa que tu proyecto necesita para funcionar. Si no está instalada, el programa falla. | `requests` es una dependencia del módulo de APIs |
| **Open Source (Código Abierto)** | Software con código público y libre | Software cuyo código fuente es público, gratuito y puede ser modificado y redistribuido. Nerve y este repo son Open Source. | Licencia GNU GPL v3 |
| **GNU GPL v3** | Licencia de Nerve Community | Una licencia Open Source que garantiza que el software es libre y que cualquier derivado también debe serlo. | El archivo `LICENSE` en el repo |
| **multiplataforma** | Funciona en varios sistemas operativos | Software que funciona en Linux, macOS y Windows sin cambios. | Nerve usa Unix Sockets en Linux/macOS y TCP en Windows |
| **offline-first** | Funciona sin internet | Diseñado para funcionar sin conexión a internet. Nerve se conecta localmente, no usa la nube. | Nerve solo necesita que los procesos estén en la misma máquina |

---

## Calidad, Bugs y Proceso de Desarrollo

| Término | Qué es | Para qué sirve | Ejemplo |
| :--- | :--- | :--- | :--- |
| **Bug** | Error en el software | Fallo en el código que hace que el programa no funcione como se esperaba. | "El conversor de divisas dice que 1 USD = 0 MXN. Es un bug." |
| **Debugging** | Proceso de encontrar y corregir bugs | El arte de investigar y corregir errores. Puede ser con herramientas o simplemente leyendo y pensando. | Usar `print()` para ver el valor de una variable |
| **Refactoring** | Mejorar código sin cambiar su comportamiento | Reescribir el código para que sea más limpio o eficiente, sin que haga cosas diferentes. | Dividir una función gigante en varias pequeñas |
| **Linter** | Analizador automático de estilo | Herramienta que revisa tu código buscando errores de formato, malas prácticas o inconsistencias. | `black` (Python), que usa el CI del repo |
| **CI/CD** | Integración y entrega continua | Automatizaciones que corren con cada PR: tests, verificación de formato, despliegue. | El Linter Compasivo que corre en cada PR de Nerve Community |
| **Test / Prueba** | Código que verifica que tu código funciona | Pequeños programas automáticos que comprueban si tus funciones devuelven los resultados esperados. | `assert suma(2, 3) == 5` |
| **edge case** | Caso borde o extremo | Una entrada o situación inusual que puede romper tu programa. Pensar en ellos es parte del desarrollo robusto. | ¿Qué pasa si el usuario escribe una letra donde va un número? |
| **hardcoded** | Valor fijo escrito directamente en el código | Un valor que no se puede cambiar sin editar el código fuente. Es mala práctica para configuraciones y rutas. | `ruta = "/home/user/Descargas"` (incorrecto) |
| **dry-run** | Modo de simulación sin cambios reales | Ejecutar un script para que muestre qué haría, sin modificar nada. Fundamental en scripts que mueven archivos. | `python organizador.py --dry-run` |
| **logging** | Registro de eventos del programa | Guardar mensajes sobre lo que hace el programa mientras corre. Útil para diagnosticar problemas. | `logging.info("Archivo procesado: datos.csv")` |

---

## Conceptos de Seguridad

| Término | Qué es | Para qué sirve | Ejemplo |
| :--- | :--- | :--- | :--- |
| **Criptografía** | Ciencia de proteger información | Técnicas para cifrar datos y hacer comunicaciones seguras. | HTTPS cifra los datos entre tu navegador y el servidor |
| **random vs secrets** | Diferencia crucial en Python | `random` genera números predecibles (no seguros para contraseñas). `secrets` genera números criptográficamente seguros. | `secrets.token_urlsafe(16)` para contraseñas reales |
| **Token de acceso** | Llave de autenticación | Una cadena larga y aleatoria que actúa como contraseña para autenticar accesos a una API o servicio. | Token de GitHub para usar `gh auth login` |

---

## El Ecosistema Alenia / Nerve

| Término | Qué es | Ejemplo |
| :--- | :--- | :--- |
| **Nerve** | Motor IPC de Alenia Studios | El sistema de comunicación entre procesos que es el tema central de este repo. Los retos de nivel Core giran en torno a él. Repositorio: [alenia-nerve](https://github.com/Kaia-Alenia/alenia-nerve) |
| **Zenith** | Framework principal de Alenia Studios | Donde viven las herramientas más maduras de Alenia. Las mejores soluciones de este repo pueden graduarse a Zenith. |
| **nerve-community** | Este repositorio | El espacio de aprendizaje y contribución para construir herramientas usando Nerve de forma abierta. |
| **TRANSPARENCIA.md** | Informe de uso de donaciones | Documento público donde se detalla cómo se usaron los fondos de la comunidad. Ver: [TRANSPARENCIA.md](../TRANSPARENCIA.md) |

---

> Antes de instalar una librería o escribir código complejo, pregúntate: ¿ya existe algo en la librería estándar que haga esto? La mayoría de las veces, la respuesta es sí.

---

← [Volver al Índice del Glosario](README.md)
