# El Mapa del Ecosistema 🧩

Para que un ecosistema de software no colapse, los programadores organizan el código usando todos los trucos que has aprendido. Así es como se conectan:

## 1. El Jefe Absoluto (Singleton `__new__`)
En todo ecosistema suele haber un "Gestor" o "Motor" central. Solo debe haber UNO. Él controla el estado global (ej. En qué turno del juego vamos, o si la conexión a internet está activa). 

## 2. Las Leyes de la Física (Abstracción `ABC`)
Antes de crear cosas concretas, creamos los "Moldes Fantasma". Por ejemplo, la idea abstracta de un `Personaje`. No existen personajes genéricos, pero esta clase dicta las reglas: *"Todo personaje que exista en este mundo DEBE saber atacar"*.

## 3. Los Secretos Vitales (Encapsulamiento `__` y Propiedades `@property`)
Los seres de nuestro ecosistema tienen cosas privadas, como sus puntos de vida. ¡Nadie desde afuera debería poder decir `personaje.vida = -5000` directamente! Los protegemos con `__` y usamos Cadeneros (`@property`) para curarlos o dañarlos siguiendo las reglas.

## 4. La Población (Herencia y Polimorfismo)
De los moldes abstractos nacen las clases reales: `Mago`, `Guerrero`. Heredan todo del padre, pero cada uno ataca a su propia manera (Polimorfismo).

## 5. La Memoria Colectiva (Métodos de Clase `@classmethod`)
A veces necesitamos saber datos de toda la especie, no de un solo individuo. Por ejemplo: "¿Cuántos personajes hemos creado en total en todo el mundo?". Para eso usamos `cls` y una variable de clase.

## 6. La Voz (Métodos Dunder `__str__`)
Cuando el Gestor del universo quiera imprimir a un individuo en la consola para saber su estado, el individuo sabrá presentarse de forma bonita y legible.

---
### ⚠️ ¿Qué pasa si me equivoco hoy?
El error más común en sistemas grandes es el **Orden**. 
- Recuerda que un hijo no puede nacer si su clase padre no ha sido escrita antes en el código.
- Recuerda que no puedes llamar a un método abstracto si el hijo no lo implementó.
- Respira profundo. Lee los errores de la terminal, te dirán exactamente en qué línea tropezaste.
