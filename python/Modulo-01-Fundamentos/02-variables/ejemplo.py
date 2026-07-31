# ==========================================
# NIVEL 02: CAJAS MÁGICAS (VARIABLES)
# ==========================================

print("--- Guardando en la caja ---")

# Tomamos una caja, le pegamos la etiqueta "nombre_jugador"
# y metemos el texto "Alex" adentro (usando el símbolo =).
nombre_jugador = "Alex"

# Ahora imprimimos lo que hay en la caja.
# ¡Nota que NO usamos comillas alrededor de nombre_jugador!
print(nombre_jugador)

print("--- Reciclando cajas ---")

# Las variables pueden cambiar su contenido. Si metes algo nuevo en la caja,
# lo viejo se tira a la basura automáticamente.
nombre_jugador = "Sam"

# Ahora la caja tiene un texto diferente.
print(nombre_jugador)

print("--- Combinando texto y cajas (un vistazo al futuro) ---")

# Aunque más adelante veremos formas mejores de hacer esto,
# por ahora podemos imprimir varias cosas separadas por comas.
print("El jugador actual es:", nombre_jugador)
