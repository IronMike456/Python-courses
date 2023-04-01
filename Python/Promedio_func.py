def promedio(notas,nombreAsig):
    suma = 0
    for notita in notas: 
        suma += notita 
    r = suma/len(notas) 
    return r, nombreAsig

print(promedio([2,2,2,3,2,4], "Programacion"))

def promedio(notas,nombreAsig):
    suma = 0
    for notita in notas: 
        suma += notita 
    r = suma/len(notas) 
    return "El primedio es: " + str(r) + " De la asginatura " + nombreAsig

print(promedio([2,2,2,3,2,4], "Programacion"))

