class Animal: # Herencia
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya   
    def saludo(self):
        print('Hola!, soy un', self.tipo, 'y mi sonido es el', self.onomatopeya)

class Gato(Animal):
    tipo = 'gato'
    def __init__(self, nombre, onomatopeya):
        Animal.__init__(self, nombre, onomatopeya)
        print('Hola, soy un gato extendido xd')
     
class Perro(Animal):
    tipo = 'perro'
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print('Instanciando un perro :v')
        
class Canario(Animal):
    tipo = 'canario'
    
class Vaca(Animal):
    tipo = 'vaca'    
                       
gato = Gato('Kitty', 'Miau')            
gato.saludo()

perro = Perro('Coquito', 'Guau')
perro.saludo()

canario = Canario('Piolin', 'silvido')
canario.saludo()

vaca = Vaca('Lola', 'Muu xd')
vaca.saludo()