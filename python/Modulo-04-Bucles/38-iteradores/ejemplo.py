# ==========================================
# Archivo: ejemplo.py
# Autor: Kaia / Alenia Studios
# Descripción: Comprendiendo los iteradores manuales
# ==========================================

print("--- Clínica Médica ---")

# Tenemos la lista de pacientes esperando en la sala.
pacientes = ["Paciente 1: Carlos", "Paciente 2: María", "Paciente 3: Luis"]

print("Hay 3 pacientes en la sala de espera.")
print("Transformando la lista en un dispensador de turnos...")

# Transformamos la lista en un iterador usando iter().
turnos = iter(pacientes)

print("--- Consultorio Abierto ---")

# El doctor presiona el botón para llamar al primer paciente.
# Usamos next() para jalar el primer elemento.
print("El doctor llama al:")
print(next(turnos))

print("... (El doctor atiende a Carlos) ...")

# El doctor presiona el botón de nuevo.
# ¡Nota que usamos EXACTAMENTE el mismo código, pero nos dará a María!
print("El doctor llama al:")
print(next(turnos))

print("... (El doctor atiende a María) ...")

# Aún queda un paciente, pero el doctor decide ir a comer.
print("El doctor se va a almorzar, Luis tendrá que esperar.")
print("--- Consultorio Pausado ---")
