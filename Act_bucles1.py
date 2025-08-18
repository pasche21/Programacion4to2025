#En tu archivo main deberás:
#Importar la función randint del módulo random.
#Crear las siguientes variables con el valor 0:
#dado para guardar el número que salió en una tirada.
#contador para guardar la cantidad de tiradas.
#puntaje para acumular la suma de los dados.
#Crear un bucle while que se ejecute mientras contador sea menor a 10 y puntaje sea menor a 38.
#dentro del while:
#Guardar en la variable llamada dado el resultado de la función randint(1, 6).
#Hacer un print() de dado.
#Almacenar en la variable llamada puntaje la suma de los dados lanzados.
#Incrementar la variable llamada contador de uno en uno.
#Mostrar por consola el texto “El puntaje total es: _____”.
#Crear una estructura condicional para que, si el valor de puntaje es mayor o igual a 38, se muestre por consola el texto “Ganaste”; si es menor, que se muestre el mensaje “Perdiste”.

from random import randint
dado = 0
contador = 0
puntaje = 0

while contador < 10 and puntaje < 38:
  dado = randint(1, 6)
  print(dado)
  puntaje += dado
  contador += 1
print("El puntaje total es: "+str(puntaje))
if puntaje >= 38:
    print("Ganaste")
else:
    print("Perdiste")
    