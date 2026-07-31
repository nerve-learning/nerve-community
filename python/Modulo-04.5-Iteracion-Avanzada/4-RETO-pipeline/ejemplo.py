print("=== La Línea de Ensamble: Cómo se Encadenan los Generadores ===")
print()

# Imagina una fábrica de reseñas de productos
# El texto crudo llega así:
resenas_brutas = [
    "  MUY BUENO el producto llego rapido  ",
    "  MALO: se rompio a los 2 dias  ",
    "  EXCELENTE recomendado 100 por ciento  ",
    "  MALO no sirve devolucion urgente  ",
    "  BUENO precio accesible  ",
    "  MALO calidad pesima jamas compro aqui  ",
]


print("--- Etapa 1: Limpiador (quita espacios y pasa a minúsculas) ---")

# Generador 1: limpia cada reseña
def limpiar(resenas):
    for r in resenas:
        yield r.strip().lower()   # strip() quita espacios, lower() pone en minúsculas

# Probamos la primera etapa sola
for limpia in limpiar(resenas_brutas):
    print(f"  '{limpia}'")


print()
print("--- Etapa 2: Filtro (solo las reseñas MALAS) ---")

# Generador 2: recibe el resultado de limpiar y filtra
def filtrar_malas(resenas_limpias):
    for r in resenas_limpias:
        if "malo" in r:           # "malo" en minúsculas porque ya limpiamos
            yield r

# Encadenamos: limpiar → filtrar_malas
# filtrar_malas recibe el GENERADOR de limpiar, no una lista
pipeline_parcial = filtrar_malas(limpiar(resenas_brutas))

for mala in pipeline_parcial:
    print(f"  ⚠ {mala}")


print()
print("--- Etapa 3: Formateador (agrega el emoji de alerta) ---")

# Generador 3: toma las malas y las formatea para el reporte
def formatear_alerta(resenas_malas):
    contador = 1
    for r in resenas_malas:
        yield f"🚨 ALERTA #{contador}: {r.upper()}"  # .upper() pone todo en MAYÚSCULAS
        contador = contador + 1

# El pipeline completo: limpiar → filtrar_malas → formatear_alerta
# Ninguna etapa crea una lista. Los datos fluyen de una a otra de uno en uno.
pipeline_completo = formatear_alerta(filtrar_malas(limpiar(resenas_brutas)))

print()
print("=== Reporte Final de Reseñas Negativas ===")
print()
for alerta in pipeline_completo:
    print(alerta)


print()
print("--- Bonus: con expresión generadora para el formateador ---")

# La tercera etapa también puede ser una expresión generadora en vez de def
resenas_limpias = limpiar(resenas_brutas)
solo_malas      = filtrar_malas(resenas_limpias)
alertas         = (f"🚨 {r.upper()}" for r in solo_malas)

for a in alertas:
    print(a)
