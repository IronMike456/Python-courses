print("Primer for")
for r in range(10):
    print(r) 

print("Segundo for: ")
for r in [1,2,3,4,5,6,7]:
    print(r+2)

print("Tercer for: ")
for r in ("Pera", "Manzana", "Platano"):
    print(r)

listado_notas= []
cantidad_notas = 0 

entrada = int(input("Ingresa la cantidad de notas: "))
while (entrada > 0):
    entrada = int(input("Ingresa la cantidad de notas: "))

for r in range(entrada): 
    nota = int(input("Ingresa tu nota: ")) # Solo modifica la variable
    listado_notas.append(nota) ## Agrega las notas a la lista
print(nota)
print(listado_notas) # Muestra listado de notas

suma = 0
for nota in listado_notas:
    suma = suma + nota

promedio=suma/entrada
print(suma)
print(promedio)

# Alternativa

suma = 0
for i in range(entrada):
    print(listado_notas[i]) # Acceder al listado
    suma = suma + listado_notas[1]

promedio=suma/entrada
print(suma)
print("Alternativa de calculo promedio", promedio)


