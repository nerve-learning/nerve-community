# Reto: El Mecánico de Código 🛠️

## Tu Misión

El sistema de registro de nuestra nave espacial está dañado. El ingeniero anterior escribió el código a las 3:00 AM y dejó varios errores. 
Tu trabajo es ejecutar el archivo, leer los mensajes en rojo que te da Python (Tracebacks), buscar la línea del problema, corregirlo y volver a ejecutar hasta que el programa funcione de principio a fin.

## Pasos

1. Crea un archivo llamado `reto.py`.
2. Copia y pega el siguiente código **exactamente** como está:

```python
print("Iniciando diagnóstico del sistema de la nave...)

combustible_litros = 5000
distancia_km = 10000

# Calculamos el consumo
consumo = distncia_km / combustible_litros

# Mostramos el resultado
print(f"El consumo es de {consumo} kilómetros por litro.")

mensaje_final = "Diagnóstico completado. Nivel de éxito: "
porcentaje = 100

# Intentamos mostrar el mensaje final
resultado_final = mensaje_final + porcentaje
print(resultado_final)
```

3. Ejecuta el archivo en tu terminal (`python reto.py`).
4. **¡Boom!** Fallará. Lee el mensaje, encuentra la línea que te indica Python y arregla el primer error (Pista: tiene que ver con comillas).
5. Vuelve a ejecutar. **¡Boom!** Fallará otra vez. Lee el mensaje (Pista: revisa cómo se escribieron las variables). Arréglalo.
6. Vuelve a ejecutar. **¡Boom!** Último fallo. (Pista: estás mezclando texto con números de forma incorrecta. ¿Recuerdas las f-strings?). Arréglalo.
7. Cuando al ejecutar el programa ya no salga ningún mensaje en rojo y veas todo el texto en pantalla, ¡habrás superado el reto!
