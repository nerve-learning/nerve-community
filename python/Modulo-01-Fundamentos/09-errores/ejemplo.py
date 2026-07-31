# ==========================================
# NIVEL 09: EL ARTE DE EQUIVOCARSE
# ==========================================

# NOTA: Este programa está diseñado para fallar. 
# Si lo ejecutas tal como está, Python te mostrará errores.
# Para ver cada error, debes ir comentando (poniendo un #) 
# la línea que falló, y luego volver a ejecutar.

print("--- Iniciando simulador de errores ---")

# 1. SyntaxError (Error de Sintaxis)
# Aquí nos falta el paréntesis de cierre al final.
# Descomenta (quita el #) de la siguiente línea para ver el error:
# print("Se me olvidó cerrar esto"

# 2. NameError (Error de Nombre)
# Vamos a crear una variable, pero luego la escribiremos mal.
nombre_usuario = "Alejandro"

# Python dirá: name 'nombre_usario' is not defined
# Descomenta la siguiente línea para ver el error:
# print(f"Bienvenido, {nombre_usario}") 

# 3. TypeError (Error de Tipo)
# Intentaremos sumar texto con números directamente, sin f-strings.
manzanas = 5

# Python dirá: can only concatenate str (not "int") to str
# Descomenta la siguiente línea para ver el error:
# print("Tengo " + manzanas + " manzanas")

print("Si ves este mensaje, significa que todos los errores anteriores están comentados (desactivados).")
