from abc import ABC, abstractmethod

print("--- 1. El Singleton (Motor del Juego) ---")
class MotorJuego:
    _unico = None

    def __new__(cls):
        if cls._unico is None:
            cls._unico = super().__new__(cls)
            cls._unico.turno = 1
        return cls._unico
    
    def avanzar_turno(self):
        self.turno += 1
        print(f"\n--- ⏳ Comienza el turno {self.turno} ---")


print("\n--- 2. La Abstracción y Memoria Colectiva (Clase Padre) ---")
class Personaje(ABC):
    # Variable de clase para saber cuántos existen en total
    _poblacion_total = 0

    @classmethod
    def ver_poblacion(cls):
        return cls._poblacion_total

    def __init__(self, nombre, vida):
        self.nombre = nombre
        # Encapsulamiento: La vida es privada (__)
        self.__vida = vida 
        Personaje._poblacion_total += 1 # Sumamos a la población global

    # Propiedad (Cadenero) para leer la vida sin tocarla directamente
    @property
    def vida(self):
        return self.__vida

    # Contrato estricto: Todo hijo DEBE saber atacar
    @abstractmethod
    def atacar(self):
        pass
    
    # Método Dunder para que se vea bonito al hacerle print()
    def __str__(self):
        return f"[{self.nombre}] ❤️ {self.vida} HP"


print("\n--- 3. Herencia y Polimorfismo (Los Hijos) ---")
class Guerrero(Personaje):
    def atacar(self):
        print(f"⚔️ {self.nombre} da un hachazo tremendo!")

class Mago(Personaje):
    def atacar(self):
        print(f"🔥 {self.nombre} lanza una bola de fuego!")


print("\n--- 4. Dando vida al Ecosistema ---")
# Creamos el gestor del juego
juego = MotorJuego()

# Creamos nuestros héroes
arthas = Guerrero("Arthas", 100)
gandalf = Mago("Gandalf", 80)

# Verificamos la población usando el método de clase
print(f"Población mundial: {Personaje.ver_poblacion()} héroes registrados.")

# Hacemos que interactúen
juego.avanzar_turno() # Avanza al turno 2
print(arthas)         # Llama a __str__ mágicamente
arthas.atacar()       # Polimorfismo en acción

juego.avanzar_turno() # Avanza al turno 3
print(gandalf)
gandalf.atacar()

# Demostrando el Singleton:
juego_clon = MotorJuego()
print(f"\nTurno actual en el juego original: {juego.turno}")
print(f"Turno actual en la copia pirata: {juego_clon.turno}")
print("¡El Singleton funciona! Ambos son el mismo juego.")
