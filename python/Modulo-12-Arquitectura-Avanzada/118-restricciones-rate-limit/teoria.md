# El Escudo Anti-Spam

Por defecto, cuando inicias tu `NexusHub()`, es como una plaza pública. Cualquiera puede gritar tan rápido como pueda. 
Pero Nerve (recuerda instalarlo en tu PC con `pip install alenia-nerve`) tiene la capacidad de contratar un guardia de seguridad interno.

### 1. El Concepto de Rate Limit (Límite de Tasa)

La idea es simple: Establecer una regla de **"Máximo X mensajes por segundo"**.
Si un bot respeta la regla, sus mensajes pasan con normalidad. Si se desespera y envía más rápido de lo permitido, el guardia (el Hub) tira los mensajes sobrantes a la basura directamente. El destinatario nunca se entera de que hubo un exceso de mensajes.

### Anatomía del Cadenero

Para activarlo, debes pasarle las instrucciones al Hub en el momento exacto en que lo creas, usando un parámetro especial:

```python
# Permitimos máximo 2 mensajes por segundo.
hub = NexusHub(rate_limit_messages_per_sec=2)
```

También existe otro límite enfocado en el tamaño de lo que envías (para evitar que envíen fotos o archivos gigantes que traben la red):

```python
# Máximo 5000 bytes (letras/caracteres) por minuto.
hub = NexusHub(rate_limit_bytes_per_min=5000)
```

*Nota:* Si un bot excede el límite, el Hub simplemente ignora el mensaje. En la terminal donde está corriendo el Hub verás una advertencia que dice: `Rate limit exceeded for client.`, indicando que el cadenero hizo su trabajo.

### ¿Qué pasa si me equivoco?

**El Error de la Asfixia Estricta:**
Si configuras `rate_limit_messages_per_sec = 0.1` (pensando que significa 1 mensaje cada 10 segundos), ten mucho cuidado. Un número demasiado bajo podría bloquear TODO el tráfico legítimo y tus bots nunca lograrán comunicarse. Siempre empieza con números razonables como `5` o `10` para protegerte de ráfagas masivas. Si estás programando un videojuego donde los bots envían su posición 60 veces por segundo, ¡no debes usar un límite bajo!
