from Clases.Usuario import *
from Clases.Direccion import *
from Clases.Fecha import *

#Pedido por consola literal 5 porque meimprime la direccion en memoria el metodo get de usuario? usu1.getNombre = #en la RAM
print("ingrese sus datos: ")
nombre = input("")
id = input()
ciudadNacimiento = input()
telefono =input()
email = input("")
usu1 = Usuario(nombre,id,ciudadNacimiento,telefono,email)
    
print("ingrese su fecha de nacimeinto")
dd = input()
mm = input()
aa = input()
f = Fecha(dd,mm,aa)
usu1.setFechaNacimiento(f)
    
print("ingrese su direccion ")
calle = input("")
nomenclatura = input("")
barrio = input("")
ciudad = input("")
edificio = input("")
apto = input("")
d = Direccion(calle,nomenclatura,barrio,ciudad,edificio,apto)
usu1.setDir(d)
    
print(nombre +" "+ str(id) +" "+ str(dd) +" - "+ str(mm) +" - "+ str(aa) +" "+ ciudadNacimiento +" "+ str(telefono) +" "+ email +" "+ calle +" #"+ nomenclatura +" "+ barrio +" "+ ciudad + " "+ edificio + " "+ apto)