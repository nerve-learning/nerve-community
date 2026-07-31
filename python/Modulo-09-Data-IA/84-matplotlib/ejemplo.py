# Traemos a nuestro pintor y lo apodamos "plt"
import matplotlib.pyplot as plt

print("--- 1. Preparando la información ---")
# Estas listas serán nuestros ejes. 
# Pueden ser listas normales, o arrays de Numpy, ¡o columnas de Pandas!
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
ventas_diarias = [10, 15, 7, 20, 25]

print("Información lista. Entregando datos al pintor...")


print("\n--- 2. Trazando la obra de arte ---")
# plt.plot toma la primera lista para la base (horizontal)
# y la segunda lista para la altura (vertical)
plt.plot(dias_semana, ventas_diarias)

print("El pintor ya dibujó en secreto.")
print("Si el programa terminara aquí, no verías absolutamente nada.")


print("\n--- 3. Revelando la gráfica ---")
print("¡Abre bien los ojos! Aparecerá una ventana nueva.")
print("(Nota: El programa se pausará hasta que cierres la ventana de la gráfica)")

# Esta es la orden final. Levanta el telón y muestra la ventana.
plt.show()

print("¡Terminamos! Cerraste la gráfica con éxito.")
