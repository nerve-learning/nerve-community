# Nivel 98: Despliegue y Seguridad 🚀

¡Felicidades! Tienes microservicios hablando entre sí. Pero hay un problema crítico: ahora mismo, tu red es como una casa con la puerta abierta. Cualquier otro programa en tu computadora podría conectarse a tu Hub y escuchar o enviar mensajes.

Cuando pasamos de "jugar en nuestro editor" a "ponerlo en producción" (lo que los programadores llaman **Despliegue**), necesitamos dos cosas:
1. **Configuración externa**: No queremos escribir contraseñas directamente en el código de Python.
2. **Autenticación**: Necesitamos un guardia de seguridad en la puerta de nuestra red.

En este nivel aprenderás a:
1. Usar un token de autenticación (`auth_token`) para proteger tu Hub.
2. Usar un archivo de configuración (`nerve.config`) para guardar secretos de forma segura.

## Ruta de Aprendizaje

- `teoria.md`: Entenderemos cómo funcionan los archivos de configuración y las llaves de acceso.
- `ejemplo.py`: Un código que usa una contraseña para entrar al club VIP de nuestra red.
- `reto.md`: Tu misión: Configurar un Hub impenetrable usando archivos externos.
