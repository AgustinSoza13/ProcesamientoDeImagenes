from skimage import io
import matplotlib.pyplot as plt
Image=io.imread("descarga.jpg")/255.0
print("dimensiones de la imagen:\n")
print(Image.shape)
plt.imshow(Image)
plt.show()
