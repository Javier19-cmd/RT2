from utilidades import * #Archivo de utilidades.
#Clase para el raytracer.
class Raytracer(object):
    #Ancho y alto de la imagen.
    width  = 0 
    height = 0
    #Variable para el framebuffer.
    framebuffer = 0 

    #Variable para guardar el color del fondo.
    color_fondo = 0

    #Variable para guardar el color del punto. 
    colorPunto = 0

    #Variable para guardar la matriz de esferas.
    spheres = []

    #Variable para guardar la matriz de planos.
    planes = []

    #Variable para guardar la lista de colores.
    colors = []

    #Variable para guardar la luz.
    light = None

    #Método que escribe el archivo bmp.
    def write(self): #Escribir un archivo, pero con el zbuffer.
            #Se abre el archivo con la forma de bw.
            f = open("RT2.bmp", "bw")
            
            #Se escribe el encabezado del archivo.

            #Haciendo el pixel header.
            f.write(char('B'))
            f.write(char('M'))
            #Escribiendo el tamaño del archivo en bytes.
            f.write(dword(14 + 40 + self.width * self.height * 3))
            f.write(dword(0)) #Cosa que no se utilizará en este caso.
            f.write(dword(14 + 40)) #Offset a la información de la imagen. 14 bytes para el header, 40 para la información de la imagen. Aquí empieza la data.
            #Lo anterior suma 14 bytes.

            #Información del header.
            f.write(dword(40)) #Este es el tamaño del header. Esto es de 4 bytes, por eso se utiliza el dword.
            f.write(dword(self.width)) #Ancho de la imagen. Esto es de 4 bytes, por eso se utiliza el dword.
            f.write(dword(self.height)) #Alto de la imagen. Esto es de 4 bytes, por eso se utiliza el dword.
            f.write(word(1)) #Número de planos. Esto es de 2 bytes, por eso se utiliza el word.
            f.write(word(24)) #24 bits por pixel. Esto es porque usa el true color y el RGB.
            f.write(dword(0)) #Esto es la compresión. Esto es de 4 bytes, por eso se utiliza el dword.
            f.write(dword(self.width * self.height * 3)) #Tamaño de la imagen sin el header.
            #Pixels que no se usarán mucho.
            f.write(dword(0))
            f.write(dword(0))
            f.write(dword(0))
            f.write(dword(0))
            #Lo anterior suma 40 bytes.

            #print("Framebuffer", framebuffer)
            #Pintando el archivo de color negro.
            for y in range(self.height):
                for x in range(self.width):
                    f.write(self.framebuffer[y][x])

            #print("Archivo escrito")

            f.close() #Cerrando el archivo que se escribió.