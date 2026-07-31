import asyncio
# Si esto te da error de que no existe, abre tu terminal y ejecuta: pip install aiohttp
import aiohttp 

async def consultar_pokemon(nombre):
    print(f"--- Buscando a {nombre} ---")
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"
    
    # 1. Abrimos la sesión asíncrona (el canal de comunicación)
    async with aiohttp.ClientSession() as sesion:
        
        # 2. Hacemos la petición GET (esperamos sin bloquear el programa)
        async with sesion.get(url) as respuesta:
            
            # 3. Esperamos a que se descargue el JSON
            # Nota: aiohttp tiene .json() igual que requests, pero requiere await
            datos = await respuesta.json()
            
            peso = datos["weight"]
            print(f"> ¡Encontrado! {nombre.capitalize()} pesa {peso} hectogramos.")

async def main():
    print("Iniciando búsqueda en la Pokedex...\n")
    
    # Lanzamos dos peticiones a internet ¡AL MISMO TIEMPO!
    # Mientras esperamos a ditto, también pedimos a pikachu.
    await asyncio.gather(
        consultar_pokemon("ditto"),
        consultar_pokemon("pikachu")
    )
    
    print("\nBúsqueda finalizada.")

asyncio.run(main())
