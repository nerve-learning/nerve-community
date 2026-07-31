# Teoría: La Caja Fuerte de Acero

Imagina que tienes un documento en papel con la fórmula secreta de la Coca-Cola. 

- **Guardarlo normal:** Es como dejar el papel sobre tu escritorio. Si alguien entra a la habitación (un hacker o un virus), lo lee sin esfuerzo.
- **Usar Criptografía (Nerve):** Es como comprar una caja de titanio indestructible, meter el papel adentro, sellarla al vacío y ponerle un candado con una combinación. Ahora puedes dejar la caja en medio de la calle; todos la verán, pero nadie podrá abrirla sin la combinación.

A este proceso de sellado matemático se le llama **Encriptación**. En Nerve, las cajas fuertes tienen la extensión `.nrv`.

## Anatomía de la Criptografía en Nerve

Para construir estas cajas fuertes no necesitamos ser matemáticos genios. Nerve nos da dos herramientas (funciones): una para empacar (`pack`) y otra para desempacar (`unpack`).

```python
from nerve import pack_nrv, unpack_nrv
```
* **Qué hace:** Traemos las herramientas de cerrajería desde la fábrica de Nerve.

```python
pack_nrv("archivo_visible.txt", "caja_fuerte.nrv", "mi_secreto_123")
```
* **Qué hace:** 
  - 1er Parámetro: Lo que queremos proteger (puede ser un archivo o una carpeta entera).
  - 2do Parámetro: El nombre de la caja fuerte impenetrable que se va a crear.
  - 3er Parámetro: La combinación del candado (tu contraseña).

```python
unpack_nrv("caja_fuerte.nrv", "carpeta_extraida", "mi_secreto_123")
```
* **Qué hace:** Toma la caja fuerte, prueba la contraseña, y si es correcta, escupe los archivos originales dentro de la `"carpeta_extraida"`.

---

## ¿Qué pasa si me equivoco?

### 1. El Error Fatídico: Olvidar la Contraseña
Si pierdes tu contraseña de un archivo `.nrv`, **lo pierdes para siempre**. 
A diferencia de Netflix o Facebook donde puedes dar clic en "olvidé mi contraseña", la encriptación matemática de Nerve (AES-GCM + Argon2) no guarda tu contraseña en ninguna nube ni tiene puerta trasera. ¡Ni los creadores de Nerve pueden abrir tu archivo!

### 2. Contraseña Incorrecta
Si intentas desempacar un archivo con una contraseña mala, verás un error en rojo:
`ValueError: Invalid password or corrupted .nrv container`
Python te dice: *"La llave que metiste no gira en el candado. O me diste la llave equivocada, o alguien rompió el candado."*
