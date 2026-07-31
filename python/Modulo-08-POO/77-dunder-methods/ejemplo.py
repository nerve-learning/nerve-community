print("--- 1. Definiendo un Libro SIN voz ---")

class LibroMudo:
    def __init__(self, titulo):
        self.titulo = titulo

libro_aburrido = LibroMudo("El principito")

# Si imprimimos este objeto, Python no sabrá cómo mostrarlo.
# Nos dará su dirección de memoria.
print("Mira qué feo se ve un objeto sin __str__:")
print(libro_aburrido) 


print("\n--- 2. Definiendo un Libro CON voz (__str__) ---")

class LibroMagico:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
    # Agregamos el método dunder __str__
    def __str__(self):
        # REGLA DE ORO: Siempre usamos 'return'
        return f"📖 '{self.titulo}', escrito por {self.autor}."

libro_genial = LibroMagico("Harry Potter", "J.K. Rowling")


print("\n--- 3. Probando la Magia ---")

# Ahora, al hacer un simple print, Python busca silenciosamente el __str__
# y muestra el texto hermoso que preparamos.
print("Mira qué hermoso se ve ahora:")
print(libro_genial)
