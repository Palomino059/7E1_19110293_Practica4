import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Colores.jpg',0)
im = cv2.imread('Colores.jpg')
negro = cv2.imread('negro.jpg')
imag = cv2.imread('Colores.jpg',0)

"--------------- Imagen en Negro --------------------"
" Trazo en Lineas  "
cv2.line(negro,(0,0),(300,300),(200,0,0),5)
cv2.line(negro,(300,0),(0,300),(200,0,0),5)

" Circulo "
cv2.circle(negro,(100,100),50,(0,0,200),-1)

cv2.imshow('Imagen', negro)
cv2.waitKey(0)
cv2.destroyAllWindows()

"------------------ Imagen con Texto ----------------"

cv2.putText(negro,'19110293',(0,50),1,2,(255,255,0),2,cv2.LINE_AA)
cv2.putText(negro,'19110293',(0,25),1,2,(174,64,23),2,cv2.LINE_AA)
cv2.putText(negro,'19110293',(0,10),1,2,(78,174,23),2,cv2.LINE_AA)

cv2.imshow('Texto', negro)
cv2.waitKey(0)
cv2.destroyAllWindows()


"----------- Imagen en Gris -----------------------"

cv2.line(img,(0,0),(500,500),(400,0,0),5)
cv2.line(img,(500,0),(0,500),(400,0,0),5)

cv2.circle(img,(100,100),50,(0,0,200),-1)

cv2.imshow('Imagen', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"------------------ Imagen en gris con Texto ----------------"

cv2.putText(img,'19110293',(0,50),1,2,(255,255,0),2,cv2.LINE_AA)
cv2.putText(img,'19110293',(0,25),1,2,(174,64,23),2,cv2.LINE_AA)
cv2.putText(img,'19110293',(0,10),1,2,(78,174,23),2,cv2.LINE_AA)

cv2.imshow('Texto',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


"-------------- ROI -----------------"

im2 = im[150:800, 200:600]

cv2.imshow('Imagen Original', im)
cv2.imshow('Imagen ROI', im2)
cv2.waitKey(0)
cv2.destroyAllWindows()

"--------------- ROI 2 ----------------------"

roi = cv2.selectROI(im)

print(roi)
demuestra = im[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]

cv2.imshow('Imagen ', demuestra)
cv2.waitKey(0)
cv2.destroyAllWindows()

"--------------- CANNY -----------------------"

canny = cv2.Canny(imag, 100, 200)

titles = ['Imagen', 'Canny']
imagen = [imag, canny]
for i in range(2):
    plt.subplot(1,2,i+1), plt.imshow(imagen[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()    
