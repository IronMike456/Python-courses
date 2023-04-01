v1 = 2 
v2 = 3
v3 = 2
v4 = -4
cadena = "Huawei is not the best"
resultado = ("El resultado es: ", v1 == v2)
print(resultado) #False

resultado2 = ("El resultado es: ", v1 == v3)
print(resultado2) #True

resultado3 = ("El resultado es: ", v1 <= v2)
print(resultado3) 

resultado4 = ("El resultado es: ", v1 >= v2)
print(resultado4) 

resultadoand = (resultado and resultado2)
print(resultadoand)

resultadonot = (not resultado2)
print(resultadonot)

resultadolen = len(cadena)
print(resultadolen)

resultadoabs = abs(v4)
print(resultadoabs)

