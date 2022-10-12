from gl import * 
from utilidades import * #Archivo de utilidades.
from material import * #Archivo de material.
from ray import * #Archivo de rayo.

def main(): 
    glCreateWindow(500, 500)  
    glClearColor(10, 20, 150) 
    glClear() 
    #Creando array para las esferas.
    glColor(255, 0, 0)
    #glSphere(3, 1, -16, 0.5)
    
    #Creando esferas.
    glSphere() #Esfera 3 color azul.
    #glPlane() #Plano.

    finish()

main()