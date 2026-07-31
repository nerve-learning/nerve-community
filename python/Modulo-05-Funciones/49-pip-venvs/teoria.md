# Teoría: Pip y Entornos Virtuales

## ¿Qué son `pip` y los Entornos Virtuales?
Imagina que Python viene con una caja de herramientas básica. Pero a veces quieres construir algo avanzado y necesitas herramientas especiales (como una motosierra o un taladro) que alguien más ya inventó.

- **`pip`**: Es como un centro comercial gigante en internet (llamado PyPI) donde puedes descargar herramientas (librerías) gratis. `pip` significa "Pip Installs Packages" (Pip instala paquetes).
- **Entorno Virtual (`venv`)**: Imagina que trabajas en dos proyectos. En uno necesitas pintura azul y en otro pintura roja. Si metes todo en la misma mochila, se puede hacer un desastre. Un entorno virtual es una "mochila" aislada solo para un proyecto.

## Desmontaje Conceptual (Símbolos en la Terminal)
Hoy no usaremos tanto código de Python, sino **comandos en la terminal** (la pantalla negra).
1. `python -m venv nombre_del_entorno`: 
   - `python`: Llama a Python.
   - `-m`: Significa "módulo" (vamos a usar un módulo interno).
   - `venv`: El módulo que crea entornos virtuales.
   - `nombre_del_entorno`: Es el nombre de la carpeta (mochila) que vas a crear (comúnmente se usa `env` o `venv`).
2. `source env/bin/activate` (Mac/Linux) o `env\Scripts\activate` (Windows):
   - Esto "abre tu mochila" para que empieces a usar lo que hay adentro.
   - Sabrás que está abierta porque en tu terminal aparecerá `(env)` al inicio.
3. `pip install nombre_del_paquete`:
   - `install`: La orden para descargar e instalar algo.
   - `nombre_del_paquete`: El nombre de la herramienta que quieres. (Ej: `colorama`, para ponerle color al texto).

## Anatomía de un Proyecto
Así se ve tu carpeta antes y después de crear un entorno:

**Antes:**
MiProyecto/
  L__ mi_codigo.py

**Después:**
MiProyecto/
  L__ env/ (¡La mochila con herramientas!)
  L__ mi_codigo.py
