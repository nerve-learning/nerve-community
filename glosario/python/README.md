# Glosario de Python

Referencia técnica de los términos de Python que aparecen en los módulos del curso. Cada archivo cubre los conceptos introducidos en su módulo correspondiente.

---

## Cómo funciona el glosario

Si estás trabajando desde tu repositorio privado generado con `nerve--template`, no tienes que venir aquí a leer todo de golpe.

El glosario de Python está dividido en archivos por módulo. Cada archivo cubre exactamente los conceptos que introduces en ese módulo, para que puedas consultarlo cuando algo no te quede claro.

---

## Índice de archivos

| Archivo | Módulo del curso | Contenido principal |
| :--- | :--- | :--- |
| [01-fundamentos.md](01-fundamentos.md) | Modulo-01-Fundamentos | Variables, tipos de datos, operadores, f-strings, comentarios, indentación |
| [02-control-de-flujo.md](02-control-de-flujo.md) | Modulo-02-Flujo | `if`/`elif`/`else`, `for`, `while`, `match`, `break`, `continue` |
| [03-funciones.md](03-funciones.md) | Modulo-03-Estructuras → Modulo-05-Funciones | `def`, parámetros, `return`, `*args`, `**kwargs`, lambdas, scope |
| [04-estructuras-de-datos.md](04-estructuras-de-datos.md) | Modulo-03-Estructuras → Modulo-04-Bucles | Listas, tuplas, diccionarios, sets, list comprehension |
| [05-modulos-y-librerias.md](05-modulos-y-librerias.md) | Modulo-05-Funciones → Modulo-06-OS | `import`, `pip`, `venv`, `requirements.txt`, módulos de la librería estándar (`os`, `pathlib`, `json`, `csv`, `datetime`, `re`, `random`, `secrets`, `argparse`) |
| [06-manejo-de-errores.md](06-manejo-de-errores.md) | Modulo-05.5-Calidad-de-Codigo | `try`/`except`/`finally`, `raise`, excepciones comunes, manejo robusto |
| [07-archivos-y-entrada-salida.md](07-archivos-y-entrada-salida.md) | Modulo-06-OS | `open()`, modos de apertura, `with`, lectura/escritura de CSV y JSON |
| [08-poo-basica.md](08-poo-basica.md) | Modulo-08-POO | `class`, `__init__`, `self`, herencia, métodos especiales |
| [09-data-ia.md](09-data-ia.md) | Modulo-09-Data-IA | `numpy`, `pandas`, `matplotlib`, `scikit-learn`, análisis de CSV |
| [10-nerve-ipc.md](10-nerve-ipc.md) | Modulo-10-Nerve | IPC, `NexusHub`, `NexusClient`, Pub/Sub, Unix Sockets con Python |
| [11-herramientas-avanzadas.md](11-herramientas-avanzadas.md) | Modulo-11-Herramientas-Nerve | `nerve.config`, GitHub Actions, `pytest`, linters, coverage |
| [12-arquitectura-avanzada.md](12-arquitectura-avanzada.md) | Modulo-12-Arquitectura-Avanzada | Microservicios, orquestador, failover, `async`/`await` |

---

## Cómo contribuir

Si notas que falta un término importante, que una explicación es confusa o que falta un buen ejemplo, puedes contribuir:

1. Haz Fork del repositorio `nerve-community`.
2. Crea una rama nueva.
3. Edita el archivo `.md` correspondiente siguiendo el formato existente: **¿Qué es?**, **¿Para qué se usa?**, **Ejemplo de código**, **Errores comunes**.
4. Haz Push y abre un Pull Request.

Para más detalles sobre el flujo de contribución, lee: [Cómo hacer tu primer PR](../../COMO-HACER-TU-PRIMER-PR.md)

---

← [Volver al Índice del Glosario](../README.md)
