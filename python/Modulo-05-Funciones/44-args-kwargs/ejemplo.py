print("--- 1. Llamar por Nombre (Saltarse el orden) ---")

def crear_servidor(nombre, memoria="2GB", disco="50GB", estado="Apagado"):
    print("Servidor:", nombre)
    print("RAM:", memoria, "| Disco:", disco, "| Estado:", estado)
    print("-" * 20)

# Solo damos el nombre, el resto usa el Plan B
crear_servidor("Web_Principal")

# Queremos cambiar el estado a "Encendido", pero no queremos cambiar RAM ni Disco.
# Solución: Lo llamamos por su etiqueta directamente.
crear_servidor("Base_De_Datos", estado="Encendido")


print("\n--- 2. Empaquetando Infinitos con *args ---")

# El '*' convierte 'nombres' en una tupla con todos los valores extra
def pasar_lista(profesor, *nombres):
    print("Profesor a cargo:", profesor)
    print("Alumnos presentes:")
    
    # Recorremos la caja mágica 'nombres' (que es una tupla)
    for alumno in nombres:
        print("-", alumno)

# "Snape" se guarda en 'profesor'.
# Todo el resto se va directo a la bolsa '*nombres'.
pasar_lista("Snape", "Draco", "Crabbe", "Goyle", "Pansy")


print("\n--- 3. Empaquetando Etiquetas con **kwargs ---")

# El '**' convierte 'detalles' en un diccionario
def imprimir_ficha_tecnica(producto, **detalles):
    print("FICHA DE:", producto)
    
    # Recorremos el diccionario 'detalles'
    for etiqueta in detalles:
        # Imprimimos la llave (etiqueta) y su valor
        print(etiqueta, ":", detalles[etiqueta])

# "Laptop X" se guarda en 'producto'.
# El resto trae etiquetas, así que Python las empaca en el diccionario '**detalles'.
imprimir_ficha_tecnica("Laptop X", procesador="Core i9", ram="32GB", color="Negro")


print("\n--- 4. ¡Todo junto! ---")

# Primero los normales, luego el *, luego el **
def operacion_compleja(mision, *agentes, **equipamiento):
    print("Misión:", mision)
    print("Agentes asignados:", agentes) # Esto imprimirá una tupla ()
    print("Equipamiento:", equipamiento) # Esto imprimirá un diccionario {}

# Fíjate cómo Python sabe exactamente a dónde mandar cada cosa:
# "Infiltración" -> mision
# "007", "008" -> *agentes (porque no tienen etiqueta)
# coche="Aston Martin", arma="Walther" -> **equipamiento (porque sí tienen etiqueta)
operacion_compleja("Infiltración", "007", "008", coche="Aston Martin", arma="Walther")
