#Clase material.
class Material:
    def __init__(self, diffuse): #Constructor de la clase.
        self.diffuse = diffuse #Esto guarda un color.

    def __repr__(self):
        return f"Material({self.diffuse}, {self.albedo}, {self.spec})"