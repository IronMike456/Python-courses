from math import sqrt # Solo manda a llamar a sqrt
# from math import * --> manda a llamar toda la libreria
# import math --> tienes que referenciar math.cos()
a = int(input("Ingresa a: "))
b = int(input("Ingresa b: "))
c = int(input("Ingresa c: "))
def calculo(a, b, c):
    discriminante = (b**2) - (4*a*c)
    if(discriminante < 0):
        print('La ecuacion no tiene soluciones reales')
        return None
    elif(discriminante == 0):
        x= -b/(2*a)
        return x
    else: 
        x1 = (-b - sqrt(discriminante))/(2*a)
        x2 = (-b + sqrt(discriminante))/(2*a)
        return x1, x2
    #print('Las dos soluciones reales son: ')
    #print(x1)
    #print(x2)

print(calculo(a,b,c))