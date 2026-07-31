# ejemplo.py

print("--- CALENTAMIENTO: El Cajero de Peaje ---")
# Vamos a usar todo lo aprendido para calcular cuánto paga un auto.

tipo_vehiculo = "camion" # Puede ser "moto", "auto", "camion"
numero_pasajeros = 1
es_hora_pico = True

# Usamos match-case porque evaluamos EXACTAMENTE una variable contra opciones fijas
match tipo_vehiculo:
    case "moto":
        tarifa_base = 5
        print("Tarifa base de moto: $5")
    case "auto":
        tarifa_base = 10
        print("Tarifa base de auto: $10")
    case "camion":
        tarifa_base = 20
        print("Tarifa base de camión: $20")
    case _:
        # Red de seguridad
        tarifa_base = 0
        print("Vehículo desconocido, deténgase.")

# Si es un vehículo válido (tarifa_base > 0), aplicamos las reglas de flujo
if tarifa_base > 0:
    
    # 1. Regla de carpool (Optimización con Truthy y and)
    if tipo_vehiculo == "auto" and numero_pasajeros >= 4:
        print("¡Auto compartido! Descuento aplicado.")
        tarifa_base = tarifa_base - 3
        
    # 2. Regla de hora pico
    if es_hora_pico:
        print("Es hora pico, hay recargo.")
        tarifa_base = tarifa_base + 5
        
    print("TOTAL A PAGAR: $", tarifa_base)

else:
    print("No se puede calcular el cobro.")

print("------------------------------------------")
