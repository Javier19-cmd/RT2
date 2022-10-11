from code import interact
from ray import *
from utilidades import *
from math import *
from vector import *
from sphere import *
from material import *
from light import *
from color import *

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
    c1.color_fondo = color(r, g, b).toBytes() #Se le asigna el color.

def glClear(): #Función para limpiar la pantalla.
    c1.framebuffer = [
            [c1.color_fondo for x in range(c1.width)] 
            for y in range(c1.height)
        ] #Se crea el framebuffer.

def glColor(r, g, b): #Función para el color de la figura.
    c1.colorPunto = color(r, g, b).toBytes() #Se le asigna el color.

#Defininiendo el point.
def point(x, y, c): 
    if x < c1.width and y < c1.height and x >= 0 and y >= 0:
        c1.framebuffer[y][x] = c

def glSphere(): #Método para crear las esferas.

    #c1.spheres.append(Sphere(V3(x, y, z), r, col)) #Guardando la esfera en el array de esferas.
    #c1.colors.append(col) #Guardando el color de la esfera.
    
    #Crenado el material de las esferas.
    rubber = Material(diffuse=color(255, 100, 240), albedo=[0.9, 0.1], spec=10)
    ivory = Material(diffuse=color(255, 165, 210), albedo=[0.6, 0.3], spec=50)

    #Creando esferas.
    c1.spheres = [
        Sphere(V3(-3, 0,-12), 2, rubber),
        Sphere(V3(2, 0,-12), 2, ivory),
    ]

    c1.light = Light(V3(-20, 20, 20), 1.5, color(255, 255, 255)) #Creando la luz.

def cast_ray(orig, direction): #Método para el rayo.
    #Revisa contra que chocó y en base a eso regresa un material.
    
    material, intersect = scene_intersect(orig, direction) #Llamando a la función para la intersección.

    if material is None: #Si no hay material, entonces se regresa el color de fondo.
        return c1.color_fondo

    light_dir = (c1.light.position - intersect.point).normalice() #Llamando al método para la luz.

    diffuse_intensity = light_dir @ intersect.normal #Calculando la intensidad de la luz.
    
    #Calculando el color de la esfera.
    
    #print(material.diffuse)
    #print(diffuse_intensity)
    #print(material.albedo[0])

    diffuse = material.diffuse * diffuse_intensity * material.albedo[0] #Calculando la reflexión difusa.
    #print("Diffuse: ", diffuse)

    #Componente especular.
    light_reflection = reflect(light_dir, intersect.normal) #Calculando la reflexión.
    reflection_intensity = max(0, light_reflection @ direction) #Calculando la intensidad de la reflexión.
    specular_intensity =  c1.light.intensity * reflection_intensity ** material.spec #Calculando la intensidad de la luz.
    specular = c1.light.c * specular_intensity * material.albedo[1] #Calculando la reflexión especular.

    #print("Especular: ", specular)

    #print(diffuse + specular)

    # print(light_reflection)
    # print(reflection_intensity)
    # print(specular_intensity)

    return (diffuse + specular).toBytes() #Regresando el color de la esfera.

#Método para calcular la reflexión.
def reflect(I, N):
    return (I - N * 2 * (N @ I)).normalice()

#Función para la intersección.
def scene_intersect(orig, direction):
    #Revisa todos los objetos de la escena y regresa el material del objeto con el que chocó.
    zBuffer = 999999 #Se crea el zBuffer. 
    material = None #Se crea el material.
    intersect = None #Se crea la intersección.

    for o in c1.spheres: #Recorriendo el array de esferas.
        object_intersect = o.ray_intersect(orig, direction) #Llamando al método para el rayo.
        
        if object_intersect: #Si hay intersección, entonces se regresa el material.
            if object_intersect.distance < zBuffer:
                #Se actualiza el zBuffer y se regresa el material actualizado.
                zBuffer = object_intersect.distance
                material = o.material
                intersect = object_intersect
    
    return material, intersect #Regresando el color de la esfera.


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
        
            point(x, y, c) #Pintando un punto con el color que se recibe después del cast_ray.
    c1.write()