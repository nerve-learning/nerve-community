# Sobreviviendo a la Red

Cuando usas `asyncio.gather()` para lanzar 10 peticiones al mismo tiempo, ¿qué pasa si 1 de ellas falla (por ejemplo, la URL no existe)?
Si no hacemos nada, esa única falla lanzará un error que **destruirá el programa completo** y las otras 9 peticiones exitosas se perderán.

Para evitar esto, usamos el clásico bloque `try/except` DENTRO de nuestra función asíncrona.

### Desmontaje Conceptual
La sintaxis es idéntica a la que ya conoces, solo la envolvemos alrededor de nuestras llamadas asíncronas.

```python
async def descargar(url):
    try:
        # Intentamos hacer algo peligroso que depende de internet
        async with sesion.get(url) as respuesta:
            return await respuesta.text()
    except Exception as e:
        # Si algo explota (Error 404, no hay internet, etc)
        # La computadora salta aquí, atrapa el error en la variable 'e'
        # y permite que el programa siga viviendo.
        print(f"Error al descargar: {e}")
```

### El parámetro salvavidas en Gather
Otra herramienta fantástica es decirle a `gather` que no entre en pánico si una tarea falla.
`await asyncio.gather(tarea1(), tarea2(), return_exceptions=True)`

- **`return_exceptions=True`**: Significa "Si una de estas tareas explota, no detengas a las demás. Solo devuélveme el error como si fuera el resultado de esa tarea, para que yo sepa qué falló, pero deja que las demás terminen felices".

### ¿Qué pasa si me equivoco?
El error común es olvidar poner el `try/except` cuando haces un scraper masivo. De repente, tu código lleva 20 minutos descargando cosas, llega a un link roto, explota, y pierdes todo tu progreso. Siempre asume que las peticiones web van a fallar.
