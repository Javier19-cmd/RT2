#Archivo para otras cosas.
from intersect import *
from vector import *

class Plane(object):
    def __init__(self, y, w, l, material):
        self.y = y
        self.w = w
        self.l = l
        self.material = material

    def ray_intersect(self, orig, direction): #Método para la intersección.
        d = -(orig.y + direction.y) / direction.y
        impact = orig + direction * d
        normal = V3(0, 1, 0)


        if d <= 0 or \
            impact.x < -2 or impact.x > 2 or \
            impact.z > -5 or impact.z < -10: #Si la distancia es menor o igual a 0, entonces no hay intersección.
            return None

        return Intersect(
            distance=d,
            point=impact,
            normal=normal
        )