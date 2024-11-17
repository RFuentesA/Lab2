from Clases.Usuario import *
from Clases.Direccion import *
from Clases.Fecha import *

if __name__ == '__main__':
    f1 = Fecha(10, 5, 2006)
    #print(f1)

    usu1 = Usuario("richi", 110, "valledupar", 3042236809, "rfuentesa@unal.edu.co")
    usu1.setFechaNacimiento(f1)
    print(usu1)