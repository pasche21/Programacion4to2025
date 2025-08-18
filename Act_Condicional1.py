#En tu archivo main:
#Crear una variable llamada edad que guarde la edad del usuario ingresada por consola.
#Crear una estructura condicional que evalúe si el usuario tiene 16 años o más.
#Si la condición se cumple, mostrar por consola el texto “Tienes permitido conducir”.
#En caso de que la condición no se cumpla, mostrar por consola el texto “No tienes permitido conducir”.

edad= int(input("ingresa tu edad"))

if edad >= 16:
  print ("Tienes permitido conducir")
else:
  print ("No tienes permitido conducir")
