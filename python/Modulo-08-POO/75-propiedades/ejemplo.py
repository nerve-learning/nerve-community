print("--- 1. Fabricando el Termostato Inteligente ---")

class Termostato:
    def __init__(self):
        # Escondemos la temperatura real. Nadie puede tocarla sin pasar por el guardia.
        self.__temperatura_real = 20
        
    # SOMBRERO LECTOR (@property)
    # Disfraza esta función para que desde afuera se vea como una variable normal.
    @property
    def temperatura(self):
        return self.__temperatura_real
        
    # SOMBRERO GUARDADOR (@nombre.setter)
    # Permite usar el signo '=' desde afuera, pero ejecutando este código primero.
    @temperatura.setter
    def temperatura(self, nuevo_valor):
        # Aquí está la magia: validamos antes de permitir el cambio
        if nuevo_valor < -10 or nuevo_valor > 50:
            print(f"❌ ¡ALERTA! {nuevo_valor}°C es extremo. La casa podría incendiarse o congelarse.")
        else:
            # Si pasa la validación, modificamos la variable privada
            self.__temperatura_real = nuevo_valor
            print(f"✅ Temperatura ajustada correctamente a {self.__temperatura_real}°C")


print("--- 2. Usando las propiedades (La Magia) ---")

mi_casa = Termostato()

# LEER: Usamos 'mi_casa.temperatura' ¡sin paréntesis!
print(f"La temperatura actual es: {mi_casa.temperatura}°C")

# ESCRIBIR (CASO BUENO): 
# Usamos el signo '='. Esto despierta al @temperatura.setter de forma invisible.
mi_casa.temperatura = 25 

# ESCRIBIR (CASO PELIGROSO):
# Intentamos poner un valor absurdo. El setter interceptará esto y nos bloqueará.
mi_casa.temperatura = 1000 

print("--- 3. Comprobando el resultado final ---")
# Volvemos a leer. Verificaremos que el 1000 nunca logró entrar a la variable privada.
print(f"La temperatura segura sigue siendo: {mi_casa.temperatura}°C")
