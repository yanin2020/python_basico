# Objetos y clases :v

class Usuario: 
    nombre = 'Maria'
    apellido = "Jesus"
    
usuario = Usuario()

# print(usuario.nombre, usuario.apellido)

# Métodos
class Usuario:
  def __init__(self, nombre, apellido):
      self.nombre = nombre
      self.apellido = apellido
      
usuario = Usuario('Valentina', 'Quintero')
usuario2 = Usuario('Maria', 'Jesus')

# print(usuario.nombre, usuario.apellido, usuario2.nombre, usuario2.apellido) 

# class Usuario:
    # def __init__(self, nombre, apellido):
      # self.nombre = nombre
      # self.apellido = apellido
      
    # def saludo(self):
        # print('Hola :D!!, mi nombre es', self.nombre, self.apellido)
          
# usuario = Usuario('Valentina', 'Quintero')
# usuario2 = Usuario('Maria', 'Jesus')

# usuario.saludo()
# usuario2.saludo() 

# Self,eliminar propiedades y objetos :)
class Usuario:
    def __init__(self, nombre, apellido):
      self.nombre = nombre
      self.apellido = apellido
      
    def saludo(self):
        print('Hola :D!!, mi nombre es', self.nombre, self.apellido)

class Admin(Usuario): # Herencia
    def superSaludo(self):
        print('Hola!!, me llamo,', self.nombre, 'y soy administrador de la web :D')
         
usuario = Usuario('Valentina', 'Quintero')

# usuario.saludo()
usuario.nombre = 'Maria'
# usuario.saludo()
# del usuario.nombre
# del usuario # Si borro el objeto no estará definida y dará error
# print(usuario) 

admin = Admin('Valentina', 'Quintero')
admin.saludo()
admin.superSaludo()

# usuario.superSaludo()




                               