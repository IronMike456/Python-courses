
x=3
while x>=0: 
    a_input = input("Ingresa un numero, una minuscula o Mayuscula: ")
    if(a_input.isnumeric() == True): 
        print("Es numero")
    elif(a_input.isupper() == True ): 
        print("Es mayuscula")
    elif(a_input.islower() == True):
        print("Es minuscula") 
    else:  
        print("No es numero ni letra")


