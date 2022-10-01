from gl import * 
from utilidades import * #Archivo de utilidades.

def main(): 
    glCreateWindow(2028, 2028)  
    glClearColor(1, 1, 1) 
    glClear() 
    glColor(1, 0, 0)

    glSphere(-1.3,      0, -12, 1, color(0.1, 0.5, 0.4)) #Esfera 1.
    glSphere(-4.3,      0, -12, 1, color(0.1, 0.2, 0.9)) #Esfera 2.
    
    finish()

main()