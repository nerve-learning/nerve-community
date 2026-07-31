# Importamos nuestro robot y su brújula
from selenium import webdriver
from selenium.webdriver.common.by import By
# Importamos la herramienta para hacer pausas en el tiempo
import time

print("--- 1. Invocando al Robot Fantasma ---")
robot = webdriver.Chrome()
print("¡Observa tu barra de tareas, Chrome se acaba de abrir solo!")

print("\n--- 2. Navegando a la zona de pruebas ---")
robot.get("http://quotes.toscrape.com/login")
print("Viajando a la página de inicio de sesión...")
# Le decimos al robot que se duerma 2 segundos para asegurar que la página cargue
time.sleep(2) 

print("\n--- 3. Llenando el formulario ---")
# Buscamos la caja del usuario por su ID
caja_usuario = robot.find_element(By.ID, "username")
# Y escribimos en ella
caja_usuario.send_keys("EstudiantePython")
print("El robot ha escrito el nombre de usuario.")

# Pausa de 1 segundo para que tus ojos humanos puedan ver el texto
time.sleep(1)

# Buscamos la caja de contraseña por su ID
caja_password = robot.find_element(By.ID, "password")
caja_password.send_keys("contraseña_super_secreta")
print("El robot ha escrito la contraseña.")

# Otra pequeña pausa
time.sleep(1)

print("\n--- 4. Presionando el botón ---")
# Buscamos el botón de login. Si miras el código de esa página, 
# el botón tiene la clase "btn-primary".
boton_login = robot.find_element(By.CLASS_NAME, "btn-primary")

# ¡Hacemos el clic!
boton_login.click()
print("¡Clic realizado! Intentando entrar...")

# Hacemos una pausa larga de 4 segundos para que disfrutes viendo
# la página a la que acabas de entrar.
time.sleep(4)

print("\n--- 5. Apagando al Robot ---")
# Siempre, siempre debemos destruir al robot al terminar.
robot.quit()
print("Navegador fantasma cerrado. Misión cumplida.")
