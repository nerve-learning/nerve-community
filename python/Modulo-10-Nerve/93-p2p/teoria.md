# Teoría: El Walkie-Talkie Bidireccional

Imagina que tienes un Walkie-Talkie moderno. Tiene un altavoz (por donde sale la voz de tu amigo) y un botón de micrófono (para que tú hables).

Para que un nodo P2P funcione, necesitamos emular esto en código:
1. **El Altavoz:** Contratamos a un recepcionista (`cliente.listen()`) que trabaje de fondo 24/7.
2. **El Micrófono:** En el flujo principal de nuestro programa, hacemos un ciclo infinito (`while True`) que nos pregunte constantemente qué queremos decir usando `input()`, y luego envíe ese mensaje con `cliente.send()`.

Como la red de Nerve funciona en segundo plano, el recepcionista no bloquea al micrófono, y el micrófono no bloquea al recepcionista. ¡Ambos pueden existir al mismo tiempo!

## Anatomía P2P

```python
# 1. EL ALTAVOZ (Recepcionista)
def escuchar_mensaje(datos):
    print("\n[Amigo]:", datos["texto"])

# Contratamos al recepcionista (¡SOLO UNA VEZ!)
cliente.listen(escuchar_mensaje)

# 2. EL MICRÓFONO (El bucle infinito)
while True:
    lo_que_escribi = input("Yo: ")
    cliente.send("amigo", {"texto": lo_que_escribi})
```
* **Qué hace:** 
  - El recepcionista (`escuchar_mensaje`) es llamado mágicamente por Nerve cada vez que llega algo por el tubo neumático. 
  - El `while True` (Módulo 04) es un bucle que nunca termina. Constantemente detiene el programa en el `input()`, esperando que escribas algo y presiones ENTER. Cuando lo haces, lo mete en una caja (diccionario) y lo envía a `"amigo"`. ¡Y luego vuelve a empezar!

---

## ¿Qué pasa si me equivoco?

El error más destructivo al mezclar bucles infinitos con recepcionistas es meter el contrato dentro del bucle.

**MAL 🔴:**
```python
while True:
    cliente.listen(escuchar_mensaje)  # ¡NO HAGAS ESTO!
    texto = input("Escribe: ")
```
**¿Por qué está mal?**
Cada vez que el bucle da una vuelta, le estás diciendo a Nerve que contrate a un recepcionista NUEVO. Al final, tendrás miles de recepcionistas amontonados en tu computadora. Cuando llegue un solo mensaje, ¡todos los miles de recepcionistas intentarán gritar al mismo tiempo! 

**La Regla de Oro P2P:**
El recepcionista (`listen`) siempre se contrata **FUERA** y **ANTES** del bucle infinito. Solo necesitas uno.
