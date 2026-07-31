import asyncio
import aiohttp
import time

# Nuestro mini-bot que extraerá datos de una sola página
async def extraer_datos(sesion, url, id_bot):
    print(f"--- Bot {id_bot} iniciando ---")
    print(f"[Bot {id_bot}] Visitando: {url}")
    
    try:
        # Tocamos la puerta del servidor
        async with sesion.get(url) as respuesta:
            respuesta.raise_for_status() # Verificamos que no haya error 404/500
            
            # Descargamos el contenido en formato texto
            html = await respuesta.text()
            
            # Solo sacamos los primeros 50 caracteres para no saturar la pantalla
            fragmento = html[:50].replace('\n', '') 
            print(f"[Bot {id_bot}] ÉXITO. Fragmento: '{fragmento}...'")
            print(f"--- Bot {id_bot} terminó ---\n")
            
            return f"Bot {id_bot} obtuvo datos."
            
    except Exception as e:
        print(f"[Bot {id_bot}] FALLÓ. Error: {e}")
        print(f"--- Bot {id_bot} terminó ---\n")
        return f"Bot {id_bot} falló."

# El director de la orquesta
async def orquestador():
    print("=== Iniciando Scraper Concurrente ===\n")
    
    # Vamos a extraer de 3 sitios al mismo tiempo
    urls = [
        "https://www.example.com",
        "https://www.python.org",
        "https://url-que-no-existe-999.com" # Este bot va a fallar
    ]
    
    inicio = time.time()
    
    # Creamos la sesión principal
    async with aiohttp.ClientSession() as sesion:
        # Preparamos las misiones para nuestros bots
        misiones = []
        for i in range(len(urls)):
            # Sacamos la url correspondiente
            url_actual = urls[i]
            # Creamos la tarea pero AÚN no la ejecutamos
            mision = extraer_datos(sesion, url_actual, id_bot=i+1)
            misiones.append(mision)
        
        print("¡Lanzando todos los bots al mismo tiempo!\n")
        
        # gather lanza la lista de misiones al mismo tiempo
        # El * desempaqueta la lista para dársela a gather
        resultados = await asyncio.gather(*misiones)
        
    fin = time.time()
    
    print("=== Resumen Final ===")
    print(f"Tiempo total: {round(fin - inicio, 2)} segundos.")
    print("Resultados de cada bot:", resultados)

# Encendemos la maquinaria
asyncio.run(orquestador())
