a = int(input("Ingresa a: "))
b = int(input("Ingresa b: "))
c = int(input("Ingresa c: "))
from math import sqrt # Solo manda a llamar a sqrt
# from math import * --> manda a llamar toda la libreria
# import math --> tienes que referenciar math.cos()


discriminante = (b**2) - (4*a*c)

if(discriminante < 0):
    print('La ecuacion no tiene soluciones reales')
elif(discriminante == 0):
    x= -b/(2*a)
    print('La solucion unica es: ', x)
else: 
    x1 = (-b - sqrt(discriminante))/(2*a)
    x2 = (-b + sqrt(discriminante))/(2*a)
    print('Las dos soluciones reales son: ')
    print(x1)
    print(x2)

