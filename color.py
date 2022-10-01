#Clase color.
class Color:
    def __init__(self, r, g, b): #Constructor de la clase.
        self.r = r
        self.g = g
        self.b = b
    
    def __mul__(self, other):
        
        #Verificando que los tipos sean correctos.
        if type(other) == int or type(other) == float:
           self.r *= other
           self.g *= other
           self.b *= other
        else: 
            self.r *= other.r
            self.g *= other.g
            self.b *= other.b

        
        #Verificando que los valores de r, g, b no se salgan de los rangos.
        self.r = min(255, max(self.r, 0))
        self.g = min(255, max(self.g, 0))
        self.b = min(255, max(self.b, 0))
    
    def toBytes(self): #Método para convertir el color a bytes.
        return bytes([self.r, self.g, self.b])

    def __repr__(self):
        return "color(%s, %s, %s)" % (self.r, self.g, self.b)