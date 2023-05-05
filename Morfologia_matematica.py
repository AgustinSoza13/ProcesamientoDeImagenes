        r, g, b = self.imagen[x,y]
                self.imagenGris[x,y]=0.2989 * r + 0.5870 * g + 0.1140 * b
    def VisualizarGris(self):
        plt.imshow(self.imagenGris,cmap='gray')        
        plt.show()
    def VisualizarImagen(self):
        self.imagen.show()

    def getImagen(self):
        return self.imagen
    def getImagenGris(self):
        return self.imagenGris
    def getImagenErocionada(self):
        return self.imagenErosionada
    def getImagenDilatada(self):
        return self.imagenDilatada



    def Erocion(self,image):            
        self.alto,self.ancho,_=self.imagen.shape
        a=2
        #kernel = np.ones((5,5))
        self.imagenErosionada=np.zeros((self.alto,self.ancho))
        for i in range(self.alto):
            for j in range(self.ancho):
                patch = image[i-1:i+a, j-1:j+a]
                print(patch)
                """
                pivot=0
                for t in patch:
                    for h in t:
                        if pivot==0:
                            pivot=h
                        if pivot>h:
                            pivot=h 
                """
                #self.imagenErosionada[i, j]=pivot                   
                #imagenErosionada[i, j] = min(min(fila) for fila in patch)#erosio

        #plt.imshow(self.imagenErosionada,cmap="gray")
        #plt.show()

    def Dilatacion(self,image):
        a=2
        #kernel = np.ones((5,5))
        self.imagenDilatada=np.zeros((self.alto,self.ancho))
        for i in range(self.alto):
            for j in range(self.ancho):
                patch = image[i-1:i+a, j-1:j+a]
                pivot=0
                for t in patch:
                    for h in t:
                        if pivot==0:
                            pivot=h
                        if pivot<h:
                            pivot=h 
                self.imagenDilatada[i, j]=pivot                   
                #imagenErosionada[i, j] = min(min(fila) for fila in patch)#erosio

        plt.imshow(self.imagenDilatada,cmap="gray")
        plt.show()


    def TopHat(self):
        pass