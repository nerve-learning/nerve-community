print("--- 1. Preparando la Corona (La Clase Singleton) ---")

class Rey:
    # Esta es la memoria de la fábrica. Aquí guardaremos al único Rey.
    _instancia_secreta = None

    # Secuestramos el momento del nacimiento
    def __new__(cls):
        # Verificamos si la corona está vacía
        if cls._instancia_secreta is None:
            print("👑 ¡Ha nacido un nuevo Rey! (Creando el objeto en memoria...)")
            # Le decimos a Python que fabrique al objeto real y lo guardamos
            cls._instancia_secreta = super().__new__(cls)
        else:
            print("🛑 ¡Alto ahí! Ya existe un Rey. Te daré el que ya existe.")
            
        # Siempre, SIEMPRE devolvemos al mismo Rey
        return cls._instancia_secreta

    # El init se ejecutará después de cada "nacimiento" (incluso los falsos)
    def __init__(self):
        # Para no sobreescribir el nombre cada vez, revisamos si ya tiene uno
        # hasattr pregunta: "¿Este objeto tiene el atributo 'nombre'?"
        if not hasattr(self, 'nombre'):
            self.nombre = "Arturo"
            print("   -> El Rey ha sido bautizado como", self.nombre)


print("\n--- 2. Coronando al primer Rey ---")
rey_norte = Rey()
print("El rey del norte se llama:", rey_norte.nombre)


print("\n--- 3. Intentando coronar a un Impostor ---")
# Intentamos crear otro objeto Rey
rey_sur = Rey()

# Vamos a cambiarle el nombre al rey del sur a ver qué pasa
rey_sur.nombre = "Impostor Malvado"

print("\n--- 4. La Verdad Sale a la Luz ---")
print("Nombre del rey_sur:", rey_sur.nombre)
print("Nombre del rey_norte:", rey_norte.nombre) # ¡Cambió también!

# El truco final: comprobamos si son literalmente la misma entidad en memoria
# El operador 'is' revisa si son el mismo clon físico, no solo si son iguales.
if rey_norte is rey_sur:
    print("\n😱 ¡MAGIA! El rey_norte y el rey_sur son EXACTAMENTE EL MISMO OBJETO.")
else:
    print("Son personas distintas.")
