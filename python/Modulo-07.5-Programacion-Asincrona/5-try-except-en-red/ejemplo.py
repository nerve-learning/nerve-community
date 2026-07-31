import asyncio
import aiohttp

async def visitar_pagina(sesion, url):
    print(f"--- Intentando visitar {url} ---")
    
    # Envolvemos el código peligroso en un bloque try
    try:
        async with sesion.get(url) as respuesta:
            
            # Lanzar un error manual si el servidor responde con error (ej. 404)
            # raise_for_status() hace que la respuesta explote si no fue exitosa.
            respuesta.raise_for_status() 
            
            print(f"> ¡Éxito! {url} está viva.")
            return "Éxito"
            
    except aiohttp.ClientError as error_de_red:
        # Atrapamos errores específicos de aiohttp (como URLs que no existen)
        print(f"> [FALLO] No se pudo conectar a {url}. Causa: {error_de_red}")
        return "Fallo"
    except Exception as e:
        # Atrapamos cualquier otro error por si acaso
        print(f"> [FALLO] Error inesperado en {url}: {e}")
        return "Fallo"

async def main():
    urls = [
        "https://www.google.com", 
        "https://una-pagina-falsa-que-no-existe-123.com", # Esto va a fallar
        "https://www.python.org"
    ]
    
    print("Iniciando visitas...\n")
    
    async with aiohttp.ClientSession() as sesion:
        # Preparamos la lista de tareas
        tareas = []
        for url in urls:
            tareas.append(visitar_pagina(sesion, url))
        
        # Lanzamos todas juntas
        await asyncio.gather(*tareas)
        
    print("\nPrograma terminado. ¡Sobrevivimos al error!")

asyncio.run(main())
