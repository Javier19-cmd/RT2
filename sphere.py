class Sphere(object): #Clase para esferas.
    def __init__(self, center, radius, material): #Recibe el centro y el radio.
        self.center = center
        self.radius = radius
        self.material = material 
    
    def ray_intersect(self, orig, dir): #Recibe el origen y la dirección del rayo.
        L = self.center - orig #Vector L.

        tca = L @ dir #Producto punto entre L y la dirección del rayo.

        l = L.len() #Longitud de L al cuadrado.

        d2 = l**2 - tca**2 #Distancia al cuadrado.
        

        if d2 > self.radius**2: #Si la distancia al cuadrado es mayor al radio al cuadrado.
            #print(d2, self.radius**2)
            return False
        else:

            thc = (self.radius**2 - d2)**0.5 #Distancia al cuadrado.

            t0 = tca - thc #Distancia al cuadrado.
            t1 = tca + thc #Distancia al cuadrado.
            
            if t0 < 0: #Si la distancia al cuadrado es menor a 0.
                t0 = t1 #Distancia al cuadrado.
            
            if t0 < 0:  #Si la distancia al cuadrado es menor a 0.
                return False
            

        return True
    
    #Método toString para imprimir la esfera.
    def __str__(self):
        return str(self.center) + " " + str(self.radius) + " " + str(self.material)