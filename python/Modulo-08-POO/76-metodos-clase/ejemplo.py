print("--- 1. Diseñando la Fábrica de Robots ---")

class FabricaRobots:
    # 1. VARIABLE DE CLASE (El letrero de la fábrica)
    # Vive fuera del __init__. Le pertenece a FabricaRobots.
    robots_creados = 0 
    
    def __init__(self, nombre):
        # Variable de instancia (pertenece al robot)
        self.nombre = nombre 
        
        # Cada vez que el __init__ se ejecuta (nace un robot), 
        # le sumamos 1 al letrero de la fábrica.
        FabricaRobots.robots_creados += 1
        print(f"🤖 {self.nombre} ensamblado y listo.")

    # 2. MÉTODO DE CLASE (El Gerente)
    # Usamos @classmethod y la palabra 'cls' (que representa a FabricaRobots)
    @classmethod
    def dar_reporte(cls):
        # Accedemos a la variable de la fábrica usando cls
        print(f"📊 REPORTE DE FÁBRICA: Se han producido {cls.robots_creados} robots.")


print("\n--- 2. Pidiendo un reporte antes de trabajar ---")

# ¡OJO! No hemos creado ningún robot todavía. 
# Pero podemos llamar al método de clase usando el nombre del molde.
FabricaRobots.dar_reporte()


print("\n--- 3. Ensamblando robots ---")

robot1 = FabricaRobots("R2-D2")
robot2 = FabricaRobots("C-3PO")
robot3 = FabricaRobots("Wall-E")


print("\n--- 4. Pidiendo un reporte al final del día ---")

# Volvemos a llamar a la fábrica. El letrero debió haber subido a 3.
FabricaRobots.dar_reporte()
