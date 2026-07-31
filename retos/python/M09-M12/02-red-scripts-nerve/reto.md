# Red de Scripts con Nerve

> **Nivel**: Módulos 09–12 completados
> **Tiempo estimado**: 5 horas
> **Lenguaje**: Python

## Tu misión

Crea una red de 3 scripts que se comunican entre sí usando Nerve.

## Lo que debe hacer tu programa

- Script 1 (productor): genera datos cada 2 segundos y los envía
- Script 2 (procesador): recibe, transforma y reenvía
- Script 3 (monitor): muestra un dashboard en tiempo real
- El sistema debe sobrevivir si uno de los scripts se reinicia

## Restricciones (respétalas o el reto no cuenta)

- **Solo puedes usar** conceptos de los módulos 01 al 12
- **Obligatorio**: usar NexusClient y NexusHub de nerve
- **Obligatorio**: manejo de reconexión automática
- **No puedes usar**: threading directamente (usa async/await)

## Criterio de éxito

Tu solución es válida si:
1. Los 3 scripts corren simultáneamente sin errores
2. Si cierras y abres un script, se reconecta y sigue funcionando
3. Alguien que no te conoce puede entender el output sin explicación
