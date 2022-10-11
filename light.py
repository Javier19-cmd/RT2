#Clase de luz.
class Light: 
    def __init__(self, position, intensity, c): #Constructor de la clase.
        self.position = position #Posición de la luz.
        self.intensity = intensity #Intensidad de la luz.
        self.c = c #Color de la luz.