from Clases.Usuario import *
from Clases.Direccion import *
from Clases.Fecha import *

nombre = input("Introduce tu nombre: ")
id_usuario = input("Introduce tu ID: ")
dia, mes , año = Fecha(input("Introduce tu fecha de nacimiento"))
ciudad_nacimiento = input("Introduce tu ciudad de nacimiento: ")
telefono = input("Introduce tu teléfono: ")
email = input("Introduce tu email: ")
direccion = Direccion(input("Introduce tu dirreción: "))

Us_new = Usuario(nombre, id_usuario, dia, mes, año, ciudad_nacimiento, telefono, email, direccion)
print(Us_new)
