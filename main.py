from gl import * 
from utilidades import * #Archivo de utilidades.

def main(): 
    glCreateWindow(2028, 2028)  
    glClearColor(1, 1, 1) 
    glClear() 
    #Creando array para las esferas.
    glColor(1, 0, 0)
    #glSphere(3, 1, -16, 0.5)

    #Creando al Snowman.
    #Parte de abajo.
    #Botón entre la parte de abajo y la media.
    glSphere(2.3,      0, -12, 0.3, color(0.1, 0.5, 0.4)) #Esfera 3 color azul.

    #Botón de hasta abajo.
    glSphere(2.3,   1.5, -12, 0.5, color(0.1, 0.5, 0.4)) #Esfera 4 color azul.

    glSphere(3,        2, -16, 2, color(1, 0, 0)) #Esfera 1 color rojo.
    
    #Creando botones del tronco del muñeco.
    glSphere(2.3,      -0.9, -12, 0.2, color(0.1, 0.5, 0.4)) #Esfera 3 color azul.
    
    #Tronco.
    glSphere(3.8,     -1, -20, 2, color(0, 1, 0)) #Esfera 2 color verde.
    
    #Ojos.
    glSphere(2.1,      -2.6, -12, 0.1, color(0.6, 0.1, 0.5)) #Primer ojo.
    glSphere(2.5,      -2.6, -12, 0.1, color(0.6, 0.1, 0.5)) #Segundo ojo.

    #Nariz.
    glSphere(2.3,     -2.3, -12, 0.1, color(0.1, 0.3, 0.2)) #Nariz.

    #Cabeza.
    glSphere(3.45,   -3.5, -18, 1, color(0, 0, 1)) #Esfera 3 color azul.

    finish()

main()