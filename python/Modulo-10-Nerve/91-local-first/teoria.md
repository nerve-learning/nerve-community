# Teoría: La Magia del Local-First y Nerve

Imagina que estás en un edificio de oficinas gigante (tu computadora). 
- **Módulo 07 (Web APIs):** Mandabas un correo físico a una sucursal en otro país para hacerle una pregunta al chico de contabilidad que está en el piso de arriba. Toma mucho tiempo.
- **Nerve (Local-First):** Instalas un sistema de **tubos neumáticos** (como en los supermercados o bancos). Metes un papel en una cápsula, la pones en el tubo, ¡y llega al piso de arriba en un parpadeo!

Nerve es ese sistema de tubos. Conecta todos tus programas en Python (¡y de otros lenguajes!) usando "Sockets Locales". No requiere internet, no abre puertos al exterior, todo es privado y rápido.

---

## Anatomía de un Nodo Nerve

Para usar nuestro sistema de tubos, necesitamos un "radio-transmisor" o "nodo". El código para crearlo es súper directo:

```python
from nerve import NexusClient
```
* **Qué hace:** Trae los planos de la fábrica de Nerve para poder construir nuestra propia antena (`NexusClient`).

```python
cliente = NexusClient()
```
* **Qué hace:** Construimos la antena (un objeto) y la guardamos en la caja llamada `cliente`.

```python
cliente.connect("mi_programa")
```
* **Qué hace:** Enchufamos la antena a la pared y le ponemos un gafete con nuestro nombre (`"mi_programa"`). ¡Ahora la red sabe que existimos!

```python
paquete = {"temperatura": 25}
cliente.send("termostato", paquete)
```
* **Qué hace:** Metemos un diccionario (`paquete`) en la cápsula del tubo neumático y le decimos a Nerve: *"Por favor, manda esto directamente a quien se llame 'termostato'"*. 

```python
cliente.broadcast({"alerta": "terremoto"})
```
* **Qué hace:** Usamos el **megáfono** de la red. En lugar de mandarlo a una persona específica, se lo gritamos a TODOS los programas que estén conectados al tubo neumático en ese momento.

---

## ¿Qué pasa si me equivoco?

El error más común al empezar con Nerve es intentar conectar un cliente cuando el "Hub Central" (el motor del tubo neumático) está apagado.

**Si ejecutas tu código y ves un error enorme rojo como este:**
`ConnectionRefusedError: [Errno 111] Connection refused` o `NerveHub Not Reachable`

**¿Qué significa?**
Tu programa intentó enchufar la antena, pero no había electricidad en la pared.

**¿Cómo lo soluciono?**
Antes de correr tu código de Python, siempre debes abrir OTRA terminal y escribir el comando mágico:
`nerve start`
Esto enciende el motor central que permite que los tubos neumáticos funcionen. ¡Déjalo corriendo ahí y ejecuta tu código en otra ventana!
