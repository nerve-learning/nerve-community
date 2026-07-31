# Teoría: El Guardia de Seguridad (Auth Token)

Imagina que tu Hub es un club exclusivo. Hasta ahora, las puertas estaban abiertas de par en par. Cualquiera que supiera dónde estaba el club, podía entrar, escuchar conversaciones y gritar mensajes falsos.

Para solucionar esto, introducimos el concepto de **Auth Token** (Token de Autenticación). Es literalmente una contraseña. Si un cliente intenta conectarse y no sabe la contraseña, el Hub le cierra la puerta en la cara.

## Dos formas de usar el Auth Token

### 1. Directo en el código (Mala práctica en producción)

Puedes pasarle la contraseña directamente cuando creas el cliente o el Hub:

```python
hub = NexusHub(auth_token="mi_secreto_123")
# o
cliente = NexusClient(auth_token="mi_secreto_123")
```
Esto funciona, pero es peligroso. Si subes tu código a internet, ¡todos verán tu contraseña!

### 2. El archivo de configuración (Buena práctica)

La forma profesional de desplegar aplicaciones es usar un archivo externo que *no* subimos a internet. Nerve buscará automáticamente un archivo llamado `nerve.config` en la misma carpeta donde ejecutas tu código.

**Anatomía del `nerve.config`:**
Es un archivo de texto simple. No lleva comillas, no lleva espacios alrededor del igual.

```text
auth_token=mi_secreto_123
```

¡Eso es todo! Si creas ese archivo, `NexusHub()` y `NexusClient()` lo leerán automáticamente.

## ¿Qué pasa si me equivoco?

El error más común es escribir la contraseña mal en el cliente o no tener el archivo `nerve.config` donde debería estar.

**¿Cómo se lee en la terminal?**
Verás un error rojo que dice algo como:
`[NERVE] Connected to hub as 'nodo_1' failed (auth).`
Esto significa que el Hub está vivo, te escuchó tocar la puerta, pero te rechazó porque tu contraseña (token) era incorrecta o no enviaste ninguna.
