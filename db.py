import mysql.connector

midb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'gato'
)

cursor = midb.cursor()

# Listar datos
# cursor.execute('select * from adopcion')
# resultado = cursor.fetchall()
# print(resultado)

# Limitar datos
cursor.execute('select * from adopcion limit 2')
resultado = cursor.fetchall()
print(resultado)

# Ver definiciones de tablas
# cursor.execute('show create table adopcion')

# Insertar datos
# sql = 'insert into adopcion (nombregato, raza, edad, telefono) values (%s, %s, %s, %s)'
# values = ('Garfield', 'persa', 10, 2125743301)

# Inserta datos
# sql = 'update adopcion set edad = %s where id = %s'
# values = (7, 8)
# cursor.execute(sql, values)

# midb.commit()

# print(cursor.rowcount)

# Eliminar datos
# sql = 'delete from adopcion where id = %s'
# values = (8,)
# cursor.execute(sql, values)
# midb.commit()