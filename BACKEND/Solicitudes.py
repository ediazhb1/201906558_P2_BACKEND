class solicitud:
    def __init__(self, ids, titulo, url, categoria, descargas,descripcion, precio, likes):
        self.ids = ids
        self.titulo = titulo
        self.url = url
        self.categoria = categoria
        self.descargas = descargas
        self.descripcion = descripcion
        self.precio = precio
        self.likes= likes



    def setIds(self, ids):
        self.ids = ids

    def setTitulo(self, titulo):
        self.titulo = titulo

    def setUrl(self, url):
        self.url = url

    def setCategoria(self, categoria):
        self.categoria = categoria

    def setDescargas(self, descargas):
        self.descargas = descargas

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def setPrecio(self, precio):
        self.precio = precio

    def setLikes(self, likes):
        self.likes = likes

#----------------------------------

    def getIds(self):
        return self.ids

    def getTitulo(self):
        return self.titulo

    def getUrl(self):
        return self.url

    def getCategoria(self):
        return self.categoria

    def getDescargas(self):
        return self.descargas

    def getDescripcion(self):
        return self.descripcion

    def getPrecio(self):
        return self.precio

    def getLikes(self):
        return self.likes
