 Historia 1
# La historia se sitúa en el pueblo ficticio de Hawkins, en el estado de Indiana, Estados Unidos, durante los años ochenta,
# cuando un niño de doce años llamado Will Byers desaparece misteriosamente.
# Poco después, Eleven, una niña aparentemente fugitiva y con poderes telequinéticos,
# se encuentra con Mike, Dustin y Lucas, amigos de Will, y los ayuda en la búsqueda de su amigo desaparecido.


# Solicitar al usuario cinco palabras nuevas para reemplazar
lugar = input("Escribí un lugar ficticio: ")
estado = input("Escribí el nombre de un estado: ")
nombre_nino = input("Escribí un nombre de niño: ")
nombre_chica = input("Escribí un nombre de niña: ")
sustantivo = input("Escribí un sustantivo relacionado con poderes: ")

# Mostrar un título
print("\n🌟 Tu historia personalizada de ciencia ficción 🌟\n")

# Mostrar la historia con las palabras reemplazadas
print(
    "La historia se sitúa en el pueblo ficticio de " + lugar + ", en el estado de " + estado +
    ", durante los años ochenta, cuando un niño de doce años llamado " + nombre_nino +
    " desaparece misteriosamente.\nPoco después, " + nombre_chica + 
    ", una niña aparentemente fugitiva y con poderes " + sustantivo +
    ", se encuentra con Mike, Dustin y Lucas, amigos de " + nombre_nino +
    ", y los ayuda en la búsqueda de su amigo desaparecido."
)
t