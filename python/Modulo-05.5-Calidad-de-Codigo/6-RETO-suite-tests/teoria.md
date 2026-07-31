# Teoría: El Cinturón Negro de Calidad 🥋

¡Llegaste al final del módulo! Ya no escribes código "a ciegas". Has aprendido a crear código profesional, autodocumentado y blindado contra errores. 

Repasemos tu nuevo cinturón de herramientas:

1. **Type Hints (`: int`, `-> str`)**
   Las etiquetas de las cajas. Le dicen al mundo y a tu editor qué tipos de datos entran y qué sale de tus funciones.
   
2. **Docstrings (`"""..."""`)**
   El manual de instrucciones integrado. Responde la pregunta "¿Para qué sirve esto?" usando las secciones `Args:` y `Returns:`.

3. **pytest y `assert`**
   Tu robot inspector. Usa `assert` para exigirle a tu código que siempre devuelva lo que esperas. Si algo es mentira, pytest levanta la alarma.

4. **Fixtures (`@pytest.fixture`)**
   Tus ayudantes. Funciones especiales que fabrican y te entregan configuraciones o datos listos (como carritos de compras o usuarios falsos) directo a los parámetros de tus tests.

5. **Parametrize (`@pytest.mark.parametrize`)**
   La fotocopiadora de tests. Te permite escribir un solo test y repetirlo mágicamente decenas de veces con diferentes valores, ahorrándote mucho tiempo.

6. **Mocks (El Doble de Acción)**
   La técnica maestra. Cuando una función necesita conectarse a internet o hacer pagos (cosas impredecibles), le pasamos un "Doble de Acción" (una función falsa muy predecible) como parámetro para probar nuestra lógica sin riesgos.

En una **Suite de Tests** profesional (un archivo lleno de muchas pruebas), usamos todas estas herramientas combinadas. 

En el reto de hoy, te enfrentarás a un código legacy (código viejo y descuidado). Tu deber será aplicar tu cinturón negro para domarlo, documentarlo y blindarlo. ¡A pelear!
