# Importamos a nuestro traductor de palabras a números
from sklearn.feature_extraction.text import CountVectorizer

print("--- 1. Los textos humanos ---")
# Una lista normal con oraciones que nosotros entendemos,
# pero que para la máquina son ruido incomprensible.
mensajes = [
    "Me encanta el helado",
    "Odio el helado",
    "Me encanta python"
]
print("Mensajes originales:")
print(mensajes)


print("\n--- 2. Invocando al Traductor ---")
# Creamos a nuestro traductor
traductor = CountVectorizer()

# Le pedimos que lea, aprenda y traduzca todo en un solo paso
mensajes_traducidos = traductor.fit_transform(mensajes)
print("¡Traducción completada!")


print("\n--- 3. Lo que ve la computadora ---")
# OJO: Usamos .toarray() para descomprimir el resultado y poder verlo
# Verás puros 0s y 1s. Cada fila es una oración de las de arriba.
print(mensajes_traducidos.toarray())


print("\n--- 4. El diccionario secreto ---")
# ¿Cómo sabemos qué significa cada columna de números de arriba?
# Le preguntamos al traductor qué palabras aprendió:
print(traductor.get_feature_names_out())
print("(Nota cómo el traductor, para simplificarse la vida, convierte todo a minúsculas y ordena las palabras alfabéticamente)")
