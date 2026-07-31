import asyncio

# Usamos 'async def' para decirle a Python que esta función puede pausarse
async def calentar_agua():
    print("--- Calentando Agua ---")
    print("1. Ponemos la tetera en el fuego.")
    
    # 'await' le dice al Event Loop: "Pausa esta función 3 segundos. 
    # Ve a hacer otras cosas y vuelve cuando el tiempo termine."
    await asyncio.sleep(3) 
    
    print("2. ¡El agua está hirviendo! (Piiiip)")
    print("--- Fin Calentar Agua ---\n")

async def preparar_cafe():
    print("--- Preparando Café ---")
    print("1. Sacamos la taza.")
    
    # Await hace que la ejecución de esta función se suspenda 1 segundo
    await asyncio.sleep(1) 
    
    print("2. Ponemos el café en la taza.")
    print("--- Fin Preparar Café ---\n")

async def rutina_mañanera():
    print("¡Buenos días! Empezamos la rutina.\n")
    
    # IMPORTANTE: Aquí todavía estamos haciendo las cosas UNA POR UNA (secuencial)
    # Primero esperamos el agua...
    await calentar_agua()
    
    # Luego esperamos el café...
    await preparar_cafe()
    
    print("¡Rutina terminada, a beber el café!")

# Encendemos el Event Loop con nuestra función principal
asyncio.run(rutina_mañanera())
