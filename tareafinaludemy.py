# Escribir una función que reciba nombre y apellido y los que vaya agregando a 
# un archivo
def agregarNombreAArchivo(nombre, apellido):
    c = open('nombrecompleto.txt', 'a')
    c.write(nombre + ' ' + apellido + '\n')
    c.close()
    
agregarNombreAArchivo('Valentina', 'Hernandez')    
    