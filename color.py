#Clase color.
class color:
    def __init__(self, r, g, b): #Constructor de la clase.
        self.r = r
        self.g = g
        self.b = b
    
    def __mul__(self, other):
        r = self.r
        g = self.g
        b = self.b

        #Verificando que los tipos sean correctos.
        if type(other) == int or type(other) == float:
           r *= other
           g *= other
           b *= other
        else: 
            r *= other.r
            g *= other.g
            b *= other.b

        
        #Verificando que los valores de r, g, b no se salgan de los rangos.
        r = min(255, max(r, 0))
        g = min(255, max(g, 0))
        b = min(255, max(b, 0))

        return color(r, g, b)
    
    def toBytes(self): #Método para convertir el color a bytes.
        return bytes([self.r, self.g, self.b])

    def __repr__(self):
        return "color(%s, %s, %s)" % (self.r, self.g, self.b)