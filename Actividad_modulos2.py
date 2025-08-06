import datetime

ahora = datetime.datetime.now()
print(ahora)

fecha = datetime.datetime(2003, 10, 2)
print(fecha)

diferencia = ahora - fecha
print(diferencia)

diferenciaEnDias = diferencia.days
print(diferenciaEnDias)

anios = diferenciaEnDias / 365
print(anios)

print("Tengo " + str(int(anios)) + " años")
