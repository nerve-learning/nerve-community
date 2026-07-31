print("--- 1. Función con Parámetros (Ingredientes) ---")

# 'fruta' y 'liquido' son parámetros. Son etiquetas vacías.
def preparar_batido(fruta, liquido):
    # Usamos las etiquetas dentro de la función
    print("Licuando " + fruta + " con " + liquido + "...")
    print("¡Batido terminado! 🥤")

# Ahora llamamos a la función y le pasamos los datos reales (Argumentos)
preparar_batido("Fresa", "Leche")
preparar_batido("Plátano", "Agua")
# Fíjate cómo la misma función hace cosas distintas gracias a los parámetros.


print("\n--- 2. Función con Return (Entregando resultados) ---")

# Esta función calcula el precio con impuesto, pero NO lo imprime.
# Solo hace el cálculo matemático y TE LO DEVUELVE.
def calcular_precio_final(precio_producto, impuesto):
    aumento = precio_producto * (impuesto / 100)
    total = precio_producto + aumento
    
    # Aquí escupimos el valor hacia afuera.
    # ¡La función termina inmediatamente en esta línea!
    return total

# Como la función escupe un valor, necesitamos una variable ('billetera') para atraparlo.
# Llamamos a la función con 100 de precio y 15 de impuesto.
precio_zapatos = calcular_precio_final(100, 15)
precio_camisa = calcular_precio_final(50, 10)

print("El precio a pagar por los zapatos es:", precio_zapatos)
print("El precio a pagar por la camisa es:", precio_camisa)

# Podemos incluso usar el resultado directamente en otras operaciones
total_compra = precio_zapatos + precio_camisa
print("En total vas a pagar:", total_compra)


print("\n--- 3. El error de usar print en vez de return ---")

def funcion_tramposa(numero):
    print("Procesando el número:", numero)
    # ¡Ups! Olvidé poner 'return'

# Intento atrapar el valor...
resultado_tramposo = funcion_tramposa(99)

# Mira lo que pasa si trato de ver qué atrapé
print("El valor atrapado es:", resultado_tramposo)
# Verás que dice 'None', porque la función no me entregó nada físico.
