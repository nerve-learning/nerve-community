# Teoría: Empacando y Desempacando Cajas 📦

Para trabajar con JSON, Python incluye una herramienta de fábrica. No necesitas instalar nada de Internet, solo sacarla de la caja de herramientas con `import json`.

Esta herramienta tiene dos funciones mágicas principales:

### 1. Desempacar: `json.loads()`
La 's' al final significa **String** (Texto). `loads` se lee como *"Load String"* (Cargar Texto).
Toma una caja plana (un texto en formato JSON) y la "arma" convirtiéndola en un **Diccionario de Python** real que puedes usar.

```python
texto_internet = '{"nombre": "Mario"}' # Esto es solo texto
diccionario = json.loads(texto_internet) # ¡Magia! Ahora es un diccionario
```

### 2. Empacar: `json.dumps()`
La 's' también significa **String**. `dumps` se lee como *"Dump String"* (Volcar a Texto).
Toma tu hermoso **Diccionario de Python** y lo "aplasta" en un texto plano (JSON) para que puedas enviarlo por la red.

```python
mi_diccionario = {"nombre": "Luigi"} # Diccionario de Python
texto_para_enviar = json.dumps(mi_diccionario) # Ahora es texto JSON
```

---

## Anatomía de un JSON

A simple vista, un JSON se ve idéntico a un diccionario de Python, pero tiene una regla de oro estricta: **Las llaves siempre deben llevar comillas dobles `""`**.

```json
{
    "jugador": "Zelda",
    "vidas": 3,
    "tiene_espada": true
}
```
*Nota: En JSON los booleanos van en minúscula (`true`, `false`), pero al usar `json.loads()`, Python los convierte automáticamente a sus propios booleanos (`True`, `False`).*

---

## ¿Qué pasa si me equivoco? (El Panel de Errores)

**Error 1: `json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes`**
- **Por qué pasa:** Intentaste usar `json.loads()` en un texto que usaba comillas simples `''` en lugar de dobles `""` para los nombres de las propiedades. JSON es un lenguaje muy especial y solo acepta comillas dobles.
- **Solución:** Asegúrate de que el texto que estás desempacando sea un JSON válido con comillas dobles.

**Error 2: `TypeError: the JSON object must be str, bytes or bytearray, not dict`**
- **Por qué pasa:** Intentaste hacer `json.loads()` (desempacar) en algo que ¡ya era un diccionario! Solo puedes desempacar texto (cajas planas).
- **Solución:** Verifica si tus datos ya son un diccionario antes de intentar convertirlos.
