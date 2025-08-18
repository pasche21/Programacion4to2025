#En tu archivo main:
#Cambiar los siguientes elementos:
#“Patata” por “Fresa”
#“Tomate” por “Manzana”
#“Cebolla” por “Durazno”
#Ordenar la lista por orden alfabético.
#Mostrar por consola la lista modificada.
#Crear una condición para verificar si “maracuyá” se encuentra en la lista de frutas.
#Si la condición se cumple, mostrar por consola “Sí, hay maracuyá”; en caso de que no, mostrar “No hay maracuyá”.
#Invertir el orden de la lista y mostrar por consola la lista modificada.

frutas = ["pistacho", "Mandarina", "Patata", "Naranja", "Pomelo", "Coco", "Tomate", "Kiwi", "Mango", "Cebolla"]

frutas[2]="Fresa"
frutas[6]="Manzana"
frutas[9]="Durazno"
frutas.sort()
print(frutas)



if "maracuyá" in frutas:
  print("Sí, hay maracuyá")
else:
  print("No hay maracuyá")

frutas.reverse()
print(frutas)
