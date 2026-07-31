import requests
import time

print("--- 1. Preparando al Guardia Nocturno ---")
print("⚠️ Para detener a este guardia, haz clic en esta terminal y presiona Ctrl+C")
print("Comenzando rondas de vigilancia en 3 segundos...")
time.sleep(3)

url_vigilada = "https://httpbin.org/get"
numero_de_ronda = 1

# PIEZA 1: El Motor Eterno
# Este bucle se repetirá hasta el fin de los tiempos (o hasta que lo apagues)
while True:
    print(f"\n--- Iniciando Ronda #{numero_de_ronda} ---")
    
    # PIEZA 2: Los Ojos
    # El guardia va a revisar la puerta (la URL)
    respuesta = requests.get(url_vigilada)
    
    # PIEZA 3: El Cerebro
    # El guardia decide si hay que encender las alarmas
    if respuesta.status_code == 200:
        print("✅ Todo en orden. El servidor está despierto y sano.")
    else:
        print(f"🚨 ¡ALERTA! Algo anda mal. El servidor devolvió el código: {respuesta.status_code}")
    
    # PIEZA 4: El Freno
    # ¡VITAL! Sin esto, lanzaríamos un ataque contra el servidor.
    print("😴 El guardia descansa 2 segundos antes de su próxima ronda...")
    time.sleep(2)
    
    # Aumentamos el contador de la ronda para saber cuántas veces hemos vigilado
    numero_de_ronda = numero_de_ronda + 1
