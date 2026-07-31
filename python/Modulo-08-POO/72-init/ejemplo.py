print("--- 1. Definiendo la Guardería ---")

class MascotaVirtual:
    # Este método mágico se dispara automáticamente en el instante del nacimiento.
    # Pedimos nombre y especie al dueño.
    def __init__(self, nombre, especie):
        # 1. Guardamos los datos que nos enviaron desde afuera
        self.nombre = nombre
        self.especie = especie
        
        # 2. Definimos datos universales. 
        # Toda mascota nueva nace con 100 de energía y mucha hambre.
        # ¡No necesitamos pedir esto en los paréntesis!
        self.energia = 100
        self.hambrienta = True
        
        # Incluso podemos hacer que el __init__ imprima cosas automáticamente
        print(f"🌟 ¡Ha nacido un nuevo {self.especie} llamado {self.nombre}!")

    def alimentar(self):
        # Esta es una función normal. Solo se ejecuta cuando nosotros lo ordenemos.
        self.hambrienta = False
        self.energia = self.energia + 20
        print(f"🍎 {self.nombre} comió. ¡Ya no tiene hambre! Su energía subió a {self.energia}.")


print("--- 2. Adoptando Mascotas ---")

# ¡Presta atención! Aquí es donde Python ejecuta el __init__ mágicamente.
# Enviamos "Firulais" y "Perro". Python los mete en las variables del __init__.
mascota_uno = MascotaVirtual("Firulais", "Perro")

# Nace una segunda mascota. Su __init__ es totalmente independiente del primero.
mascota_dos = MascotaVirtual("Garfield", "Gato")


print("--- 3. Interactuando con el Estado ---")

# Vamos a espiar cómo nacieron (gracias a los valores por defecto del __init__)
print(f"¿{mascota_uno.nombre} tiene hambre? -> {mascota_uno.hambrienta}")

# Ejecutamos una acción para cambiar ese estado interno
mascota_uno.alimentar()

# Comprobamos que el estado de Firulais cambió, pero Garfield sigue hambriento
print(f"¿{mascota_uno.nombre} tiene hambre ahora? -> {mascota_uno.hambrienta}")
print(f"¿{mascota_dos.nombre} tiene hambre ahora? -> {mascota_dos.hambrienta}")
