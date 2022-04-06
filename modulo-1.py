import modulos as papasfritas
from camelcase import CamelCase

print(papasfritas.mascotas)
papasfritas.saludo('Valentina')

c = CamelCase()
s = 'Esta oración necesita CamelCase!'

camelcased = c.hump(s)
print(camelcased)