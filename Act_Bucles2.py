#En tu archivo main deberás:
#Crear una variable llamada clave y asignarle el valor “DigitalHouse”.
#Crear una variable llamada password y guardar la respuesta del usuario a un input() solicitando que ingrese la contraseña.
#Crear un bucle while que se ejecute mientras clave sea distinto a password.
#Dentro del while:
#Volver a cambiar el valor de la variable password utilizando un input() que muestre un mensaje indicando que hubo un error e invitando al usuario a intentar nuevamente.
#Una vez finalizado el bucle, mostrar por consola el mensaje: La contraseña ingresada es correcta

clave = "DigitalHouse"
password = input("Ingrese la contraseña")

while clave != password:
  password = input("Hubo un error, intente de nuevo con otra contraseña")
print("La contraseña ingresada es correcta")
