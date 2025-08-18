puntos_vida_dragon = 100
import random 
# LA MEGA FUNCION
def tirarDado (lados):
  return random.randint(1,lados)
# ATAQUE
def atacarDragon():
  ataque = tirarDado(20)+tirarDado(4)
  return ataque
# NO SE
puntos_vida_dragon = puntos_vida_dragon - atacarDragon()
# FIN