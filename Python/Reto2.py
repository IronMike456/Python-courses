from collections import Counter  
Correo = input("Ingrese un correo correcto: ")
dominios = []

while(len(Correo) != 0): 
    if '@' in Correo and '.' in Correo and any(chr.isdigit() for chr in Correo): ## Validar que el correo contenga @, punto y numeros
        print("Correo: ", Correo, " es valido")
        desdearroba = Correo.index('@') # toma la posicion del '@'
        hastapunto = Correo.index('.') # Toma la posicion del primer '.'
        dominio =  Correo[desdearroba+1:hastapunto] # Imprime despues del arroba hasta el primer punto
        print(dominio) 
        dominios.append(dominio) #Guarda lo impreso en un array
        Correo = input("Ingrese un correo correcto: ")
    else: 
        print("Correo: ", Correo, " es invalido") 
        Correo = input("Ingrese un correo correcto: ")

print("Los dominios son: ", dominios)

conteo=Counter(dominios) # Libreria que cuenta el numero de repeticiones
resultado={} # Diccionario que guardara el conteo
for clave in conteo:   # For para la asignacion de claves en el conteo de los dominios
    valor=conteo[clave] #Asigna segun el conteo un valor al directorio
    resultado[clave] = valor # Guarda en el directorio 

print(resultado)



