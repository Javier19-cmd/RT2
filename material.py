class Material: #Clase de material.
    def __init__(self, diffuse): #Constructor de la clase.
        self.diffuse = diffuse
    
    #Método toString para imprimir el material.
    def __str__(self):
        return str(self.diffuse)

    #Obteniendo el objecto con cierto índice.
    def __getitem__(self, index):
        return self.diffuse[index]