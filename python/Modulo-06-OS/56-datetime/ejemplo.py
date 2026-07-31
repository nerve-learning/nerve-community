# --- 1. Trayendo el reloj del sistema ---
# 'import' nos trae la caja de herramientas del tiempo
import datetime

print("--- Consultando el reloj maestro ---")

# Le pedimos a Python que capture el instante exacto en este momento.
# .now() es una acción, por eso lleva ().
ahora = datetime.datetime.now()

print("El paquete de tiempo completo se ve así de crudo para los humanos:")
print(ahora)


# --- 2. Desarmando el paquete de tiempo ---
print("\n--- Sacando las piezas de información ---")

# Usamos el punto para acceder a las gavetas de información dentro de 'ahora'.
# ¡Nota que NO usamos paréntesis al final porque son solo datos, no acciones!
el_anio = ahora.year
el_mes = ahora.month
el_dia = ahora.day

la_hora = ahora.hour
los_minutos = ahora.minute

print("Año extraído:", el_anio)
print("Mes extraído:", el_mes)
print("Día extraído:", el_dia)


# --- 3. Dando formato humano ---
print("\n--- Reloj Amigable ---")

# Ya sabemos usar variables, así que podemos armar nuestro propio texto
# separando los elementos con comas en nuestro print.
print("Hoy es el día", el_dia, "del mes", el_mes, "del año", el_anio)
print("Y son exactamente las", la_hora, "con", los_minutos, "minutos.")

print("\n--- ¡Viaje en el tiempo completado! ---")
