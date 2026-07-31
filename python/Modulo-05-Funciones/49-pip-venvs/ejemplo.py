# ==========================================
# EL MAGO Y SUS HERRAMIENTAS MÁGICAS
# ==========================================
# Historia: El mago acaba de comprar un "paquete" de colores en el centro comercial (pip).
# Para usarlo, primero tuvo que preparar su mochila mágica (entorno virtual) e instalarlo.

# ------------------------------------------
# INSTRUCCIONES ANTES DE CORRER ESTE CÓDIGO
# ------------------------------------------
# Abre tu terminal en esta carpeta y escribe:
# 1. Crear el entorno: python -m venv mi_entorno
# 2. Activar entorno (Windows): mi_entorno\Scripts\activate
#    Activar entorno (Mac/Linux): source mi_entorno/bin/activate
# 3. Instalar la herramienta: pip install colorama
# 4. Ahora sí, corre este archivo: python ejemplo.py
# ------------------------------------------

# Ahora usamos la herramienta externa 'colorama' que instalamos.
import colorama

# Iniciamos colorama para que funcione en cualquier computadora
colorama.init()

# colorama nos da variables con colores que podemos poner en nuestros textos
print(colorama.Fore.RED + "¡El dragón escupe fuego!")
print(colorama.Fore.BLUE + "El mago lanza un hechizo de agua.")
print(colorama.Fore.GREEN + "El bosque recupera su energía.")

# Regresamos el color a la normalidad al final
print(colorama.Style.RESET_ALL + "La batalla ha terminado y el mundo vuelve a la normalidad.")
