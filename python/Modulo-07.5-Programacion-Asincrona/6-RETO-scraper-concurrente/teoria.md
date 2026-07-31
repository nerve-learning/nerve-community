# El Arsenal Asíncrono Completo

No hay conceptos nuevos en este nivel. Es hora de ensamblar las piezas de Lego que ya conoces. 
Repasemos lo que significa cada símbolo que usarás:

1. **`asyncio.run()`**: El interruptor maestro. Enciende el Event Loop.
2. **`async def`**: Define una función que tiene el superpoder de ser pausada.
3. **`async with aiohttp.ClientSession() as sesion:`**: Abre un canal de comunicación de alto rendimiento con internet. Cerramos la puerta al salir.
4. **`async with sesion.get(url) as respuesta:`**: Toca la puerta de la página web sin quedarnos congelados esperando.
5. **`await respuesta.text()`**: Esperamos educadamente a que se descarguen los datos del sitio web.
6. **`try / except`**: El escudo protector. Si una página se cae, la atrapamos para que nuestro programa no explote.
7. **`asyncio.gather()`**: El lanzacohetes de tareas. Enviamos a todos nuestros mini-bots al mismo tiempo a visitar distintas páginas.

### El Reto Final
El sitio al que te enfrentarás en el reto (`https://nerve.community.aleniastudios.me/`) es un sitio de prueba. Tu objetivo será crear tareas para descargar diferentes apartados o "endpoints" al mismo tiempo y ver qué tan rápido la programación asíncrona puede hacer el trabajo en comparación con hacerlo de forma síncrona.

### ¿Qué pasa si me equivoco?
Si te atascas en el reto, revisa tus `await`. Si usas `session.get(url)` sin `async with`, tendrás errores extraños de contexto. Si usas `respuesta.text()` sin `await`, te quedarás con una promesa vacía. ¡Revisa tu sintaxis detenidamente!
