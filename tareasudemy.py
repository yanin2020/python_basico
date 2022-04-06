# multiplicar dos números sin usar el símbolo de multiplicación
a = 4
b = 8
resultado = 0

for x in range(a):
    resultado += b
    
print('El resultado es :', resultado)
    
# Ingresar nombre y apellido e imprimirlo al revés
nombre = 'Vanesa' 
apellido = 'Mercedes'

concatenacion = nombre + ' ' + apellido

print(concatenacion[::-1])

# Escribir una función que encuentre el elemento menor de una lista
lista = [1, 2, 3, 55, -45, 8, -76]

menor = 'init'

for x in lista:
    if menor == 'init':
        menor = x
    else:
        menor = x if x < menor else menor
        
print('El número menor es:', menor)        

# Escribir una función que devuelva el volumen de una esfera por su radio
# 4/3 * pi * r ** 3
def calculaVolumen(r):
    return 4 / 3 * 3.14 * r ** 3

resultado = calculaVolumen(6)

print('El resultado es:', resultado)

# Escribir una función que indique si el usuario es mayor de edad
def esMayor(usuario):
    return usuario.edad > 17

class Usuario:
    def __init__(self, edad): 
        self.edad = edad
        
usuario = Usuario(15)        
usuario2 = Usuario(20)

resultado1 = esMayor(usuario)
resultado2 = esMayor(usuario2)

print(resultado1, resultado2)

# Escribir una función que indique si un número es par o impar
def esPar(n):
    return n % 2 == 0

resultado = esPar(10)
print('El número es:', resultado)

# Escribir una función que indique cuantas vocales tiene una palabra 
palabra = 'Esternomastoydeo'
vocales = 0
for x in palabra:
    y = x.lower()
    vocales += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' else 0

print('La palabra tiene:', vocales, 'vocales xd')

# Escribir una aplicación que reciba una cantidad infinita de números hasta
# decir basta, luego que devuelva la suma de los dos números ingresados
lista = []
print('Ingrese números y para salir escriba "basta"')
while True:
    valor = input('Ingrese valor: ')
    if valor == 'basta':
        break
    else:
        try:
            valor = int(valor)
            lista.append(valor)
        except:
            print('Dato inválido :/')
            exit()
            
resultado = 0
for x in lista:
    resultado += x
    
print(resultado)                    

