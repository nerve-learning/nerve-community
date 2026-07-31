# 11 - Herramientas Avanzadas y Nerve

### `nerve.config`

**¿Qué es?**
Un archivo especial de configuración que guarda parámetros sobre cómo debe comportarse un agente o servicio dentro de la red de Nerve.

**¿Para qué se usa?**
Para guardar cosas como el nombre del agente, puertos a los que debe conectarse, o configuraciones locales, sin tener que "hardcodear" (escribir fijamente) esa información dentro del código de Python.

**Ejemplo:**
```json
{
  "agent_name": "procesador_de_datos",
  "hub_address": "127.0.0.1:8000"
}
```

**Errores comunes de principiante:**
- Subir este archivo a un repositorio público con contraseñas o tokens privados en su interior.

**Términos relacionados:** [`secrets`](#secrets)

### `sparse-checkout`

**¿Qué es?**
Una técnica avanzada de Git que permite descargar (clonar) solo una parte específica (una carpeta o archivo) de un repositorio gigante, en lugar de descargar todo el historial y todas las carpetas.

**¿Para qué se usa?**
Para ahorrar espacio y tiempo. Por ejemplo, si solo te interesa trabajar en el Módulo 05, no necesitas descargar todos los archivos, videos y recursos de los otros módulos.

**Ejemplo:**
```bash
git sparse-checkout set "python/Modulo-05"
```

**Errores comunes de principiante:**
- Confundirse y pensar que los demás archivos fueron borrados del proyecto, cuando en realidad solo están ocultos localmente por el sparse-checkout.

**Términos relacionados:** [Git (Glosario general)](../README.md)

### `GitHub Actions`

**¿Qué es?**
La plataforma de integración continua (CI/CD) integrada directamente en GitHub. Es básicamente una computadora en la nube que ejecuta tareas automáticamente cada vez que haces algo (como un `push` a tu repositorio).

**¿Para qué se usa?**
Para automatizar tareas repetitivas como: ejecutar pruebas en tu código, evaluar tus retos para ver si los pasaste, o hacer deploy (subir tu código a producción) de tu aplicación.

**Ejemplo:**
```yaml
# Un archivo en .github/workflows/main.yml le dice a GitHub qué hacer
name: Evaluador de Retos
on: [push]
jobs:
  evaluar:
    runs-on: ubuntu-latest
```

**Errores comunes de principiante:**
- Indentar mal los espacios en el archivo YAML de configuración, lo que causa que GitHub no entienda las instrucciones.

**Términos relacionados:** [`workflow / job / step`](#workflow--job--step)

### `workflow` / `job` / `step`

**¿Qué es?**
Son los bloques de construcción de GitHub Actions. Un **workflow** es el proceso completo automatizado. Un workflow contiene **jobs** (trabajos grandes como "probar" o "construir") que pueden correr en paralelo. Cada job se divide en **steps** (pasos individuales y secuenciales, como "instalar Python", "correr script").

**¿Para qué se usa?**
Para estructurar ordenadamente qué acciones debe tomar el servidor automático de GitHub.

**Ejemplo:**
```yaml
# workflow: Evaluación
jobs:
  # job: probar-codigo
  probar-codigo:
    steps:
      # step 1
      - name: Instalar dependencias
        run: pip install pytest
      # step 2
      - name: Correr tests
        run: pytest test_main.py
```

**Errores comunes de principiante:**
- Pensar que si un *step* falla, el siguiente se ejecutará (por defecto, si un paso falla, todo el job se detiene).

**Términos relacionados:** [`GitHub Actions`](#github-actions)

### `secrets`

**¿Qué es?**
Son variables de entorno cifradas y seguras que configuras en tu repositorio de GitHub para guardar información confidencial (contraseñas, tokens de APIs, claves SSH).

**¿Para qué se usa?**
Para que los *workflows* de GitHub Actions puedan usar una contraseña (por ejemplo, para publicar en un servidor) sin que nadie más pueda leerla en el código público.

**Ejemplo:**
```yaml
- name: Loguearse al servidor
  run: login --token ${{ secrets.MI_TOKEN_SECRETO }}
```

**Errores comunes de principiante:**
- Tratar de imprimir (hacer `echo`) un secret en la consola para ver si funciona; GitHub lo censurará y mostrará `***`.
- Olvidar definir el secret en la configuración del repositorio antes de intentar usarlo en el workflow.

**Términos relacionados:** [`GitHub Actions`](#github-actions)

### `pytest`

**¿Qué es?**
El framework (herramienta) más popular y utilizado para escribir pruebas (tests) de software en Python.

**¿Para qué se usa?**
Para comprobar automáticamente si tu código hace lo que se supone que debe hacer, sin tener que ejecutarlo manualmente a cada rato. Nerve usa pytest para evaluar automáticamente tus retos.

**Ejemplo:**
```python
def sumar(a, b): return a + b

def test_sumar():
    assert sumar(2, 3) == 5 # Si esto es verdad, la prueba pasa
```

**Errores comunes de principiante:**
- Escribir funciones de prueba sin el prefijo `test_`, causando que pytest simplemente las ignore al ejecutar.

**Términos relacionados:** [`coverage`](#coverage)

### `coverage`

**¿Qué es?**
La "cobertura de código". Es una métrica (un porcentaje) que te indica qué tanta cantidad de tu código fuente fue ejecutada durante tus pruebas automáticas.

**¿Para qué se usa?**
Para detectar partes de tu programa que nunca se han probado. Si tienes un `if`/`else`, y tus tests solo pasan por el `if`, tu *coverage* te avisará que te falta probar la situación del `else`.

**Ejemplo:**
```bash
# Correr tests calculando la cobertura
pytest --cov=mi_programa
# Salida: mi_programa.py  85% de cobertura
```

**Errores comunes de principiante:**
- Obsesionarse con llegar al 100% de coverage escribiendo pruebas tontas, en lugar de asegurar que las funciones críticas se prueben con casos reales (calidad sobre cantidad).

**Términos relacionados:** [`pytest`](#pytest)

### `linter` / `flake8` / `black`

**¿Qué es?**
Un **linter** es un programa que analiza tu código para encontrar errores de estilo o posibles bugs sin necesidad de ejecutarlo. `flake8` es un linter famoso en Python. `black` es un formateador: reescribe automáticamente tu código para que cumpla con los estándares estéticos.

**¿Para qué se usa?**
Para que el código de un equipo grande parezca escrito por una sola persona. Evita discusiones sobre si usar comillas simples o dobles, o cuántos espacios dejar, porque la herramienta toma esas decisiones por ti de forma estandarizada (PEP 8).

**Ejemplo:**
```bash
# Formatea todo tu código a la perfección
black mi_script.py

# Revisa si hay errores lógicos o variables sin usar
flake8 mi_script.py
```

**Errores comunes de principiante:**
- Ignorar las advertencias del linter pensando que "si corre, está bien", acumulando "deuda técnica" (código difícil de leer).

**Términos relacionados:** [PEP 8 (Estilos de código)](#)
