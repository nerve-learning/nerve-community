# Reto 16: El Validador de Perfiles 📱

Te han contratado para limpiar la base de datos de una nueva red social. Hay usuarios que han creado cuentas, pero a veces no llenan su "Biografía" o todavía no tienen "Seguidores". 
Tu misión es usar el poder de "Truthy y Falsy" para darles un diagnóstico rápido sin usar comparadores (`==`, `!=`, `>`, `<`).

## Instrucciones

1. Crea dos variables para un usuario:
   * `biografia` (un texto. Escribe un texto corto o déjalo vacío `""`).
   * `seguidores` (un número entero. Pon un número o pon `0`).

2. **Revisión de Biografía**:
   * Escribe un `if` que reciba directamente la variable `biografia` (sin comparadores).
   * Si es Truthy, imprime: `"Biografía lista para mostrarse."`
   * Si es Falsy (usa un `else`), imprime: `"Tu perfil está muy vacío. ¡Escribe algo sobre ti!"`

3. **Revisión de Seguidores**:
   * Escribe otro `if` que reciba directamente la variable `seguidores` (sin comparadores).
   * Si es Truthy, imprime: `"¡Ya tienes tu propia audiencia!"`
   * Si es Falsy (con un `else`), imprime: `"Aún no tienes seguidores. ¡Empieza a publicar!"`

### Conceptos permitidos
- Variables (asignación con `=`).
- Tipos de datos (`int`, `str`).
- Estructura condicional (`if`, `else`).
- El concepto de Truthy/Falsy (usar variables como si fueran booleanos).
- `print()`.

### Conceptos prohibidos
- PROHIBIDO usar NINGÚN comparador de los que vimos antes (`==`, `!=`, `>`, `<`, `>=`, `<=`).
- Funciones `def`.
- Lógica anidada compleja (haz los `if` separados).

### Resultado esperado en terminal
Si configuras `biografia = ""` y `seguidores = 5`, al correr tu código la terminal debe mostrar exactamente esto:

```text
Tu perfil está muy vacío. ¡Escribe algo sobre ti!
¡Ya tienes tu propia audiencia!
```
