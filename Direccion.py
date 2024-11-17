class Direccion:
    def __init__(self, calle, ciudad, nomenclatura, edificio, barrio, apto):
        self.__calle = calle
        self.__ciudad = ciudad
        self.__nomenclatura = nomenclatura
        self.__edificio = edificio
        self.__barrio = barrio
        self.__apto = apto
    
        
    def setCalle(self, c):
        self.__calle = c
        
    def getCalle(self):
        return self.__calle
    
    def setCiudad(self, c):
        self.__ciudad = c
        
    def getCiudad(self):
        return self.__ciudad