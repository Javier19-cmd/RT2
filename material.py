#Clase material.
class Material:
    def __init__(self, diffuse, albedo, spec): #Constructor de la clase.
        self.diffuse = diffuse #Esto guarda un color.
        self.albedo = albedo #Esto el albedo del material.
        self.spec = spec #Esto guarda el especular del material.