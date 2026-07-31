# Reto 118: La Ventanilla del Banco Lento 🏦

En este banco, el cajero es muy gruñón. Si le hablas muy rápido, se harta y te ignora por completo.

Vas a configurar un sistema con un Rate Limit súper estricto y un cliente que no tiene paciencia y repite lo mismo una y otra vez.

### 📝 Instrucciones:

1. Crea tu archivo Python con las importaciones necesarias (`NexusHub`, `NexusClient`, `time`).
2. Configura tu `NexusHub` para que el límite sea de **1 mensaje por segundo** (`rate_limit_messages_per_sec=1`). Inícialo.
3. Crea un cliente llamado `"cajero"` y ponlo a escuchar (`listen`). Cuando reciba un mensaje, debe imprimir: `🏦 [CAJERO] Procesando petición: {payload}`.
4. Crea otro cliente llamado `"cliente_impaciente"`.
5. El `"cliente_impaciente"` usará un bucle `for` para enviar **5 mensajes EXACTAMENTE iguales** al cajero: `{"peticion": "¡Quiero mi dinero ya!"}`.
6. **El truco:** Dentro del bucle, inmediatamente después de enviar el mensaje con `.send()`, usa `time.sleep(0.2)` (0.2 segundos). Esto significa que enviará los 5 mensajes en tan solo 1 segundo.
7. Al final de tu código (fuera del bucle), espera 2 segundos y cierra/desconecta el sistema como siempre.

### ⛔ Reglas Estrictas:
* **Permitido:** `for`, `time.sleep(0.2)`, `NexusHub(rate_limit_messages_per_sec=1)`.
* **Prohibido:** Olvidar configurar el límite en el Hub. Si se te olvida, el cajero imprimirá las 5 peticiones y habrás reprobado.
* **Prohibido:** Usar un `time.sleep()` mayor a 1 segundo dentro del bucle. El objetivo es provocar que el Hub tire los mensajes a la basura porque vas demasiado rápido.

### 🎯 Resultado Esperado en la Terminal:
```text
🏦 [CAJERO] Procesando petición: {'peticion': '¡Quiero mi dinero ya!'}
```
*(Solo debe procesarse una petición. Puede que veas advertencias rojas en tu consola diciendo "Rate limit exceeded". ¡Eso es bueno, significa que el Hub detuvo al impaciente!)*
