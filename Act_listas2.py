#En tu archivo main deberás:
#Utilizar la técnica correspondiente para extraer los animales salvajes de la lista y almacenarlos en una variable llamada animalesSalvajes. Luego, deberás ordenar la nueva lista por orden alfabético utilizando el método apropiado.
#Utilizar la técnica correspondiente para extraer los animales domésticos de la lista y almacenarlos en una variable llamada animalesDomesticos. Luego, deberás ordenar la lista por orden alfabético utilizando el método apropiado.
#Mostrar por consola las variables animalesSalvajes y animalesDomesticos.

animales = ["Avestruz", "León", "Elefante", "Gorila", "Ballenas", "Caballo", "Gallina", "Hámster", "Perro", "Gato"]

# Clasificación manual según si son salvajes o domésticos
animalesSalvajes = animales[0:5]
animalesDomesticos = animales[5:]

# Ordenar las listas en orden alfabético
animalesSalvajes.sort()
animalesDomesticos.sort()

# Mostrar resultados por consola
print(animalesSalvajes)
print(animalesDomesticos)
