
import matplotlib.pyplot as plt
from skimage import io
from PIL import Image
import numpy as np
import matplotlib.image as mpimg
import cv2
class Imagen:
    def __init__(self,ruta):
        self.ruta=ruta
    def CargarImagen(self):
        self.imagen=cv2.imread(self.ruta)
    def convertir_a_grises(self):
        self.imagen = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2GRAY)

    def EscalaDeGrises(self):
        
        self.imagenGris=np.zeros((self.alto,self.ancho))
        for x in range(self.alto):
            for y in range(self.ancho):
                r, g, b = self.imagen[x,y]
                self.imagenGris[x,y]=0.2989 * r + 0.5870 * g + 0.1140 * b
    def VisualizarGris(self):
        plt.imshow(self.imagenGris,cmap='gray')        
        plt.show()
    def VisualizarImagen(self):
        plt.imshow(self.imagen)
        plt.show()
        
    def getImagen(self):
        return self.imagen
    def getImagenGris(self):
        return self.imagenGris
    def getImagenErocionada(self):
        return self.imagenErosionada
    def getImagenDilatada(self):
        return self.imagenDilatada
    def getImagenApetura(self):
        return self.imagenApertura

    def Erocion(self,image):            
        x,y,=image.shape
        a=2
        #kernel = np.ones((5,5))
        self.imagenErosionada=np.zeros((x,y))
        for i in range(x):
            for j in range(y):
                patch = image[i-1:i+a, j-1:j+a]
                pivot=0
                for t in patch:
                    for h in t:
                        if pivot==0:
                            pivot=h
                        if pivot>h:
                            pivot=h 
                self.imagenErosionada[i, j]=pivot   
        plt.imshow(self.imagenErosionada)   
        plt.title("Eroción")             

    def Dilatacion(self,image):
        x,y=image.shape
        a=2
        #kernel = np.ones((5,5))
        self.imagenDilatada=np.zeros((x,y))
        for i in range(x):
            for j in range(y):
                patch = image[i-1:i+a, j-1:j+a]
                pivot=0
                for t in patch:
                    for h in t:
                        if pivot==0:
                            pivot=h
                        if pivot>h:
                            pivot=h
                self.imagenDilatada[i, j]=pivot                   
                

                 
        
    def Apertura(self,a):
        
        pass

    def TopHat(self):
        pass
# originalgriss-
if __name__ == '__main__':

    camara=Imagen("uno.png")
    camara.CargarImagen()
    camara.convertir_a_grises()
    camara.Erocion(camara.getImagen())
    camara.Dilatacion(camara.getImagen())
    #camara.Apertura(camara.Dilatacion())
    #plt.imshow(camara.getImagenApetura,cmap="gray")
    #plt.show()
    
    fig,axs=plt.subplots(3,3,figsize=(8,8))#
    axs[0,0].imshow(camara.getImagen(),cmap="gray")
    axs[0,1].imshow(camara.getImagenErocionada(),cmap="gray")
    axs[1,0].imshow(camara.getImagenDilatada(),cmap="gray")
    axs[1,1].imshow(camara.getImagenDilatada()-camara.getImagen(),cmap="gray")
    plt.show()
    

    plt.imshow(camara.getImagenDilatada()-camara.getImagen(),cmap="gray")
    plt.title("gradiente morfologico")
    #camara.Erocion(camara.getImagen())
    #plt.imshow(camara.getImagenDilatada()-camara.getImagen())#gradiente morfologico
    plt.show()
    #plt.imshow(camara.getImagenErocionada()-camara.getImagen(),cmap="gray")
    #plt.show()
    #-----
    plt.imshow(camara.getImagen()-camara.getImagenDilatada(),cmap="gray")
    plt.title("uno")
    plt.show()
    plt.imshow(camara.getImagen()-camara.getImagenErocionada(),cmap="gray")
    plt.title("dos")
    plt.show()

    camara.Dilatacion(camara.getImagenErocionada())
    plt.imshow(camara.getImagen()-camara.getImagenDilatada(),cmap="gray")
    plt.title("final")
    plt.show()

#diferencia finita

