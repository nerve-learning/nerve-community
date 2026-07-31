# Nivel 115: La Memoria del Sistema (Manejo de Estado) 🧠

Imagina que creas un bot en Nerve para una tienda. El bot recibe el mensaje: `"Vendí 2 camisas"`. El bot lo imprime en la pantalla y termina. Luego recibe: `"Vendí 3 camisas"`. Lo imprime y termina. 
Si el jefe te pregunta: *"¿Cuántas camisas hemos vendido en total hoy?"*, tu bot no sabrá qué responder, porque tiene "amnesia". Cada vez que recibe un mensaje, olvida lo que pasó en el mensaje anterior.

En la arquitectura de software, a esto le llamamos ser **"Stateless"** (Sin Estado). 
Pero los sistemas avanzados (como carritos de compras, videojuegos multijugador o sistemas de inventario) necesitan recordar. Necesitan **"State"** (Estado).

En este nivel aprenderás cómo darle memoria a tus nodos de Nerve para que puedan recordar información a lo largo del tiempo, sumando, restando o acumulando datos con cada mensaje que llega.

### Ruta de aprendizaje

1. **Teoría (`teoria.md`)**: El Pez Dorado vs El Elefante. Por qué las variables normales fallan y cómo usar un Diccionario como cerebro.
2. **Ejemplo (`ejemplo.py`)**: Construiremos un Bot de Almacén que lleva la cuenta de las manzanas.
3. **Reto (`reto.md`)**: Programarás un Tamagotchi de red que recuerda si tiene hambre.
