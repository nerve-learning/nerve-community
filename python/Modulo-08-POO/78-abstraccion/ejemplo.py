# Importamos las herramientas para crear fantasmas y contratos
from abc import ABC, abstractmethod

print("--- 1. Definiendo el Contrato (Clase Abstracta) ---")

# Esta es nuestra clase abstracta. Hereda de ABC para volverse un "fantasma".
class Electrodomestico(ABC):
    
    # El decorador obliga a todos los hijos a tener este método.
    @abstractmethod
    def encender(self):
        # Un electrodoméstico genérico no sabe cómo encenderse.
        # Así que usamos 'pass' para dejarlo en blanco.
        pass

print("El contrato del Electrodomestico ha sido creado.")
print("Regla: Todo hijo debe saber cómo 'encender'.")


print("\n--- 2. Creando a los Hijos Cumplidores ---")

# La Television hereda del fantasma Electrodomestico
class Television(Electrodomestico):
    
    # Cumplimos el contrato creando el método 'encender'
    def encender(self):
        print("📺 Pantalla brillando... Mostrando el canal 5.")

# La Licuadora también hereda
class Licuadora(Electrodomestico):
    
    # Cumplimos el contrato de nuevo
    def encender(self):
        print("🌪️ ¡Brrrrr! Licuando las frutas a máxima velocidad.")


print("\n--- 3. Usando nuestros objetos reales ---")

# Creamos nuestros objetos
mi_tele = Television()
mi_licuadora = Licuadora()

# Los usamos. Sabemos con seguridad que tienen el método 'encender'
# porque el contrato (la clase abstracta) los obligó a tenerlo.
mi_tele.encender()
mi_licuadora.encender()


print("\n--- 4. La Trampa del Fantasma ---")
# Si intentamos crear un Electrodomestico genérico, el programa explota.
# Descomenta la línea de abajo bajo tu propio riesgo para ver el error:

# aparato_misterioso = Electrodomestico()
print("👻 (No podemos crear un Electrodomestico genérico, Python nos detendría con un TypeError)")
