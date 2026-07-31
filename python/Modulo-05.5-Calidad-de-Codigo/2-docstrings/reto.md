# Reto 2: El Escritor de Manuales 📖

El nuevo programador vio tus Type Hints (¡buen trabajo!) pero ahora se queja de que no entiende qué hacen las funciones matemáticamente complejas. Tu jefe te pide que agregues el manual de instrucciones (Docstrings) a 3 funciones críticas.

## Instrucciones Paso a Paso:

Copia estas 3 funciones en tu archivo `reto.py` y **agrega un docstring completo** (con descripción, Args y Returns) a cada una.

```python
def calcular_area_triangulo(base: float, altura: float) -> float:
    return (base * altura) / 2

def es_mayor_de_edad(edad: int) -> bool:
    return edad >= 18

def crear_usuario(nombre: str, correo: str) -> dict:
    return {"user": nombre, "email": correo, "activo": True}
```

Para cada función:
1. Agrega las `"""` (comillas triples) justo debajo de la línea `def`, con indentación correcta.
2. Escribe una oración que empiece con un verbo (ej. "Calcula...", "Verifica...").
3. Agrega la sección `Args:` explicando cada parámetro.
4. Agrega la sección `Returns:` explicando qué devuelve.
5. Al final de tu archivo `reto.py`, usa la función `help()` para imprimir el manual de `crear_usuario` en la terminal y comprobar que lo hiciste bien.

## Reglas Estrictas:
✅ **Conceptos Permitidos:** `def`, `"""`, Type Hints (`:`, `->`), diccionarios, `help()`.
❌ **Conceptos Prohibidos:** Clases, importar módulos, cambiar la lógica interna. ¡Solo escribe texto entre comillas triples!

## Resultado Esperado en tu Terminal:

Al ejecutar tu código, la salida de `help(crear_usuario)` debería mostrar algo muy similar a esto (el texto exacto dependerá de lo que escribiste):

```text
Help on function crear_usuario in module __main__:

crear_usuario(nombre: str, correo: str) -> dict
    Crea un diccionario con los datos del usuario.
    
    Args:
        nombre: El nombre del usuario.
        correo: El correo electrónico del usuario.
        
    Returns:
        Un diccionario con las claves 'user', 'email' y un estado 'activo' en True.
```

¡Escribe tus manuales en `reto.py` y verifica tu resultado!
