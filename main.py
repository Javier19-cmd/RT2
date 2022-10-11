from gl import * 
from utilidades import * #Archivo de utilidades.

def main(): 
    glCreateWindow(1024, 1024)  
    glClearColor(255, 255, 255) 
    glClear() 
    #Creando array para las esferas.
    glColor(255, 0, 0)
    #glSphere(3, 1, -16, 0.5)

    #Creando al Snowman.
    #Parte de abajo.
    #Botón entre la parte de abajo y la media.
    glSphere(1,      0, -12, 0.3, color(100, 199, 159)) #Esfera 3 color azul.

    #Botón de hasta abajo.
    glSphere(1,   1.5, -12, 0.5, color(100, 199, 159)) #Esfera 4 color azul.

    finish()

main()