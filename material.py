#Clase material.
class Material:
    #Diffuse, albedo y spec.
    def __init__(self, diffuse, albedo, spec): #Constructor de la clase.
        self.diffuse = diffuse #Esto guarda un color.
        self.albedo = albedo #Esto guarda un array.
        self.spec = spec #Esto guarda un número.