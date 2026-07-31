# ejemplo.py

print("--- 1. El Menú de la Cafetería ---")

print("Menú: 1=Café, 2=Té, 3=Chocolate")
opcion_elegida = 2

# Usamos 'match' y le entregamos la variable que queremos revisar.
match opcion_elegida:
    # Si la variable vale 1...
    case 1:
        print("☕ Preparando un Café calientito.")
    # Si la variable vale 2...
    case 2:
        print("🍵 Preparando un Té de manzanilla.")
    # Si la variable vale 3...
    case 3:
        print("🍫 Preparando un Chocolate espeso.")
    # El comodín: Si la variable no fue ni 1, ni 2, ni 3...
    case _:
        print("❓ Lo siento, no tenemos esa opción en el menú.")


print("\n--- 2. Evaluando días de la semana (Textos) ---")

dia_actual = "sábado"

match dia_actual:
    case "lunes":
        print("A iniciar la semana con energía.")
    case "viernes":
        print("¡Por fin es viernes!")
    case "sábado":
        print("Día de descanso y diversión.")
    case "domingo":
        print("Día de preparar las cosas para mañana.")
    case _:
        print("Es un día regular a mitad de semana.")


print("\n--- 3. Juntando opciones usando el símbolo '|' (O lógico del match) ---")

# ¿Qué pasa si varias opciones hacen exactamente lo mismo?
# Podemos usar la barra vertical '|', que en los 'case' significa "o".
# OJO: La barra '|' suele estar en tu teclado arriba de la tecla Tab o cerca del número 1.

direccion = "norte"

match direccion:
    # Esto se lee: caso "norte" O caso "sur"
    case "norte" | "sur":
        print("Te estás moviendo en el eje Vertical.")
    case "este" | "oeste":
        print("Te estás moviendo en el eje Horizontal.")
    case _:
        print("Dirección desconocida.")
