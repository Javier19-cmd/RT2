from gl import * 
from utilidades import * #Archivo de utilidades.

def main(): 
    glCreateWindow(2028, 2028)  
    glClearColor(255, 255, 255) 
    glClear() 
    glColor(1, 0, 0)

    #Guardando los valores del color en una variable.
    col1 = [100, 120, 20]
    glSphere(-1.3,      0, -12, 1, col1) #Esfera 1.
    col2 = [100, 100, 100]
    glSphere(1.5,      0, -6, 1, col2) #Esfera 2.
    
    finish()

main()