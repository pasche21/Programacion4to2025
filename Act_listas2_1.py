#En tu archivo main:
#Crear una variable con el nombre puntajes con una lista vacía.
#Agregar a la lista los puntajes 1000, 920, 830, 750 y 670 de mayor a menor utilizando el método correspondiente.
#Quitar de la lista los puntajes 920, 830 y 750 utilizando el método correspondiente.
#Crear una variable llamada contador, con un valor igual a 0 para usar como contador.
#Utilizar un input() con el texto "Por favor indique la cantidad de puntajes a ingresar" y guardar el valor de su respuesta en una variable llamada cantidadPuntajes.
#Crear un bucle while para verificar que el valor de cantidadPuntajes sea un número.
#Ejecute un input() con el texto "Por favor indique la cantidad de puntajes a ingresar" y guarde el valor de su respuesta en la variable llamada cantidadPuntajes.
#Crear otro bucle while para que se ejecute mientras contador sea menor a cantidadPuntajes.
#Dentro del while:
#Incrementar contador en 1.
#Crear una variable puntaje con input() para almacenar el valor ingresado.
#Agregar el puntaje a la lista y convertirlo a int.
#Mostrar por consola el texto "Los mejores puntajes son:".
#Realizar un print() de la lista.
#Pistas

puntajes = []
puntajes.append(1000)
puntajes.append(920)
puntajes.append(830)
puntajes.append(750)
puntajes.append(670)

puntajes.remove(920)
puntajes.remove(830)
puntajes.remove(750)

contador = 0

cantidadPuntajes = input("Por favor indique la cantidad de puntajes a ingresar")

while not cantidadPuntajes.isdigit():
  cantidadPuntajes = input("Por favor indique la cantidad de puntajes a ingresar")

while contador < int(cantidadPuntajes):
  contador += 1
  puntaje = input("Indicar valor del puntaje: ")
  puntajes.append(int(puntaje))
  
print("Los mejores puntajes son:")
print(puntajes)


