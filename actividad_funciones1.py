def calcular_densidad(masa, volumen):
  return masa/volumen

densidad1 = calcular_densidad(10, 2)
print(densidad1)

densidad2 = calcular_densidad(270, 33)
print(densidad2)
print("La densidad total es: " + str(densidad1 + densidad2))
