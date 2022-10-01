class Material: #Clase de material.
    def __init__(self, diffuse): #Constructor de la clase.
        self.diffuse = diffuse
    
    #Método toString para imprimir el material.
    def __str__(self):
        return str(self.diffuse)