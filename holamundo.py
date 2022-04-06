#print('hola mundo')
#print('aguacato')
#print (2+5)
#como identar en python
#if 3 > 5:
   # print('Esto no se va a ejecutar')
x = 4
y = 'Pancho comestible'
#print(x, y) 
a, b, c = 'Pan','Panchito','Pancito'
#print(a, b, c) 
valor1 = valor2 = valor3 = 'Aguacate'
#print(valor1, valor2, valor3)
inicio = 'Agua'
final = 'cate'
#print(inicio + final) 

palabra = 'Tortuga' #string
oracion = 'Pan que no tiene harina xd' # string
entero = 20 # interger
conDecimales = 20.3 # float
complejo = 1j 
#print(palabra, oracion, entero, conDecimales, complejo)
#ejemplo de lista con días de la semana
lista = ['lunes', 'martes', 'miércoles']
lista2 = lista.copy() # método para copiar listas
lista.append('jueves')
#lista.clear() # Método para vaciar listas
# print(lista, lista2.count('jueves')) # método para contar cuantos elementos de lista tienen el strin jueves
# print(len(lista), len(lista2)) # imprime 4 que son elementos que tiene la lista y 3 que tiene lista2
# print(lista[0]) # En la lista se comienza en cero el índice

# lista.pop() # Elimina el último elemento de la lista
# lista.remove('martes') # Elimina el índice que elijamos
# lista.reverse() # Voltea la lista
# lista.sort() # Ordena la lista solo con datos del mismo tipo
tupla = ('una', 'vaca', 'sin', 'cola', 'vaca')
# print(tupla.count('vaca')) # Método count en tupla, las tuplas llevan parentesís y no se pueden modificar
# print(tupla.index('vaca')) # Muestra el índice del elemento en este caso tenemos 2 índices en vaca
listaDeTupla = list(tupla)
listaDeTupla.append('gatito feliz')
# print(listaDeTupla)
rango = range(6)
# print(rango)

diccionario = {
   'nombre': 'kitty',
   'raza': 'siames',
   'edad': 7
}
# print(diccionario.get('nombre')) # Método get para obtener valores
diccionario['nombre'] = 'Pelusa' # Forma de cambiar el valor
# print(len(diccionario)) # Método len para saber cuantos elementos tiene el diccionario
diccionario['ronronea?'] = 'Si'
# print(diccionario)
diccionario.pop('ronronea?') # Método pop para eliminar elementos
# print(diccionario)
copiaGatito = diccionario.copy() # Crea un clon
copiaGatito = dict(diccionario) # También hace un clon
diccionario.clear() # Vacia el diccionario
# print(diccionario, copiaGatito)
gatitos = {
   "Kitty":{
   "nombre": "Kitty",
   "edad": 7
},
"Mamba": {
 "nombre": "Black Mamba",
 "edad": 12     
}
}
# print(gatitos)

perritos = dict(nombre="Coquito", edad=6)
# print(perritos) # Diccionario anidados

verdadero = True # Valores booleanos
falso = False
# print(verdadero, falso)

# if y condicionales
# if 2 < 5:
  # print('2 es menor que 5')

# a == b
# a < b
# a > b
# a != b
# a <= b
# a >= b

# if 2 == 2:
  # print('2 es igual a 2')
   
# if 2 == 3:
  # print('2 es igual a 3')
   
# if 2 > 5:
  # print('2 es mayor a 5')
   
# if 5 > 2:
  # print('5 es mayor a 2')
   
# if 2 != 2:
  # print('2 es distinto a 2')
   
# if 3 == 2:
  # print('3 es distinto a 2')
   
# if 3 >= 2:
  # print('3 es mayor o igual a 2')
   
# if 3 != 3:
  # print('3 es menor o igual a 3')                     

# Condicionales if, elif, y else
if 2 > 5:
   print('dos es menor a 5 en if')
elif 2 > 5:
   print('2 menor a 5 en elif')
elif 2 < 5:
   print('2 menor a 5 en segundo elif')
else:
   print('yo no imprimo solo si todo lo anterior evalua en falso')         
   
if 2 > 5:
   print('dos es menor a 5 en if')
else:
   print('yo no imprimo solo si todo lo anterior evalua en falso 2')         
      
# If cortos y ternarios
if 2 < 5: print('if de una línea')

# print('cuando devuelve true') if 5 > 2 else print('cuando devuelve false')
      
# And y or
if 2 < 5 and 3 > 2:
   print('ambas devuelven true')      
if 2 < 5 and 3 < 2: # Si una condición evalua en true se ejecuta la intrucción
   print('Hay una falsa, esto no se mostrará')
   
if 1 < 0 and 1 < 0: # Si ambas condiciones son falsas entonces no se ejecuta
   print('Si ambas condiciones evaluan en false no se ejecuta esto')                  