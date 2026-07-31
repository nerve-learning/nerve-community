# Teoría: El Doble de Acción (Mocking) 🎭

Hay un principio en la calidad de código: **Tus tests nunca deben depender de cosas fuera de tu control**. Si tu test necesita internet y el wifi se cae, el test fallará, aunque tu código esté perfecto. Eso es injusto.

Para evitarlo, usamos **Mocks** (simulaciones).

## La forma más pura: Inyectar al Doble

¿Recuerdas que en Python las funciones son como cualquier otra variable? Puedes pasar un texto a una función, puedes pasar una lista, ¡y también puedes pasar *otra función*!

```python
# El actor "peligroso" (Impredecible, cambia cada vez)
def tirar_dado_real():
    # En la vida real, esto daría un número al azar del 1 al 6
    pass

# La función que queremos probar. 
# En vez de obligarla a usar siempre el dado real, le pedimos que RECIBA el dado que debe usar.
def jugar_turno(funcion_dado):
    resultado = funcion_dado()
    if resultado == 6:
        return "Ganaste"
    else:
        return "Perdiste"
```

Al obligar a la función a "recibir" al actor como parámetro, hemos hecho que sea 100% testeable. En el mundo del software real, esto se llama **Inyección de Dependencias** (le inyectas lo que necesita).

### El Test: Contratando al Doble de Acción

Ahora, en nuestro test, creamos un actor falso que siempre haga lo que nos convenga para la prueba:

```python
def test_ganar_el_juego():
    # 1. Creamos al doble de acción (el Mock)
    def dado_falso_que_siempre_gana():
        return 6  # Siempre devuelve 6, es súper predecible
        
    # 2. Le pasamos el doble a nuestra función en vez del actor real
    mensaje = jugar_turno(dado_falso_que_siempre_gana)
    
    # 3. Exigimos que el resultado sea victoria
    assert mensaje == "Ganaste"
```

## ¿Qué pasa si me equivoco?

**El error más común: Ejecutar la función falsa sin querer antes de tiempo**

```python
# MAL ❌
# Le pasaste el RESULTADO de la función (un número), no la función en sí.
jugar_turno(dado_falso_que_siempre_gana()) 

# BIEN ✅
# Le pasas el NOMBRE de la función, sin los paréntesis `()`. 
# Así, 'jugar_turno' podrá ejecutarla por dentro cuando la necesite.
jugar_turno(dado_falso_que_siempre_gana)
```

Fíjate muy bien en los paréntesis `()`. Cuando pasas el doble de acción como parámetro, se lo pasas sin los paréntesis. Es como entregarle la receta a un chef, en lugar de entregarle el pastel ya hecho.
