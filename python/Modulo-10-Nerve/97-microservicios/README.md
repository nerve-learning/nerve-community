# Nivel 97: Microservicios 🏭

¿Alguna vez has visto un restaurante donde una sola persona toma la orden, cocina la comida, lava los platos y cobra la cuenta? Probablemente sería un caos y muy lento.

En programación, cuando un solo archivo hace absolutamente de todo, le llamamos **Monolito**. Funciona cuando eres pequeño, pero si el sistema crece, es inmanejable. 

La solución de las grandes empresas (como Netflix o Amazon) es usar **Microservicios**: dividir ese gran programa en programas diminutos y especialistas. Uno solo toma órdenes, otro solo cocina, y otro solo cobra. ¿Cómo trabajan juntos? ¡Enviándose mensajes!

En este nivel aprenderás a:
1. Entender la diferencia entre un Monolito y una Arquitectura de Microservicios.
2. Usar `alenia-nerve` para comunicar procesos especializados.
3. Enviar mensajes directos usando `.send()` en lugar de gritarle a todos con `.broadcast()`.

## Ruta de Aprendizaje

- `teoria.md`: El arte de delegar tareas y cómo preparar nuestro Hub de Nerve.
- `ejemplo.py`: El restaurante digital (Mesero y Chef trabajando juntos).
- `reto.md`: Tu primer microservicio matemático.
