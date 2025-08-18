#En tu archivo main deberás:
#Crear una variable llamada gustoHelado para guardar el gusto de helado ingresado por el usuario.
#Crear una estructura condicional que evalúe y compare la respuesta con cuatro gustos chocolate, vainilla, fresa y pistacho. Para esto deberás usar los condicionales if, elif y else.
#Si se cumple alguna de las condiciones, mostrar por consola el texto “Sí, hay _____” (concatenar el sabor del usuario).
#En caso de que el gusto no exista, mostrar por consola el texto “No hay _____” (concatenar el sabor del usuario).

gustoHelado = input("ingresa tu gusto favorito")
if gustoHelado == "chocolate":
  print("Sí, hay "+gustoHelado)
elif gustoHelado == "fresa":
  print("Sí, hay "+gustoHelado)
elif gustoHelado == "pistacho":
  print("Sí, hay "+gustoHelado)
elif gustoHelado == "vainilla":
  print("Sí, hay " +gustoHelado)
else:
  print("No hay "+gustoHelado)
