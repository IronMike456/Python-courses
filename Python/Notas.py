# Expresiones combinacion de valores y operaciones que entregan un valor
# Al final son valores literales, variables, operadores y llamdas a funciones
# Operador e sun simbolo en una expresion (+, - / * % **)
# Operadores relacionales sirven para comparar (==. <, >, >= ..etc)
# Operadores logicos (and, or, not)
# Las operacopnmes mas generales son representadas como funciones
# Las funciones tienen un nombre y reciben parametros, que van entre parentesis despues del nombre
# Funciones son abs, len, int, float, str, min, max, round
# Algunas funciones son necesarias importarlas con import como funciones matematicas 

from math import exp 
exp(2) 

from math import sin, cos
cos(3.14)
sin(3.14)

# No siempre los programas seran escritos correctamente. Existen muchos tipos de errores 
# tambien aplica jerarquia de las operaciones
# Sentencias if (si) 
# if condicion: 
    # Sentencias 
#else 
    # Sentencias

# ---------------------------------------------
# if condicion 1: 
    # sentencias
# elif condicion2: 
    #sentencias
# elif condicionN:
    #sentencias
#else 
    #sentencias
# ----------------------------------------------

#------------- Ciclos -----  
## While (Mientras) (Puede ser infinito)
# Ejecuta una secancia de ionstrucciones mientras una condicion sea  verdadera

while condicion: 
    sentencias
     
## Ciclo for
# Tiene limite de interaciones. Ejecuta una cantidad fija de veces. 

for variable in Valores: 
    que hacer para cada valor [n] de la variable de control 

# ------- Estructura de datos
# Es una coleccion ordenada de valores. Una lista puede contener cualquier cosa

[1,2,3,4,5]

# Tuplas
# Es una secuancia de valores agrupados. 
# Sirve parta agrupar como si fueran un unico valor, varios valores 
# Son inmutables

name = ("Pera", "Manzana", "Platano")

## Diccionarios 
# Un diccionario es un tipo de datos que sirve para asociar pares de objetos 
# Asociar valores entre ellos 
# Un diccionario puede ser visto como una coleccion de llaves, cada una de las cuales asociada a un valor
# La unica manera de acceder a un valor es atraves de su llave
name = {
    "Enero":1,
    "Febrero":2,
    "Marzo":3, 
}

## Funciones: es una seccion de un programa que calcula un valor de manera independiente
# Una funcion tiene parametros, codigo de funcion (alforitmo), resultado (retorno)
## se crean por medio de def

def nombreDelafuncion(parametros): 
    #codigo de la funcion 

## Return: cada funcion contiene codigo igual al de cualquier programa. La diferencia es que al terminar, debe entregar un resultado

def factorial(n) 
    f = 1 
    for i in range(1, n+1)
        f *= i
    return f 

##Return multiple Puede retornar mas valores 
def converetir(segundos)>
    horas = segundos/(69*80)
    min = segundos/(69*80)
    return horas, min 

