class color(object):
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __mul__(self, other): #Multiplicación.
        
        r = self.r 
        g = self.g
        b = self.b
        
        if type(other) == int or type(other) == float: #Si el otro es un entero o un flotante.
            r *= other
            g *= other
            b *= other
            
        else: #Si no.             
            r *= other.r
            g *= other.g
            b *= other.b

        r = min(255, max(r, 0))
        g = min(255, max(g, 0))
        b = min(255, max(b, 0))

        #print("Color: ", color(r, g, b))

        return color(r, g, b)

    def __add__(self, other): #Multiplicación.
    
        r = self.r 
        g = self.g
        b = self.b
        
        if type(other) == int or type(other) == float: #Si el otro es un entero o un flotante.
            r += other
            g += other
            b += other
            
        else: #Si no.             
            r += other.r
            g += other.g
            b += other.b

        r = min(255, max(r, 0))
        g = min(255, max(g, 0))
        b = min(255, max(b, 0))

        #print("Color: ", color(r, g, b))

        return color(r, g, b)
    
    def toBytes(self): #Regresando los bytes.
        return bytes([int(self.b), int(self.g), int(self.r)])

    #Regresando el color.
    def __repr__(self):
        #Retornando el color.
        return "color(%s, %s, %s)" % (self.r, self.g, self.b)