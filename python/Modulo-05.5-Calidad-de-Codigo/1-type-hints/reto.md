# Reto 1: El Etiquetador del Almacén 🏷️

El almacén de la empresa tiene un sistema de funciones completamente sin etiquetas. Tu jefe te pide que las etiquetes todas correctamente antes de que llegue el nuevo programador a trabajar con ellas.

## Instrucciones Paso a Paso:

Copia exactamente estas 5 funciones en tu archivo `reto.py` y **agrega los Type Hints correctos** a cada una:

```python
def calcular_impuesto(precio, porcentaje):
    return precio * (porcentaje / 100)

def repetir_mensaje(mensaje, veces):
    return mensaje * veces

def es_numero_par(numero):
    return numero % 2 == 0

def construir_perfil(nombre, edad, ciudad):
    return {"nombre": nombre, "edad": edad, "ciudad": ciudad}

def imprimir_separador(caracter, longitud):
    print(caracter * longitud)
```

Para cada función, identifica:
1. ¿Qué tipo de dato recibe cada parámetro? (`str`, `int`, `float`, `bool`, `list`, `dict`)
2. ¿Qué tipo de dato devuelve? (¿texto? ¿número? ¿verdadero/falso? ¿diccionario? ¿nada?)

Después de agregar las etiquetas, llama a cada función con valores reales e imprime el resultado para confirmar que funciona.

> **Pista para `imprimir_separador`:** Esta función usa `print()` pero no tiene `return`. ¿Qué tipo de retorno le corresponde?

## Reglas Estrictas:
✅ **Conceptos Permitidos:** `def`, `: Tipo` en parámetros, `-> Tipo` en retorno, `return`, `print()`, f-strings, llamar funciones con valores reales.
❌ **Conceptos Prohibidos:** `import`, clases, cambiar la lógica interna de las funciones. Solo agregas etiquetas, no reescribes el código.

## Resultado Esperado en tu Terminal:

```text
Impuesto de $500 al 16%: $80.0
Mensaje repetido: HolaHolaHola
¿El 8 es par?: True
Perfil creado: {'nombre': 'Kaia', 'edad': 25, 'ciudad': 'CDMX'}
------------------------------
```

Crea tu código en `reto.py`. Si tu editor (VS Code) subraya en rojo cuando llamas a una función con el tipo incorrecto, significa que las etiquetas están funcionando correctamente.
