

import math

def calcular_velocidad_final(velocidad_inicial,aceleracion,tiempo):
    velocidad_final=velocidad_inicial+(aceleracion*tiempo)
    return velocidad_final

def calcular_distancia_recorrida(velocidad_inicial,aceleracion,tiempo):
    distancia_recorrida= (velocidad_inicial*tiempo)+(0.5*aceleracion*tiempo**2)
    return distancia_recorrida

#obtener los valores que se requieran

velocidad_inicial=float(input(" ingresar la velocidad inicial en m/s : "))

aceleracion=float(input(" ingresar los valores de la aceleracion en m/s2 : "))

tiempo=float(input( " ingresar los valores del tiempo en segundos : "))

# calcular la velocidad final u la distancia recorrida 

velocidad_final=calcular_velocidad_final(velocidad_inicial, aceleracion,tiempo)
distancia_recorrida=calcular_distancia_recorrida(velocidad_inicial,aceleracion,tiempo)

#imprimir los resultados obtenidos de la velocidad final y la distancia recorrida
print(" velocidad final : ", velocidad_final, "m/s")
print( " distancia recorrida", distancia_recorrida, "metros")


