# Nivel 29: Clonación Profunda (Deepcopy) 🧬

En el nivel anterior descubrimos un problema muy peligroso: cuando usamos `[:]` para clonar una lista, funciona bien... **¡hasta que hay listas dentro de listas!** 

Si tienes una caja principal con cajitas adentro, el truco de `[:]` solo compra una caja principal nueva, pero mete las *mismas cajitas originales* adentro. Si modificas una cajita en el clon, se rompe también en la original.

En la vida real, cuando guardas un documento de Excel que tiene varias hojas, quieres que al hacer "Guardar como..." todo el nuevo archivo sea completamente independiente. Para lograr esto en Python con estructuras anidadas, necesitamos pedir ayuda a una herramienta especial llamada `deepcopy` (clonación profunda).

## Ruta de aprendizaje
1. **Teoría:** Aprenderemos a traer herramientas externas a nuestro código (`import`) y qué hace exactamente `deepcopy`.
2. **Ejemplo:** Veremos la diferencia en vivo entre un clon falso (superficial) y un clon real (profundo).
3. **Reto:** Clonarás una estación espacial con diferentes compartimentos para asegurar que los daños en el clon no afecten a la estación original.
