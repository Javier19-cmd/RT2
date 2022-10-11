from gl import * 
from utilidades import * #Archivo de utilidades.
from material import * #Archivo de material.
from ray import * #Archivo de rayo.

def main(): 
    glCreateWindow(1024, 1024)  
    glClearColor(255, 255, 255) 
    glClear() 
    #Creando array para las esferas.
    glColor(255, 0, 0)
    #glSphere(3, 1, -16, 0.5)
    
    #Creando materiales.
    rojo = Material(diffuse = color(255, 0, 0))
    amarillo = Material(diffuse = color(255, 255, 0))

    #Creando esferas.
    glSphere(1,      0, -12, 0.3, rojo) #Esfera 3 color azul.

    #Botón de hasta abajo.
    glSphere(1,   1.5, -12, 0.5, amarillo) #Esfera 4 color azul.

    finish()

main()