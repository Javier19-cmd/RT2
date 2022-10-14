from intersect import *
from vector import *
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
            return None
        #else: #Quitando el else de momento.

        thc = (self.radius**2 - d2)**0.5 #Distancia al cuadrado.

        t0 = tca - thc #Distancia al cuadrado.
        t1 = tca + thc #Distancia al cuadrado.
        
        if t0 < 0: #Si la distancia al cuadrado es menor a 0.
            t0 = t1 #Distancia al cuadrado.
        
        if t0 < 0:  #Si la distancia al cuadrado es menor a 0.
            return None

        impact = orig + (dir * t0) #Impacto. 
        #print("Impacto: ", impact)
        normal = (impact - self.center).normalice() #Normal.
        #print("Normal: ", normal)

        #Regresando la distancia.
        return Intersect(
            distance = t0,
            point = impact,
            normal = normal,
        )