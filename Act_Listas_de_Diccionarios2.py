#En tu archivo main, debajo del código brindado, deberás:
#Crear un bucle for para iterar la lista de diccionarios (artistas) utilizando como iterador la clave artista.
#Dentro del bucle for muestra por consola la biografía de cada artista, concatenando toda la información disponible y respetando el siguiente formato:
#Nicole Denise Cucco, (mejor conocida como Nicki Nicole), es una cantante, rapera y compositora de 22 años que nació en Argentina. Sus géneros musicales son el pop, el trap y el hip hop.

artistas = [

 {

  "nombreArtistico": "Lali",

  "carrera": ["actriz", "cantante", "compositora"],

  "nombre": "Mariana Espósito",

  "edad": 31,

  "pais": "Argentina",

  "generoMusical": ["Pop", "Hip hop", "Dance pop"]

 },

 {

  "nombreArtistico": "Taylor Swift",

  "carrera": ["cantante", "compositora", "productora"],

  "nombre": "Taylor Alison Swift",

  "edad": 33,

  "pais": "Estados Unidos",

  "generoMusical": ["Pop", "Country pop", "Folk"]

 },

 {

    "nombreArtistico": "Karol G",

    "carrera": ["cantante", "compositora", "productora"],

    "nombre": "Carolina Giraldo Navarro",

    "edad": 33,

    "pais": "Colombia",

    "generoMusical": ["Reguetón", "Pop urbano", "Trap latino"]

  }

]

for artista in artistas:

  print(artista["nombre"] + ", (mejor conocida como " + artista["nombreArtistico"] + "), es una " + artista["carrera"][0] + ", " + artista["carrera"][1] + " y " + artista["carrera"][2] + " de " + str(artista["edad"]) + " años que nació en " + artista["pais"] + ". Sus géneros musicales son el " + artista["generoMusical"][0] + ", el " + artista["generoMusical"][1] + " y el " + artista["generoMusical"][2] + ".")