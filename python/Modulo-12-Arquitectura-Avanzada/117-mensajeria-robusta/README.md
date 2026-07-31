# Nivel 117: El Cartero que Exige Firma (Mensajería Robusta) 🛡️

Imagina que envías un paquete muy valioso por correo. Lo dejas en el buzón y... te olvidas. ¿Llegó? ¿Se perdió en el camino? ¿Se quemó el camión de reparto? No tienes idea. En el mundo del software, a esto se le llama "Disparar y Olvidar" (Fire and Forget).

Cuando construimos sistemas distribuidos reales (donde hay dinero, datos de salud o información crítica), no podemos darnos el lujo de "suponer" que el mensaje llegó. Necesitamos que el destinatario firme de recibido.

En este nivel aprenderás a implementar **Mensajería Robusta**, asegurándote de que tus bots de Nerve no solo envíen mensajes, sino que confirmen que el otro lado hizo su trabajo correctamente. 

Además, repasaremos cómo instalar y preparar tu entorno con Nerve, ya que para usar estas arquitecturas necesitas la herramienta instalada.

### Ruta de aprendizaje

1. **Teoría (`teoria.md`)**: Qué es un ACK (Acuse de Recibido) y cómo evitar que un mensaje envenenado mate a tu bot.
2. **Ejemplo (`ejemplo.py`)**: Construiremos un sistema de Cajero Automático y Banco, donde el dinero solo se descuenta si hay confirmación.
3. **Reto (`reto.md`)**: Programarás el sistema de comandas seguras de un Restaurante.
