import cv2

import matplotlib.pyplot as plt
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('tango.jpg')

print(type(img))
print(img.shape)




# cv2.imshow('image', img_convert)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


def czytanie(obrazek) -> str:
    return (pytesseract.image_to_string(obrazek))


img = cv2.imread('tango.jpg')
kubek = cv2.imread('kubek.jpg')
angcytat = cv2.imread('5s.jpg')
img1 = cv2.imread('ang.png')
img2 = cv2.imread('2.jpg')

print(czytanie(img)) #dziala
print(czytanie(kubek)) #prawie działa
print(czytanie(angcytat)) #dziala
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
img2c= cv2.threshold(cv2.GaussianBlur(img2, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
print(czytanie(img2))
print(czytanie(img1)) #dziala