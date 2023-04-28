
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import matplotlib.image as mpimg
class Imagen:
    def __init__(self,ruta):
        self.ruta=ruta
    def CargarImagen(self):
        self.imagen=Image.open(self.ruta)
    def EscalaDeGrises(self):
        img = mpimg.imread('descarga.jpg')
        alto,ancho,_=img.shape

        #self.ImagenGris=Image.new("L",(self.ancho,self.alto))#retorna imagen en escala de grises
        self.imagenGris=np.zeros((alto,ancho))
        for x in range(alto):
            for y in range(ancho):
                r, g, b = img[x,y]
                self.imagenGris[x,y]=0.2989 * r + 0.5870 * g + 0.1140 * b
        plt.imshow(self.imagenGris,cmap='gray')        
        plt.show()
        #return self.imgenGris
    
    def VisualizarImagen(self):
        plt.imshow(self.imagen)
        plt.show() 
    def VisualizarGris(self):
        plt.imshow(self.imagenGris)
        plt.show()

if __name__ == '__main__':
    lena=Imagen("descarga.jpg")
    lena.CargarImagen()
    print()
    lena.EscalaDeGrises()
    lena.VisualizarGris()
    



