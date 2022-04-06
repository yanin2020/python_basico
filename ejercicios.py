# dato = input('Ingrese dato: ')
# print(dato)
# lista = ['aguacate', 'tortuga', 'kitty', 'drones']

# if lista.count(dato) > 0:
    # print('El dato existe :)', dato)
# else:
    # print('El dato no existe :(', dato)  
    
# Calculadora sencilla
# primero = input('Ingrese primer número: ')
# segundo = input('Ingrese segundo número: ')      
# primerNumero = int(primero)
# segundoNumero = int(segundo)
# print(primerNumero + segundoNumero)

# Calculadora que convierte string a número usando try y except
primero = input('Ingrese primer número: ')

try:
    primero = int(primero)
except:
    primero = 'Vaca sin cola'
    
if primero == 'Vaca sin cola':
    print('El valor ingresado no es un entero :/')    
    exit()
        
segundo = input('Ingrese segundo número: ') 

try:
    segundo = int(segundo)
except:
    segundo = 'Vaca sin cola'

if segundo == 'Vaca sin cola':
    print('El valor ingresado no es un entero :/')    
    exit()
        
# if primero == 'Vaca sin cola' or segundo == 'Vaca sin cola':
   # print('Escribiste mal un dato, prueba de nuevo solo con números xd')    
# else:
# print(primero + segundo)

simbolo = input('Ingrese operación: ')

if simbolo == '+':
    print('Suma', primero + segundo)
elif simbolo == '-':
    print('Resta', primero - segundo)
elif simbolo == '*':
    print('Multiplicación', primero * segundo)
elif simbolo == '/':
    print('División', primero / segundo)
else:
    print('El símbolo ingresado no es válido :/')                