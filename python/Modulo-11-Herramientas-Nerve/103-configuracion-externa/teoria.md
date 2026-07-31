# Teoría: La Separación de Poderes ⚖️

Cuando escribes `cliente = NexusClient()`, el código de Python asume que el Hub está en su dirección predeterminada. Si quisieras cambiar la dirección, podrías pasársela al código... pero ¡espera! Si le pones la dirección al código, y mañana quieres cambiarla, tendrás que editar el código fuente de tu programa (y tal vez ya se lo vendiste a un cliente).

Para evitar esto, usamos un archivo externo: `nerve.config`.

## Anatomía de `nerve.config`

Nerve busca automáticamente un archivo con este nombre exacto en la misma carpeta desde la que estás ejecutando tu programa o el Hub.

Puede escribirse de dos maneras:

### 1. Formato Clave-Valor (El más fácil)
Es tan simple como escribir variables sin comillas ni espacios raros.
```text
port=8080
host=127.0.0.1
socket_path=/tmp/mi_red_secreta.sock
```

### 2. Formato JSON (El estructurado)
Usando la misma sintaxis de diccionarios que aprendimos antes.
```json
{
  "port": 8080,
  "host": "127.0.0.1",
  "socket_path": "/tmp/mi_red_secreta.sock"
}
```

- `port`: (Número) El "puerto" de red que usará en Windows o si lo fuerzas.
- `host`: (Texto) La dirección IP de la computadora (127.0.0.1 significa "esta misma máquina").
- `socket_path`: (Texto) La ruta del archivo físico en Linux/Mac donde ocurrirá la magia.

## ¿Qué pasa si me equivoco?

**El error más común:** Llamar al archivo `nerve.txt` o `config.nerve`.
**¿Qué verás?** Nerve simplemente lo ignorará. Iniciará en su dirección predeterminada de siempre (puerto 50505), y si esperabas que iniciara en el 8080, tus programas no se encontrarán.

**Otro error clásico:** Escribir mal la sintaxis del JSON (olvidar una coma o una comilla). Si haces esto, Nerve se quejará al arrancar y te dirá que el archivo de configuración está corrupto. ¡Por eso el formato clave-valor suele ser a prueba de balas para principiantes!
