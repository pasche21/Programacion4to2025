#En tu archivo main deberás:
#Obtener el puntaje mínimo de la lista, almacenarlo en una variable llamada minimo y luego mostrar su valor por consola.
#Obtener el puntaje máximo de la lista, almacenarlo en una variable llamada maximo y luego mostrar su valor por consola.
#Obtener el puntaje promedio de la lista, almacenarlo en una variable  llamada promedio y luego mostrar su valor por consola.
#Para calcular el promedio, deberás utilizar los métodos sum() y len() sobre la lista de puntajes para obtener los valores necesarios para la operación matemática.
#Invertir el orden de los puntajes de la lista usando el método necesario y realizar un print() de la lista.
#Ordenar los puntajes de la lista de menor a mayor usando el método necesario para hacerlo de forma automática.
#Mostrar por consola el texto "El TOP SCORE final es: " y debajo realizar un print() de la lista.

puntajes = [850, 920, 670, 750, 830, 1000]

minimo = min(puntajes)
print(minimo)

maximo = max(puntajes)
print(maximo)

promedio = sum(puntajes) / len(puntajes)
print(promedio)

puntajes.reverse()
print( puntajes)

puntajes.sort()
print( puntajes)

print("El TOP SCORE final es:")
print(puntajes)
