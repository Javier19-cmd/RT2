import mmap
import struct

#Se puede usar lo que se había hecho para abrir bmp's en el proyecto 1.
class Envmap(object):
    def __init__(self, filename):
        self.filename = filename
        self.read()

    def read(self):
        with open(self.path) as rb:
            m = mmap.mmap(rb.fileno(), 0, access=mmap.ACCESS_READ)
            ba = bytearray(m)

