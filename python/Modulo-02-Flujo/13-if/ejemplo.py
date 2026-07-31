# ejemplo.py

print("--- 1. El Cajero del Banco ---")

# Vamos a simular un retiro de efectivo.
saldo_bancario = 500
cantidad_a_retirar = 100

# Le preguntamos a Python: "Si el saldo es mayor o igual a lo que quiero retirar, entonces..."
if saldo_bancario >= cantidad_a_retirar:
    # Como la condición es True (500 >= 100), Python entrará aquí (nota los espacios a la izquierda)
    saldo_bancario = saldo_bancario - cantidad_a_retirar
    print(f"Retiro exitoso. Te quedan ${saldo_bancario}")

# Esta línea ya no tiene sangría. Se ejecuta SIEMPRE, sin importar lo que pasó arriba.
print("Gracias por usar el banco.")


print("\n--- 2. La Promoción Secreta ---")

# Un sistema que da un regalo si el usuario sabe la clave secreta
palabra_ingresada = "python_es_genial"

if palabra_ingresada == "python_es_genial":
    # Entramos a la habitación secreta del 'if'
    print("¡Acceso concedido!")
    print("Acabas de ganar un cupón de 50% de descuento.")

# Si la palabra_ingresada fuera diferente (ej. "hola"), las dos líneas de arriba 
# serían invisibles para Python, saltaría directamente aquí:
print("Fin del programa de promociones.")
