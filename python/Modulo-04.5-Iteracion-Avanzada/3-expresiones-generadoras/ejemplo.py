print("--- Parte 1: [corchetes] vs (paréntesis) ---")

numeros = [1, 2, 3, 4, 5]

# Con corchetes: list comprehension — crea toda la lista inmediatamente
lista_dobles = [n * 2 for n in numeros]
print("Lista (todo guardado):", lista_dobles)         # [2, 4, 6, 8, 10]
print("Tipo:", type(lista_dobles))                    # <class 'list'>

# Con paréntesis: expresión generadora — crea el grifo, no los valores
gen_dobles = (n * 2 for n in numeros)
print("Generador (solo la receta):", gen_dobles)      # <generator object ...>
print("Tipo:", type(gen_dobles))                      # <class 'generator'>


print("--- Parte 2: los dos producen lo mismo al recorrerlos ---")

# Convertimos el generador a lista para verlo completo (gasta memoria al hacer esto)
print("Valores del generador:", list(gen_dobles))     # [2, 4, 6, 8, 10]


print("--- Parte 3: expresión generadora con filtro ---")

edades = [15, 23, 17, 31, 14, 28, 19]

# Solo queremos los adultos — el 'if' al final filtra
adultos = (edad for edad in edades if edad >= 18)

print("Edades de adultos:")
for a in adultos:
    print(f"  {a} años")


print("--- Parte 4: dentro de sum(), max(), min() ---")

ventas_semana = [1500, 2300, 980, 3100, 2750]

# sum() con expresión generadora — sin crear lista intermedia
total = sum(venta for venta in ventas_semana)
print(f"Total de ventas: {total}")

# max() filtrando — la venta más alta que supere 2000
# primero filtramos con el if, luego max encuentra el mayor de esos
ventas_altas = [v for v in ventas_semana if v > 2000]   # guardamos primero para poder usar max
mejor_dia = max(ventas_altas)
print(f"Mejor día (más de 2000): {mejor_dia}")

# Forma directa: sum de los que superan 2000
total_dias_buenos = sum(venta for venta in ventas_semana if venta > 2000)
print(f"Total solo días buenos (>2000): {total_dias_buenos}")


print("--- Parte 5: expresiones generadoras con strings ---")

nombres = ["  ana  ", "BOB ", " Clara", "  DAVID"]

# Limpiar y poner en formato título — sin crear lista intermedia
for nombre_limpio in (n.strip().title() for n in nombres):
    print(f"  Bienvenido/a, {nombre_limpio}")
# .strip() quita espacios al inicio y al final
# .title() pone la primera letra en mayúscula
