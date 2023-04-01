def valida_correo(entrada):
    if(entrada.count('@')>0):
        separo = entrada.split('@')
        if(separo[1].count('.')>0):
            separo_punto = separo[-1].split('.')
            if(separo[1].count('.')>1): 
                return(separo_punto[0]+'.'+separo[1]), True
            else: 
                return separo_punto[0], True
        else: 
            print('Correo mal ingresado, falta punto')
            return('falta el punto'), False
    else: 
        print('Correo mal ingresado falta el @')
        return ('falta el @'), False

def lista_de_correos():
    correo = ""
    correo = input("ingrese correeo: ")
    lista_correo = []
    while(correo!=""):
        lista_correo.append(correo)
        correo = input 
    return lista_correo

def lista_dominios():
    lista_dom=[]
    lista = lista_de_correos()
    for correo in lista:
        if(valida_correo(correo)[1]):
            lista_dom.append(valida_correo(correo)[0])
    return lista_dom

def main():
    contador = 0
    dominios = lista_dominios()
    diccionario = dict()
    for palabra in dominios: 
        if palabra in diccionario:
            diccionario[palabra] += 1
        else: 
            diccionario[palabra] = 1
    print(dominios)
    print(diccionario)

main()





