# Reto 117: El Restaurante Seguro 🍔

En los restaurantes, cuando el mesero toma una orden, la pasa a la cocina. Pero el mesero necesita saber cuándo está lista para llevársela al cliente. Si la orden se pierde, el cliente se enojará.

Vas a construir un sistema de comandas robusto donde el Mesero anota la orden, se la envía a la Cocina, y la Cocina le envía un Acuse de Recibido (ACK) cuando termina de cocinar.

### 📝 Instrucciones:

1. Crea un archivo Python. Importa `NexusHub`, `NexusClient` y `time`. Inicia el Hub.
2. Crea dos clientes: `"mesero"` y `"cocina"`.
3. Crea un diccionario global llamado `ordenes_pendientes = {}`.
4. **La Cocina:** Crea la función que escuchará la cocina. 
   - Debe usar `try / except` para protegerse de mensajes sin los datos correctos.
   - Debe extraer el `id_orden` y el `platillo`.
   - Debe imprimir que está cocinando el platillo.
   - Al terminar, debe usar `.send()` hacia `"mesero"` con un payload de ACK que incluya el `id_orden` y un `"status": "LISTO"`.
5. **El Mesero:** Crea la función que escuchará el mesero.
   - Si recibe un ACK, debe buscar el `id_orden` en `ordenes_pendientes`.
   - Si existe, imprimir "Llevando platillo a la mesa" y borrarlo del diccionario usando `del`.
6. Pon a escuchar a ambos clientes.
7. **La Simulación:** 
   - El mesero anota la orden: `ordenes_pendientes[42] = "Hamburguesa con Papas"`.
   - El mesero envía la orden a la cocina: `{"id_orden": 42, "platillo": "Hamburguesa con Papas"}`.
8. Usa `time.sleep(3)` al final para dar tiempo a que ocurra toda la comunicación antes de desconectar y detener el hub.

### ⛔ Reglas Estrictas:
* **Permitido:** Diccionarios, `try/except`, sentencias `if`, `.send()`, `.listen()`, `del`.
* **Prohibido:** Olvidar el `try/except` en la cocina. El sistema debe ser a prueba de balas.
* **Prohibido:** Que la cocina termine de cocinar y no envíe el ACK de regreso.

### 🎯 Resultado Esperado en la Terminal:
```text
📝 [MESERO] Orden 42 anotada. Enviando a cocina...
🍳 [COCINA] Preparando: Hamburguesa con Papas (Orden 42)...
🔔 [COCINA] ¡Orden 42 terminada! Avisando al mesero...
🏃 [MESERO] Recibí ACK. ¡Llevando Hamburguesa con Papas a la mesa! Órdenes pendientes: 0
```
*(Puedes adaptar los prints para que tu historia quede igual de genial)*
