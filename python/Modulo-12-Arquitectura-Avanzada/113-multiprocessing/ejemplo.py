import multiprocessing
import time

# --- Título de la sección ---
print("--- 1. DEFINIENDO LOS TRABAJOS PESADOS ---")

def minar_oro():
    print("⛏️  Clon Minero: Empezando a picar piedra...")
    # time.sleep simula que la computadora está pensando o trabajando duro
    time.sleep(3) 
    print("💰 Clon Minero: ¡Encontré 100 monedas de oro!")

def talar_madera():
    print("🪓 Clon Leñador: Empezando a cortar árboles...")
    time.sleep(3)
    print("🪵  Clon Leñador: ¡Conseguí 50 troncos de madera!")

# --- Título de la sección ---
print("--- 2. EL ESCUDO ANTI-REBELIÓN ---")
# Sin esta línea, los clones se clonarían a sí mismos infinitamente.
if __name__ == '__main__':
    print("👨‍💼 Jefe (Cuerpo original): ¡A trabajar, clones!")

    # --- Título de la sección ---
    print("--- 3. CREANDO A LOS CLONES ---")
    
    # Creamos los clones y les asignamos su misión (target)
    # Nota: No usamos paréntesis en las funciones.
    clon_1 = multiprocessing.Process(target=minar_oro)
    clon_2 = multiprocessing.Process(target=talar_madera)

    # Mediremos cuánto tiempo tarda todo
    inicio = time.time()

    # --- Título de la sección ---
    print("--- 4. DESPERTANDO A LOS CLONES ---")
    # Al hacer start(), los clones empiezan a correr SIMULTÁNEAMENTE.
    clon_1.start()
    clon_2.start()

    # El Jefe no hace nada de trabajo duro, solo espera.
    print("👨‍💼 Jefe: Yo me quedo tomando un café mientras ellos trabajan.")

    # --- Título de la sección ---
    print("--- 5. ESPERANDO A QUE TERMINEN ---")
    # join() le dice al Jefe: "no te vayas hasta que clon_1 termine".
    clon_1.join()
    # Luego espera a que clon_2 termine.
    clon_2.join()

    # Calculamos el tiempo total
    fin = time.time()
    tiempo_total = round(fin - inicio, 1)

    # ¡Magia! Aunque cada trabajo toma 3 segundos, el tiempo total será ~3 segundos,
    # porque lo hicieron al mismo tiempo. Si el Jefe lo hiciera solo, tomaría 6.
    print(f"🏁 Todo el trabajo terminado en {tiempo_total} segundos.")
