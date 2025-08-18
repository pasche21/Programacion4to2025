#En tu archivo main deberás:
#Crear una variable llamada auto1 y, dentro de ella, guardar un diccionario con al menos tres propiedades (color, cantidad_puertas, marca).
#Repetir el paso anterior, pero replicando la estructura de datos para las variables auto2, auto3 y auto4.
#A través de la notación de corchetes, modificar el color del auto2 y luego mostrarlo por consola.

auto1 = {
    "color": "Rojo",
    "cantidad_puertas": 4,
    "marca": "Toyota"
}

auto2 = {
    "color": "Rojo",
    "cantidad_puertas": 2,
    "marca": "Ford"
}

auto3 = {
    "color": "Blanco",
    "cantidad_puertas": 4,
    "marca": "Chevrolet"
}

auto4 = {
    "color": "Negro",
    "cantidad_puertas": 5,
    "marca": "Honda"
}


auto2["color"] = "Verde"

print(auto2["color"])