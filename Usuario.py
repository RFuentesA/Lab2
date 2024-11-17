class Usuario():
    def __init__(self, nombre, id, Fecha, ciudad_nacimiento, tel, email, Direccion):
        self.__nombre = nombre
        self.__id = id
        self.__fechaNacimiento = Fecha
        self.__ciudadNacimiento = ciudad_nacimiento
        self.__telefono = tel
        self.__email = email
        self.__dir = Direccion

    def Usuario(self):
        self.__init__()
    
    def Usuario(self, nombre, id):
        self.__nombre = nombre
        self.__id = id
    
    def get_nombre(self):
        return
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_id(self):
        return
    
    def set_id(self, id):
        self.__id = id
    
    def get_fechaNacimiento(self):
        return

    def set_fechaNacimiento(self, Fecha):
        self.__fechaNacimiento = Fecha
    
    def get_ciudadNacimiento(self):
        return

    def set_ciudadNacimiento(self, ciudad_nacimiento):
        ciudadNacimiento = ciudad_nacimiento
    
    def get_telefono(self):
        return
    
    def set_telefono(self, tel):
        self.__telefono = tel
    
    def get_email(self):
        return
    
    def set_email(self, email):
        self.__email = email
    
    def get_dir(self):
        return
    
    def set_dir(self, Direccion):
        self.__dir = Direccion
    
    def __str__(self):
        texto = f"El Nombre del usuario es: {self.get_nombre}, identificado con el id: {self.get_id}, nacido el dia: {self.get_fechaNacimiento}, 
        en la ciudad de: {self.get_ciudadNacimiento}, su numero de telefono es: {self.get_telefono}, su correo electronico es: {self.get_email}, y su direccion es: {self.get_dir}"
        return texto

