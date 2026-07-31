# ==========================================
# NIVEL 27: ESTRUCTURAS ANIDADAS - EJEMPLO
# ==========================================

print("--- 1. El archivero (Lista de Listas) ---")
# Cada cajón (elemento de la lista grande) es otra lista
archivero = [
    ["Factura 1", "Factura 2"],  # Cajón 0
    ["Contrato A", "Contrato B"] # Cajón 1
]

print("Todo el archivero:")
print(archivero)

print("Lo que hay en el Cajón 0:")
print(archivero[0])

print("Abriendo el Cajón 0 y sacando el primer documento [0][0]:")
documento = archivero[0][0]
print(documento)


print("\n--- 2. Base de datos (Lista de Diccionarios) ---")
# Una lista que guarda el perfil (diccionario) de varias mascotas
mascotas = [
    {"nombre": "Firulais", "tipo": "Perro"}, # Mascota 0
    {"nombre": "Mishi", "tipo": "Gato"}      # Mascota 1
]

print("Nuestra segunda mascota (índice 1) es:")
print(mascotas[1])

print("¿Y cómo se llama esa segunda mascota? [1]['nombre']")
nombre_mishi = mascotas[1]["nombre"]
print(nombre_mishi)


print("\n--- 3. Diccionarios dentro de Diccionarios ---")
# Un contacto que tiene su dirección guardada como otro diccionario
contacto = {
    "nombre": "Tony Stark",
    "direccion": {
        "ciudad": "Nueva York",
        "calle": "Torre Stark"
    }
}

print("¿En qué ciudad vive Tony?")
# Entramos a "direccion", que nos da un diccionario, y luego entramos a "ciudad"
ciudad_tony = contacto["direccion"]["ciudad"]
print(ciudad_tony)
