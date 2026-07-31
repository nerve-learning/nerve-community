# ejemplo.py

print("--- 1. El Detector de Gemelos (== y !=) ---")

# Vamos a comparar textos (strings). Las mayúsculas importan mucho.
contrasena_guardada = "Secreto123"
contrasena_ingresada = "secreto123" # Nota la 's' minúscula

# El detective '==' revisa si son exactamente idénticas letra por letra.
son_iguales = contrasena_guardada == contrasena_ingresada
print(f"¿Las contraseñas son idénticas?: {son_iguales}")

# El detective '!=' revisa si son diferentes. 
son_diferentes = contrasena_guardada != contrasena_ingresada
print(f"¿Hubo un error de escritura (son diferentes)?: {son_diferentes}")


print("\n--- 2. El Medidor de Altura (> y <) ---")

# Para subir al juego mecánico "El Tornado" debes medir más de 150 cm.
altura_visitante = 145

# El detective '>' verifica quién gana en tamaño.
puede_subir = altura_visitante > 150
print(f"Altura del visitante: {altura_visitante}cm. ¿Puede subir?: {puede_subir}")


print("\n--- 3. El Límite de Edad (>= y <=) ---")

# Para tener licencia de conducir debes tener 18 años o más.
edad_persona = 18

# Si usamos '>' puro, diría que 18 no es mayor que 18 (False).
# Por eso usamos '>=' (mayor O IGUAL).
tiene_edad_minima = edad_persona >= 18
print(f"Edad de la persona: {edad_persona}. ¿Alcanza la edad mínima?: {tiene_edad_minima}")

# El peso máximo del elevador es 300 kg.
peso_actual = 300
# El detective '<=' revisa que no nos pasemos del límite.
es_seguro_elevar = peso_actual <= 300
print(f"Peso actual: {peso_actual}kg. ¿Es seguro usar el elevador?: {es_seguro_elevar}")
