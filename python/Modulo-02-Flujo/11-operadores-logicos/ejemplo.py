# ejemplo.py

print("--- El cine para adultos ---")

# Vamos a evaluar si una persona puede entrar a ver una película de terror.
# Necesita dos cosas: tener 18 años o más, Y traer su boleto físico.

edad = 19
tiene_boleto = True

# Guardamos en una variable el resultado de evaluar a nuestro guardia estricto (and).
# Python lee la izquierda: "edad >= 18" (que es True). 
# Luego lee la derecha: "tiene_boleto" (que es True).
# Como es True and True... el resultado final que se guarda es True.
puede_pasar = edad >= 18 and tiene_boleto

print(f"¿La persona puede entrar al cine?: {puede_pasar}")


print("--- Promoción de palomitas gratis ---")

# Hoy hay promoción. Para ganar palomitas necesitas llevar camisa roja O decir la palabra secreta.

color_camisa = "verde"
sabe_palabra_secreta = True

# Usamos a nuestro guardia relajado (or).
# Python lee la izquierda: "color_camisa == 'roja'" (False, porque es verde).
# Luego lee la derecha: "sabe_palabra_secreta" (True).
# Como el 'or' solo necesita un True para ser feliz, el resultado final es True.
gana_palomitas = color_camisa == "roja" or sabe_palabra_secreta

print(f"¿Gana palomitas gratis?: {gana_palomitas}")


print("--- El letrero de la tienda ---")

# Usaremos 'not' para llevar la contraria a un estado.
tienda_abierta = True

# Si la tienda está abierta (True), queremos saber el estado de "cerrado".
# Usamos 'not' para voltear la verdad. Si es True, lo convierte a False.
esta_cerrada = not tienda_abierta

print(f"¿La tienda está cerrada ahora mismo?: {esta_cerrada}")
