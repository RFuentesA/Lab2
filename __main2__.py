from Clases.Usuario import *
from Clases.Direccion import *
from Clases.Fecha import *

#Pedido por consola literal 5 porque meimprime la direccion en memoria el metodo get de usuario? usu1.getNombre = #en la RAM
print("ingrese sus datos: ")
nombre = input("Ingrese su nombre: ")
id = input("Ingrese su id: ")
ciudadNacimiento = input("Ingrese su ciudad de nacimiento: ")
telefono =input("Ingrese su numero de telefono: ")
email = input("Ingrese su correo electronico: ")
usu1 = Usuario(nombre, id, ciudadNacimiento, telefono, email)
    
print("ingrese su fecha de nacimeinto")
dd = input("Ingrese su dia de nacimiento: ")
mm = input("Ingrese su mes de nacimiento: ")
aa = input("Ingrese el año de nacimiento")
f = Fecha(dd, mm, aa)
usu1.setFechaNacimiento(f)
    
print("ingrese su direccion: ")
calle = input("Ingrese su calle: ")
nomenclatura = input("Ingrese la nomenclatura (#): ")
barrio = input("Ingrese el barrio: ")
ciudad = input("Ingrese la ciudad: ")
edificio = input("Ingrese el edificio: ")
apto = input("Ingrese el numero de apartemento: ")
d = Direccion(calle, nomenclatura, barrio, ciudad, edificio, apto)
usu1.setDir(d)
    
print(nombre +" "+ str(id) +" "+ str(dd) +" - "+ str(mm) +" - "+ str(aa) +" "+ ciudadNacimiento +" "+ str(telefono) +" "+ email +" "+ calle +" #"+ nomenclatura +" "+ barrio +" "+ ciudad + " "+ edificio + " "+ apto)