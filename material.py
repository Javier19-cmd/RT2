class Material: #Clase de material.
    def __init__(self, diffuse, albedo, spec): #Constructor de la clase.
        self.diffuse = diffuse
        self.albedo = albedo
        self.spec = spec
    
    #Método toString para imprimir el material.
    def __str__(self):
        return str(self.diffuse)

    #Obteniendo el objecto con cierto índice.
    def __getitem__(self, index):
        return self.diffuse[index]