class Reseña:
    def __init__(self,reseña,ids,usuario):
        self.reseña = reseña
        self.ids = ids
        self.usuario = usuario


    def setReseña(self, reseña):
        self.reseña = reseña
    
    def setIds(self, ids):
        self.ids = ids
    
    def setUsuario(self, usuario):
        self.usuario = usuario

    def getReseña(self):
        return self.reseña
    
    def getIds(self):
        return self.ids
    
    def getUsuario(self):
        return self.usuario