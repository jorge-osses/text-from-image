import pytesseract
import cv2

#cargar imagen utilizando opencv
img = cv2.imread("2.jpg")

#extraer texto de la imagen
sret = pytesseract.image_to_string(img)

#mostrar resultado
print(sret)