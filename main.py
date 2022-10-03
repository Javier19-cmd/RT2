from gl import * 
from utilidades import * #Archivo de utilidades.

def main(): 
    glCreateWindow(2028, 2028)  
    glClearColor(255, 255, 255) 
    glClear() 
    glColor(1, 0, 0)

    #Guardando los valores del color en una variable.
    col1 = [100, 120, 20]
    albedo1 = [0.9, 0.1]
    spec1 = 10
    glSphere(-1.3,      0, -12, 1, col1, albedo1, spec1) #Esfera 1.
    col2 = [100, 100, 100]
    albedo2 = [0.6, 0.2]
    spec2 = 50
    glSphere(1.5,      0, -6, 1, col2, albedo2, spec2) #Esfera 2.
    
    finish()

main()