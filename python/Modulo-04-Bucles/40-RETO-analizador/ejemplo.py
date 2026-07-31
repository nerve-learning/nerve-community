# ==========================================
# Archivo: ejemplo.py
# Autor: Kaia / Alenia Studios
# Descripción: El Analizador de Pociones Mágicas
# ==========================================

print("--- Iniciando Analizador de Inventario ---")

# 1. PREPARACIÓN (Nuestros datos crudos y nuestras cajas para resultados)
ingredientes_recolectados = ["hongo", "hongo", "veneno", "flor", "hongo", "flor"]

# Usaremos un diccionario para llevar la cuenta de lo que nos sirve
conteo_seguro = {
    "hongo": 0,
    "flor": 0
}

# 2. EL MOTOR (El bucle que analiza todo)
print("Analizando cada ingrediente...")

for ingrediente in ingredientes_recolectados:
    
    # 3. LA REACCIÓN (Tomar decisiones sobre el dato)
    if ingrediente == "veneno":
        print("¡ALERTA TÓXICA! Encontramos veneno. Deteniendo el análisis.")
        # El veneno es tan peligroso que tiramos a la basura el inventario y paramos el motor
        break
        
    elif ingrediente == "hongo":
        print("Encontré un hongo. Guardando...")
        conteo_seguro["hongo"] = conteo_seguro["hongo"] + 1
        
    elif ingrediente == "flor":
        print("Encontré una flor. Guardando...")
        conteo_seguro["flor"] = conteo_seguro["flor"] + 1

print("--- Análisis Terminado ---")
print("Resultados finales del inventario:")
print(conteo_seguro)
