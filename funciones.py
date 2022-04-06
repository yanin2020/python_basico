# Funciones         
        
def miFuncion():
    print('Mi primera función :D !!')
    
# miFuncion()

# def imprimeDato(argumentoUno):
    # print('Mi argumento es', argumentoUno)
    
# imprimeDato('parametro 1')

# def imprimeDato(nombre, apellido):
    # print('El nombre completo es:', nombre, apellido)
    
# imprimeDato('Valentina', 'Quintero')  
         
# def imprimeDato(*nombre): # Para definir multiples parametros con un *
    # print('El nombre completo es:', nombre)
    
# imprimeDato('Valentina', 'Kevin', 'Hiroshi', 'Javier')

# def nombreCompleto(apellido, nombre): # No importa el orden 
   # print(nombre, apellido)
    
# nombreCompleto(nombre= 'Valentina', apellido='Quintero')

# def nombreCompleto(**kwargs):  
  # print(kwargs['nombre'], kwargs['apellido'])

# nombreCompleto(nombre= 'Valentina', apellido='Quintero')

# Imprimir listas con funciones

# def miFuncion2(argumento = 'Aguacate'):
    # print(argumento)
    
# miFuncion2('Vaquita')
# miFuncion2()    
 
def miFuncionLista(lista):
     for el in lista:
        print(el)   
    
# miFuncionLista(['Valentina', 'Quintero']) 

def concatenaNombres(lista):
    i = ''
    for el in lista:
        i = i + el + ' '
    return i 

# nombres = concatenaNombres(['Valentina', 'Quintero']) 
# print(nombres)  
  
def recursion(i):
    if(i < 1):
        return i
    print(i)
    recursion(i - 1)
    
recursion(6)                                                                 