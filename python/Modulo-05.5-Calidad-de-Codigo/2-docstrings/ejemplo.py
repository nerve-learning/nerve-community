print("--- Parte 1: Una función muda (sin manual) ---")

def convertir_temperatura(valor: float) -> float:
    return (valor * 9/5) + 32

# Alguien que lea esto pensará: "¿Convierte de Celsius a Fahrenheit o al revés?"
# Tienen que leer la fórmula matemática para adivinar.
print(convertir_temperatura(0.0))  # 32.0


print("\n--- Parte 2: La misma función CON manual ---")

def convertir_celsius_a_fahrenheit(celsius: float) -> float:
    """
    Convierte grados Celsius a Fahrenheit.
    
    Toma la temperatura en Celsius, la multiplica por 9/5 y le suma 32.
    
    Args:
        celsius: La temperatura en grados Celsius.
        
    Returns:
        La temperatura equivalente en grados Fahrenheit.
    """
    return (celsius * 9/5) + 32

# ¡Ahora no hay dudas! El docstring explica exactamente qué pasa.
print(convertir_celsius_a_fahrenheit(0.0))  # 32.0


print("\n--- Parte 3: Docstrings mínimos de una sola línea ---")

def saludar(nombre: str) -> str:
    """Devuelve un saludo amigable con el nombre proporcionado."""
    return f"¡Hola, {nombre}!"

print(saludar("Kaia"))


print("\n--- Parte 4: Usando help() para leer el manual ---")

# La función integrada help() nos muestra el docstring en la terminal
print("Viendo la ayuda de convertir_celsius_a_fahrenheit:")
help(convertir_celsius_a_fahrenheit)
