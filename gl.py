from ray import *
from utilidades import *
from math import *
from vector import *
from sphere import *

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
    c1.spheres.append(Sphere(V3(x, y, z), r)) #Guardando la esfera en el array de esferas.
    c1.colors.append(col) #Guardando el color de la esfera.

def cast_ray(orig, direction): #Método para el rayo. 
    
    #s = Sphere(V3(-3, -5, -16), 1) #Creando la esfera.

    #print(c1.spheres)

    for sphere in c1.spheres: #Recorriendo el array de esferas.
        sphereIntersection = sphere.ray_intersect(orig, direction) #Llamando al método para la intersección de la esfera, para validar si el rayo intersecta con la esfera.
        #print(sphereIntersection)
        if sphereIntersection: #Si el rayo intersecta con la esfera.
            #Se retorna el color de la esfera.
            return c1.colors[c1.spheres.index(sphere)]
    else:  #Si el rayo no intersecta con la esfera.
        return c1.color

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
        
            point(x, y, c)
    c1.write()