class Direccion:
    def __init__(self, calle, ciudad, nomenclatura, edificio, barrio, apto):
        self.__calle = calle
        self.__nomenclatura = nomenclatura
        self.__barrio = barrio
        self.__ciudad = ciudad
        self.__edificio = edificio
        self.__apto = apto
    
    def Direccion(self):
        self.__init__
        
    def setCalle(self, c):
        self.__calle = c
        
    def getCalle(self):
        return self.__calle
    
    def setCiudad(self, ci):
        self.__ciudad = ci
        
    def getCiudad(self):
        return self.__ciudad
    
    def setNomenclatura(self,n):
        self.__nomenclatura = n
        
    def getNomenclatura(self):
        return self.__nomenclatura
    
    def setBarrio(self,b):
        self.__barrio = b
        
    def getBarrio(self):
        return self.__barrio
    
    def setEdificio(self, e):
        self.__edificio = e
        
    def getEdificio(self):
        return self.__edificio
    
    def setApto(self, a):
        self.__apto = a
        
    def getApto(self):
        return self.__apto
    
    def __str__(self):
        texto = self.getCalle + self.getNomenclatura + self.getBarrio + self.getCiudad + self.getEdificio + self.getApto
        return texto