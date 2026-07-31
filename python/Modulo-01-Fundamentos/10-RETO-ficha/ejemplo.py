# ==========================================
# NIVEL 10: PROYECTO DE EJEMPLO
# ==========================================

print("--- 🍔 Creador de Recetas 🍔 ---")

# 1. Pedimos datos al usuario
nombre_plato = input("¿Qué plato vas a cocinar?: ")
ingrediente_principal = input("¿Cuál es el ingrediente principal?: ")
precio_ingrediente_texto = input("¿Cuánto cuesta este ingrediente? (ej. 15.50): ")
porciones_texto = input("¿Para cuántas personas alcanza?: ")

# 2. Transformamos los datos (casteo) para poder hacer cálculos
precio_ingrediente = float(precio_ingrediente_texto)
porciones = int(porciones_texto)

# 3. Hacemos cálculos (Matemáticas)
# Calculamos el costo por persona y un impuesto imaginario del 10%
costo_por_persona = precio_ingrediente / porciones
costo_con_impuesto = costo_por_persona + (costo_por_persona * 0.10)

# 4. Mostramos el resultado final (f-strings)
print("\n--- 📋 Tu Receta 📋 ---")
print(f"Plato: {nombre_plato}")
print(f"Estrella del plato: {ingrediente_principal}")
print(f"Rinde para: {porciones} valientes.")
print(f"Costo por persona (con impuestos): ${costo_con_impuesto}")

# Fin del programa
print("¡A cocinar se ha dicho!")
