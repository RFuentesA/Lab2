class Fecha():
    def __init__(self, dd, mm, aa):
        self.__dia = dd
        self.__mes = mm
        self.__año = aa
    
    def Fecha(self):
        self.__init__()
    
    def getDia(self):
        return self.__dia
    
    def setDia(self, dd):
        self.__dia = dd
    
    def getMes(self):
        return self.__mes

    def setMes(self, mm):
        self.__mes = mm
    
    def getAño(self):
        return self.__año
    
    def setAño(self, aa):
        self.__año = aa
    
    #def __str__(self):
    #    return print(f"{self.getDia} - {self.getMes} - {self.getAño} ")