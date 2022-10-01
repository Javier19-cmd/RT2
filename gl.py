#Imports necesarios para el gl.
from ray import *
from utilidades import *
from math import *
from vector import *
from sphere import *
from material import *

c1 = Raytracer() #Instancia de la clase Raytracer.


def glCreateWindow(width, height): #Función para crear la ventana.
    try: #Verificar que el tamaño sea un número.
        #Saber si las dimensiones son múltiplos de 4.
        if width % 4 == 0 and height % 4 == 0:
            
            #Creando las dimensiones de la pantalla.

            c1.width = width #Ancho de la pantalla.
            c1.height = height #Alto de la pantalla.

        elif width < 0 or height < 0: #Si las dimensiones son negativas, entonces se imprime un error.
            print("Error")
        else: 
            print("Error")
    
    except (TypeError, ZeroDivisionError): #Si en caso es NoneType, entonces se imprime esta excepción.
        print("Ocurrió un problema con el tamaño de la imagen.")
    #except: #Si en caso se escribió una letra en vez de número, entonces se imprime esta excepción.
     #   print("Se ingresó una letra en vez de número.")

def glClearColor(r, g, b): #Función para el color de fondo.
    c1.color = color(r, g, b); #Se le asigna el color.

def glClear(): #Función para limpiar la pantalla.
    c1.framebuffer = [
            [c1.color for x in range(c1.width)] 
            for y in range(c1.height)
        ] #Se crea el framebuffer.

def glColor(r, g, b): #Función para el color de la figura.
    c1.colorPunto = color(r, g, b); #Se le asigna el color.

#Defininiendo el point.
def point(x, y, c): 
    if x < c1.width and y < c1.height and x >= 0 and y >= 0:
        c1.framebuffer[y][x] = c

def glSphere(x, y, z, r, col):
    #c1.spheres.append(Sphere(V3(x, y, z), r)) #Guardando la esfera en el array de esferas.
    
    col = Material(diffuse=col) #Creando el material.

    esfera = Sphere(V3(x, y, z), r, col) #Creando la esfera.

    c1.spheres.append(esfera) #Guardando la esfera en el array de esferas.
    
    print(esfera)
    print(col)
    
    # c1.colors.append(rojo) #Guardando el color de la primera esfera.
    # c1.colors.append(verde) # Guardando el color de la segunda esfera.

def cast_ray(origin, direction): #Método para el rayo.
   material, intersect = scene_intersect(origin, direction) #Revisando contra que choca el rayo.
    
   if material is None: #Si no hay material, entonces se retorna
        return c1.color #El color de fondo.

   light_dir = (c1.light.position - intersect.point).normalice() #Dirección de la luz.
   light_intensity = light_dir @ intersect.normal #Intensidad de la luz.

#    print(abs((material.diffuse[2] * light_intensity) / 255))
#    print(abs((material.diffuse[1] * light_intensity) / 255))
#    print(abs((material.diffuse[0] * light_intensity) / 255))

   diffuse = color(
        abs((material.diffuse[2] * light_intensity) / 255),
        abs((material.diffuse[1] * light_intensity) / 255),
        abs((material.diffuse[0] * light_intensity) / 255)
    )

   return diffuse


def scene_intersect(orig, direction): #Método para la intersección de la escena.
    
    zBuffer = 999999 #Z index infinito.
    material = None #Material de la esfera.
    intersect = None #Intersección de la esfera.
    
    for o in c1.spheres: #Recorriendo el array de esferas.
       object_intersect = o.ray_intersect(orig, direction)
       if object_intersect: # Si hay intersección, entonces se retorna el color de la esfera.
           if object_intersect.distance < zBuffer: #Si la distancia es menor al zBuffer, entonces se retorna el color de la esfera.
               zBuffer = object_intersect.distance
               material = o.material
               intersect = object_intersect

    return material, intersect


def finish():
    fov = int(pi/2)
    aspectRatio = c1.width / c1.height #Relación de aspecto.
    tana = tan(fov/2) #Tangente del ángulo.

    for y in range(c1.height):
        for x in range(c1.width):
            i = ((2 * (x + 0.5) / c1.width) - 1) * tana * aspectRatio
            j = (1 - ( 2 * (y + 0.5) / c1.height)) * tana
            origin = V3(0, 0, 0)
            direction = (V3(i, j, -1)).normalice()

            c = cast_ray(origin, direction) #Llamando al método para el rayo.
        
            point(x, y, c) #Creando un punto.
    c1.write()