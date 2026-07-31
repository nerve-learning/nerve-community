print("--- 1. Creando la Clase Padre (El Molde Base) ---")

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        
    # Esta acción será heredada por TODOS los hijos. ¡No hay que reescribirla!
    def dormir(self):
        print(f"Zzz... {self.nombre} está durmiendo profundamente.")
        
    # Una acción genérica que los hijos "aplastarán" para hacerla suya.
    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido misterioso.")


print("--- 2. Creando Clases Hijas (Herencia) ---")

# Al poner (Animal), el Perro absorbe el __init__, dormir() y hacer_sonido()
class Perro(Animal):
    
    # POLIMORFISMO: Reescribimos (aplastamos) hacer_sonido()
    def hacer_sonido(self):
        print(f"¡Guau, guau! Soy {self.nombre} el perro.")

# El Gato también hereda de Animal
class Gato(Animal):
    
    # POLIMORFISMO: El gato hace su propio sonido
    def hacer_sonido(self):
        print(f"¡Miau! Soy {self.nombre} el gato.")


print("--- 3. Probando a nuestros animales ---")

# Al crear los objetos, usamos el __init__ heredado del Padre que nos pide un 'nombre'
mi_perro = Perro("Toby")
mi_gato = Gato("Pelusa")
animal_raro = Animal("Cosa Genérica")

# 1. Probamos la Herencia (todos comparten el mismo método dormir)
mi_perro.dormir()
mi_gato.dormir()

# 2. Probamos el Polimorfismo (misma función, distintos resultados)
animal_raro.hacer_sonido()
mi_perro.hacer_sonido()
mi_gato.hacer_sonido()
