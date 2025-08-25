#En tu archivo main deberás:
#Crear una variable llamada jugadores que contenga una lista vacía.
#Crear una variable llamada contador que contenga el número 1.
#Utilizar un bucle while que se repita siempre que contador sea menor o igual a 3 y que dentro de este:
#Solicitar al usuario mediante el uso de input() que se ingrese el nombre, apellido, edad, club1 y club2, y almacenar dichos resultados en 5 variables que posean los respectivos nombres.
#Deberás modificar cada mensaje de input() para concatenar la variable contador al mensaje y generar un resultado dinámico. Ejemplo: nombre = input("Ingrese el nombre del jugador ____")
#Luego de generar las 5 variables, se deberá almacenar la información solicitada en un diccionario llamado jugador. Ejemplo: deportes = {"nombre" : ___}
#Agregar el diccionario a la lista jugadores, utilizando el método necesario.
#Incrementar el valor de la variable contador en uno
#Mediante el uso de un bucle for, recorrer la lista jugadores y mostrar los datos de cada uno.
#Crear una variable llamada indice con valor inicial 1 e incrementarla dentro del bucle.
#Importante: Usar jugador como nombre de la variable del bucle for (no usar i ni otros nombres genéricos).
#Utilizar print() con concatenación (+) para mostrar la información de cada jugador en una sola línea de código, con el siguiente formato:
#"Los datos del jugador 1 son: Nombre Apellido, Edad: __, Clubes: Club1 y Club2"

jugadores = []

contador = 1

while contador <= 3:
    nombre = input("Ingrese el nombre del jugador " + str(contador) + ": ")
    apellido = input("Ingrese el apellido del jugador " + str(contador) + ": ")
    edad = input("Ingrese la edad del jugador " + str(contador) + ": ")
    club1 = input("Ingrese el primer club del jugador " + str(contador) + ": ")
    club2 = input("Ingrese el segundo club del jugador " + str(contador) + ": ")

    jugador = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "club1": club1,
        "club2": club2
    }

    jugadores.append(jugador)

    
    contador += 1

indice = 1
for jugador in jugadores:
    print("Los datos del jugador " + str(indice) + " son: " +
          jugador["nombre"] + " " + jugador["apellido"] +
          ", Edad: " + jugador["edad"] +
          ", Clubes: " + jugador["club1"] + " y " + jugador["club2"])
    indice += 1