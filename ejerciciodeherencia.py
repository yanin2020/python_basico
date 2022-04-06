# Ejercicio de Herencia y clase

class Gato:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
        
    def saludo(self):
        print('Hola!, soy un gato y mi sonido es el', self.onomatopeya)

class Perro:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
        
    def saludo(self):
        print('Hola!, soy un perro y mi sonido es el', self.onomatopeya)
               
gato = Gato('Kitty', 'Miau')            
gato.saludo()

perro = Perro('Coquito', 'Guau')
perro.saludo()
