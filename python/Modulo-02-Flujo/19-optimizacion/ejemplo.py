# ejemplo.py

print("--- 1. Aplanando Nidos (Combinando condiciones) ---")

# Código de un sistema de alarma
puerta_cerrada = True
alarma_activada = True
movimiento_detectado = False

# VERSIÓN NOVATO (Muchas líneas, difícil de leer)
print("Evaluando versión novato...")
if puerta_cerrada:
    if alarma_activada:
        if not movimiento_detectado:
            print("Todo seguro en la casa.")

# VERSIÓN PROFESIONAL (Una sola línea de decisión)
print("Evaluando versión profesional...")
if puerta_cerrada and alarma_activada and not movimiento_detectado:
    print("Todo seguro en la casa.")


print("\n--- 2. Asignación Directa ---")
# Sistema de VIP en un club
dinero_en_cuenta = 5000

# VERSIÓN NOVATO
if dinero_en_cuenta >= 1000:
    es_cliente_vip = True
else:
    es_cliente_vip = False

# VERSIÓN PROFESIONAL (El comparador '>=' ya devuelve True o False)
# Guardamos la respuesta directamente en la caja 'es_cliente_vip'
es_cliente_vip = dinero_en_cuenta >= 1000

print("¿El cliente es VIP?", es_cliente_vip)


print("\n--- 3. Limpiando Redundancias ---")
tiene_cupon = True

# VERSIÓN NOVATO
if tiene_cupon == True:
    print("Aplicando descuento (novato).")

# VERSIÓN PROFESIONAL
# 'tiene_cupon' ya vale True, el 'if' solo necesita leerlo.
if tiene_cupon:
    print("Aplicando descuento (profesional).")
