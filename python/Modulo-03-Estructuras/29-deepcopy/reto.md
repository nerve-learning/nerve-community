# Reto 29: El Experimento de la Estación Espacial 🚀

La agencia espacial te ha encargado hacer pruebas de resistencia en un nuevo módulo de la estación espacial. 

No puedes hacer pruebas peligrosas en la estación real, así que debes crear una simulación (un clon profundo y perfecto). Si ocurre una explosión en tu simulación, la estación real debe quedar totalmente intacta.

## Instrucciones

1. Crea una lista llamada `estacion_real`. Esta lista debe contener exactamente esto:
   - En la posición 0: El texto `"Panel Solar"`.
   - En la posición 1: El texto `"Motor Principal"`.
   - En la posición 2: Una lista interna que represente la sala de control, con los textos `"Computadora"` y `"Soporte Vital"`.
2. Trae a tu archivo la herramienta necesaria para hacer copias profundas. (Recuerda poner esto en la primera línea de tu archivo).
3. Crea una variable llamada `simulacion` y guarda ahí un clon profundo de la `estacion_real`.
4. ¡Oh, no! En tu simulación, ocurrió un fallo. Entra a la lista interna de la variable `simulacion` (la sala de control) y elimina el `"Soporte Vital"` usando `.remove()`.
5. Imprime en pantalla un título que diga `"--- REPORTE DE DAÑOS ---"`.
6. Imprime un mensaje indicando la estación real y muestra su contenido, luego otro mensaje para la simulación mostrando su contenido.

## Conceptos permitidos
- Listas y listas anidadas `[]`.
- Strings (texto) `""`.
- Comando `import`
- Herramienta `.deepcopy()`
- Índices `[2]`
- Método `.remove()`
- Función `print()`

## Resultado esperado en la terminal
```text
--- REPORTE DE DAÑOS ---
Estación Real: ['Panel Solar', 'Motor Principal', ['Computadora', 'Soporte Vital']]
Simulación: ['Panel Solar', 'Motor Principal', ['Computadora']]
```
