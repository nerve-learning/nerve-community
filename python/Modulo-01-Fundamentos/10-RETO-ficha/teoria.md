# Teoría: El Arsenal del Fundador

Llegaste al Nivel 10 con un cinturón de herramientas poderoso. Antes de enfrentarte al reto final, repasemos cómo se usa cada herramienta.

### 1. Hablar con la pantalla (`print`)
Tu forma de comunicarte con el mundo exterior.
```python
print("Hola, soy un programa")
```

### 2. Cajas de almacenamiento (Variables y `=`)
El símbolo `=` no es igualdad, significa "guarda lo de la derecha en la caja de la izquierda".
```python
vidas = 3
```

### 3. Escuchar al usuario (`input`)
Pones en pausa el programa y esperas a que el humano escriba algo. **Siempre** te entrega texto.
```python
nombre = input("¿Cómo te llamas? ")
```

### 4. Transformar datos (Casteo)
Como `input` siempre da texto, si quieres hacer matemáticas, debes transformar la caja.
```python
edad_texto = input("Tu edad: ")
edad_numero = int(edad_texto)  # Transforma el texto a entero
altura = float("1.75")         # Transforma a decimal
```

### 5. Matemáticas básicas
Puedes sumar (`+`), restar (`-`), multiplicar (`*`) y dividir (`/`).
```python
dano_total = 15 * 3
```

### 6. Pegamento mágico (`f-strings`)
La mejor forma de mezclar palabras normales con las cajas (variables) sin causar errores de tipo. Pones una `f` al inicio y llaves `{}` alrededor de la caja.
```python
print(f"Tienes {vidas} vidas restantes, {nombre}.")
```

### 7. Notas secretas (`#`)
El símbolo `#` le dice a Python que ignore el resto de la línea. Es para ti y tu equipo.
```python
# Este código calcula el daño
```

### 8. Interpretar explosiones (Errores)
Si ves rojo, no corras. Lee la última línea.
*   `SyntaxError`: Escribiste mal un símbolo (te falta un paréntesis o comilla).
*   `NameError`: Usaste una caja que no existe o la escribiste mal.
*   `TypeError`: Mezclaste tipos incompatibles (como sumar texto con un número sin usar f-strings).

Con esto estás listo para construir programas completos. ¡Pasa al ejemplo y luego al reto!
