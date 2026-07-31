import asyncio
import time

async def hacer_hamburguesa(numero):
    print(f"[{numero}] Empezando hamburguesa...")
    # Simulamos que toma 2 segundos cocinarla
    await asyncio.sleep(2)
    print(f"[{numero}] ¡Hamburguesa lista!")

async def cocina():
    print("--- Pedido Grande ---")
    print("¡El cliente pidió 3 hamburguesas!")
    
    # Anotamos la hora exacta en la que empezamos
    inicio = time.time()
    
    # Magia simultánea: Lanzamos las 3 a la vez.
    # El 'await' espera a que las 3 terminen para continuar.
    await asyncio.gather(
        hacer_hamburguesa(1),
        hacer_hamburguesa(2),
        hacer_hamburguesa(3)
    )
    
    # Calculamos cuánto tardó en total
    fin = time.time()
    tiempo_total = round(fin - inicio, 2)
    
    print("--- Pedido Entregado ---")
    print(f"Tiempo total: {tiempo_total} segundos.")
    print("Si las hiciéramos una por una, ¡hubieran sido 6 segundos!")

asyncio.run(cocina())
