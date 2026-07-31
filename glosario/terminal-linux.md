# Glosario: Terminal — Linux y macOS

Guía de la terminal para usuarios de Linux, macOS y Termux (Android). Si estás en Windows, consulta el [Glosario de Windows](terminal-windows.md).

---

## Conceptos Universales de Terminal

| Término | Qué es | Ejemplo |
| :--- | :--- | :--- |
| **Shell** | El intérprete de comandos | El programa que lee lo que escribes y lo ejecuta. Ejemplos: `bash`, `zsh`, `fish` |
| **bash** | El shell más común en Linux | El intérprete por defecto en la mayoría de distros Linux y en los servidores. macOS usa `zsh` por defecto desde 2019. |
| **`~` (virgulilla)** | Carpeta de inicio del usuario | Atajo para `/home/tu_usuario/` en Linux o `/Users/tu_usuario/` en macOS. `cd ~` te lleva a inicio. |
| **`.` (punto)** | La carpeta actual | Representa donde estás ahora mismo. `git add .` prepara todo lo que hay aquí. |
| **`..` (dos puntos)** | La carpeta superior (padre) | Sube un nivel en el árbol de carpetas. `cd ..` sube un nivel. |

---

## Comandos Esenciales de Linux y macOS

| Comando | Qué hace | Ejemplo |
| :--- | :--- | :--- |
| `pwd` | Muestra la ruta completa de donde estás | `pwd` → `/home/alejandro/nerve-community` |
| `ls` | Lista archivos y carpetas | `ls` o `ls -la` (con detalles y archivos ocultos) |
| `cd` | Cambia de carpeta | `cd python/Modulo-01-Fundamentos` o `cd ..` |
| `mkdir` | Crea una carpeta nueva | `mkdir mi-solucion` |
| `cp` | Copia archivos o carpetas | `cp archivo.py copia.py` |
| `mv` | Mueve o renombra archivos | `mv viejo.py nuevo.py` |
| `rm` | Borra archivos — permanente, sin papelera | `rm archivo.py` o `rm -rf carpeta/` |
| `cat` | Muestra el contenido de un archivo | `cat README.md` |
| `nano` | Editor de texto simple en terminal | `nano mi_script.py` — `Ctrl+O` guarda, `Ctrl+X` sale |
| `echo` | Imprime texto en la terminal | `echo "Hola mundo"` |
| `clear` | Limpia la pantalla | `clear` |
| `which` | Muestra dónde está instalado un programa | `which python3` → `/usr/bin/python3` |
| `grep` | Busca texto dentro de archivos | `grep "def " mi_script.py` |
| `chmod` | Cambia permisos de un archivo | `chmod +x script.sh` (hacerlo ejecutable) |
| `df -h` | Muestra espacio en disco disponible | `df -h` — `-h` muestra tamaños en MB/GB |
| `sudo` | Ejecutar un comando como administrador | `sudo apt install git` |
| `apt` | Gestor de paquetes de Ubuntu/Debian | `sudo apt install python3` |
| `&&` | Encadenar comandos | `git add . && git commit -m "mensaje"` — el segundo solo corre si el primero tuvo éxito |

---

## Python desde la Terminal (Linux y macOS)

| Comando | Qué hace | Ejemplo |
| :--- | :--- | :--- |
| `python3` | Ejecutar un script Python | `python3 mi_script.py` |
| `python3 --version` | Ver la versión de Python instalada | `python3 --version` → `Python 3.11.2` |
| `pip3 install` | Instalar una librería externa | `pip3 install requests` |
| `pip3 install -r requirements.txt` | Instalar todas las dependencias del proyecto | `pip3 install -r requirements.txt` |
| `pip3 list` | Ver librerías instaladas | `pip3 list` |
| `pip3 freeze` | Generar el archivo requirements.txt | `pip3 freeze > requirements.txt` |

> En Linux y macOS usa `python3` y `pip3` (con el `3`). Sin el `3`, algunos sistemas ejecutan Python 2, que está obsoleto.

---

## Termux (Android)

Termux es una terminal Linux que corre en tu celular Android, sin necesidad de root ni PC.

| Término | Qué es | Ejemplo |
| :--- | :--- | :--- |
| **Termux** | Terminal Linux para Android | Emula una terminal Linux completa en tu celular. Instálalo solo desde F-Droid; la versión de Play Store está descontinuada. |
| **F-Droid** | Tienda de apps Open Source | La fuente correcta para descargar Termux. `https://f-droid.org` |
| **pkg** | Gestor de paquetes de Termux | El equivalente de `apt` en Termux. `pkg install python git gh -y` |
| **pkg update && pkg upgrade** | Actualizar paquetes de Termux | Primer comando a correr al abrir Termux por primera vez. |
| **termux-setup-storage** | Dar acceso al almacenamiento del celular | Permite que Termux acceda a las carpetas de Descargas, etc. |
| **Acode** | Editor de código para Android | App con resaltado de sintaxis para editar archivos de Termux cómodamente. Disponible en F-Droid y Play Store. |

> En Termux puedes usar exactamente los mismos comandos de Linux de la tabla de arriba.

---

## Variables de Entorno (Linux y macOS)

| Término | Qué es | Ejemplo |
| :--- | :--- | :--- |
| **export** | Exportar una variable al entorno | Hace que la variable esté disponible para los procesos de esa sesión. `export API_KEY="mi_clave"` |
| **.env** | Archivo de variables de entorno locales | Guarda claves y configuración. Nunca se sube a GitHub (va en `.gitignore`). `API_KEY=mi_clave` dentro del archivo. |

---

← [Volver al Índice del Glosario](README.md) | → [Glosario Windows](terminal-windows.md)
