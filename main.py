from gl import * 
from utilidades import * #Archivo de utilidades.
from material import * #Archivo de material.
from ray import * #Archivo de rayo.

def main(): 
    glCreateWindow(500, 500)  
    glClearColor(255, 255, 255) 
    glClear() 
    #Creando array para las esferas.
    glColor(255, 0, 0)
    #glSphere(3, 1, -16, 0.5)
    
    #Creando esferas.
    glSphere() #Esfera 3 color azul.

    finish()

main()