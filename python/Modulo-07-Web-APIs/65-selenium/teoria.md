# Teoría: El Titiritero del Navegador 🎭

Para usar Selenium, primero debemos importar al robot y también su "brújula" (una herramienta llamada `By` que le dice CÓMO buscar las cosas).
Además, usaremos la herramienta `time` (que viene incluida en Python) para decirle al robot que espere, porque los robots son tan rápidos que a veces intentan hacer clic antes de que la página termine de cargar.

### 1. Invocando al Robot
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

robot = webdriver.Chrome() # Abre una ventana real de Chrome
```

### 2. Navegando y Esperando
En lugar de `requests.get`, ahora es el robot quien viaja.
```python
robot.get("https://google.com")
time.sleep(2) # ¡Duerme 2 segundos para dar tiempo a que la página cargue!
```

### 3. Encontrando Cosas
En BeautifulSoup usábamos `.find()`. Nuestro robot usa `.find_element()`, pero le tenemos que decir con la brújula (`By`) si lo buscaremos por su `ID` o por su `CLASS_NAME`.
```python
boton = robot.find_element(By.ID, "id_del_boton")
```

### 4. Interactuando (¡La magia real!)
Al robot no solo le importa leer, ¡él puede tocar la página!
```python
boton.click() # Hace clic izquierdo
caja_texto.send_keys("Hola") # Escribe texto con el teclado fantasma
```

### 5. Destruyendo al Robot
Cuando terminas, es obligatorio apagar el robot. Si no lo haces, te quedarás con docenas de ventanas de Chrome abiertas consumiendo memoria.
```python
robot.quit()
```

---

## ¿Qué pasa si me equivoco? (El Panel de Errores)

**Error 1: `NoSuchElementException: Message: no such element`**
- **Por qué pasa:** El robot intentó buscar un elemento (como un botón) y no lo encontró. Casi SIEMPRE sucede porque el robot buscó demasiado rápido y la página aún no terminaba de cargar.
- **Solución:** Pon un `time.sleep(3)` justo antes de buscar el elemento para obligar al robot a tener paciencia.

**Error 2: ¡La ventana se abre y se cierra instantáneamente!**
- **Por qué pasa:** Las computadoras ejecutan el código en milisegundos. Llegó a `robot.quit()` antes de que pudieras parpadear.
- **Solución:** Pon un `time.sleep(5)` antes de `robot.quit()` si quieres tener tiempo de ver con tus propios ojos lo que hizo el robot antes de destruirse.
