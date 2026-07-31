import requests

# httpbin.org es un servidor de pruebas gratuito.
# La ruta /bearer simula un club privado. SOLO te deja entrar
# si le envías una credencial (Token).
url_vip = "https://httpbin.org/bearer"


print("--- 1. Intentando entrar SIN pase VIP ---")
# Intentamos entrar como si fuera una API pública
respuesta_rechazada = requests.get(url_vip)

print(f"Código del cadenero: {respuesta_rechazada.status_code}")
if respuesta_rechazada.status_code == 401:
    print("❌ ¡Acceso Denegado! No tenemos pulsera VIP.")


print("\n--- 2. Preparando la Billetera (Headers) ---")
# Creamos un diccionario (nuestra billetera)
billetera = {
    # La llave es 'Authorization' (así lo exigen los servidores)
    # El valor es 'Bearer ' seguido de nuestra contraseña
    "Authorization": "Bearer contraseña_secreta_del_estudiante"
}
print("Billetera preparada con éxito.")


print("\n--- 3. Intentando entrar CON pase VIP ---")
# Hacemos la llamada, pero esta vez le entregamos la billetera
# usando la instrucción: headers=billetera
respuesta_aceptada = requests.get(url_vip, headers=billetera)

print(f"Código del cadenero: {respuesta_aceptada.status_code}")
if respuesta_aceptada.status_code == 200:
    print("✅ ¡Acceso Concedido! Las puertas se abren.")

    print("\n--- 4. Viendo lo que hay dentro ---")
    # Como entramos, el servidor nos devuelve un JSON con nuestros datos
    datos_secretos = respuesta_aceptada.json()
    
    # El servidor nos repite el token que usamos para demostrar que lo leyó
    token_leido = datos_secretos["token"]
    print(f"El servidor dice que nuestro token fue: {token_leido}")
