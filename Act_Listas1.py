#En tu archivo main deberás:
#Obtener la suma de las notas de la lista, almacenar el resultado en una variable llamada sumaNotas y mostrarlo por consola con el texto “La suma de las notas es: _____”.
#Obtener la cantidad de las notas de la lista, almacenar el resultado en una variable llamada cantidadNotas y mostrarlo por consola con el texto “La cantidad de notas es: _____”.
#Crea una variable llamada  promedio y almacenar el promedio de las notas para mostrarlo por consola con el texto “El promedio de las notas es: _____”

notas = [10, 4, 6, 5, 10, 8, 9, 4]

sumaNotas = sum(notas)
print("La suma de las notas es:" + str(sumaNotas))

cantidadNotas = len(notas)
print("La cantidad de notas es:" + str(cantidadNotas))

promedio = sumaNotas/cantidadNotas
print("El promedio de las notas es:" + str(promedio))
