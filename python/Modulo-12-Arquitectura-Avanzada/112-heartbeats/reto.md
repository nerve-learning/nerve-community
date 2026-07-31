# Reto 112: El Hospital de Androides 🏥

Te acaban de nombrar Director de Sistemas del nuevo Hospital de Androides. Los androides (clientes) están conectados a la Máquina Central (Hub) que monitorea sus constantes vitales.

Como los androides son muy delicados, el valor por defecto de 5 segundos es muy lento. Si un androide falla, necesitamos saberlo casi de inmediato.

### 📝 Instrucciones:

1. Crea un archivo de Python vacío.
2. Importa `NexusHub`, `NexusClient` y `time`.
3. Crea un `NexusHub` llamado `maquina_central` y configúrale los latidos (`heartbeat_interval`) para que revise el pulso exactamente cada `1.5` segundos.
4. Enciende la `maquina_central` usando `.start()`.
5. Imprime el texto: `🏥 Maquina Central encendida: Monitor cardiaco cada 1.5s`
6. Crea un `NexusClient`, llámalo `androide_azul` y conéctalo con el nombre `"androide_azul"`.
7. Imprime el texto: `🤖 Androide Azul conectado.`
8. Usa `time.sleep(4)` para esperar 4 segundos (tiempo suficiente para que ocurran dos latidos en secreto).
9. Finalmente, desconecta al androide y detén la máquina central. Imprime `🛑 Desconexion exitosa.`

### ⛔ Reglas Estrictas:
* **Permitido**: Importar, crear el Hub con el parámetro nuevo, crear el cliente, imprimir textos y usar `time.sleep()`.
* **Prohibido**: Poner el número `1.5` entre comillas (`"1.5"`). Si lo haces, destruirás la Máquina Central.

### 🎯 Resultado Esperado en la Terminal:
```text
🏥 Maquina Central encendida: Monitor cardiaco cada 1.5s
🤖 Androide Azul conectado.
🛑 Desconexion exitosa.
```
