from gl import * 
from utilidades import * #Archivo de utilidades.

def main(): 
    glCreateWindow(2028, 2028)  
    glClearColor(255, 255, 255) 
    glClear() 
    glColor(1, 0, 0)

    glSphere(-1.3,      0, -12, 1, color(100, 50, 150)) #Esfera 1.
    glSphere(1.5,      0, -6, 1, color(200, 170, 200)) #Esfera 2.
    
    finish()

main()