class Persona:

    def __init__(self,nombre,apellido,usuario,password,confirm,rol,foto):
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.password = password
        self.confirm = confirm
        self.rol = rol
        self.foto = foto

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido
    
    def setUsuario(self, usuario):
        self.usuario = usuario

    def setPassword(self, password):
        self.password = password

    def setConfirm(self, confirm):
        self.confirm = confirm  

    def setRol(self, rol):
        self.rol = rol 

    def setFoto(self, foto):
        self.rol = foto
    #-------------------------GET----------------------------
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getUsuario(self):
        return self.usuario

    def getPassword(self):
        return self.password

    def getConfirm(self):
        return self.confirm
    
    def getRol(self):
        return self.rol

    def getFoto(self):
        return self.foto