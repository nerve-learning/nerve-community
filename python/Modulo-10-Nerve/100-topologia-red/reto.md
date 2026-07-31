# Reto: El Observador de la Matriz 🕶️

Tu misión en este nivel es presenciar con tus propios ojos cómo Nerve enruta la información visualizando la Topología Estrella.

## Instrucciones

1. Abre tu primera terminal y ejecuta el comando para iniciar el enrutador central:
   ```bash
   nerve start
   ```
2. Abre una **segunda** terminal. Ahora usaremos la herramienta visual de Nerve. Ejecuta:
   ```bash
   nerve dashboard
   ```
   *Esto debería darte un enlace como `http://localhost:8080`. Ábrelo en tu navegador web.*
3. Abre una **tercera** terminal y ejecuta nuestro código de ejemplo:
   ```bash
   python ejemplo.py
   ```
4. ¡Vuelve rápidamente a tu navegador web! 
5. Observa cómo aparecen 3 nuevos "nodos" (bolitas) conectados al Hub central (`visor_grafico`, `motor_ia`, `base_de_datos_local`). 
6. ¡Felicidades! Estás viendo el "sistema nervioso" de tu computadora en tiempo real.

> **Nota**: Cuando el script de Python termine después de 60 segundos, verás que los nodos desaparecen automáticamente del dashboard. El Hub siempre sabe quién sigue vivo.

¡Con esto concluimos nuestra introducción general al módulo Nerve y estamos listos para adentrarnos en las herramientas profundas de línea de comandos en el Módulo 11!
