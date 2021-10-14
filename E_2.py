#Paredes Márquez Carlos
#Segunda parte algoritmo 13
#14 10 2021


import cv2
import numpy as np

def fondo(x1,x2):
       im = cv2.imread('ejemplo2.png')

       #cv2.imshow('Imagen original',  im)
       #cv2.waitKey(0)

       hsv = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
       mask0 = cv2.inRange(hsv, x1, x2)
       mask = mask0.copy()

       #cv2.imshow('mascara', mask0)
       #cv2.waitKey(0)

       cv2.floodFill(mask0,None,(80,300),255)
       neg = cv2.bitwise_not(mask0)
       im2 = cv2.bitwise_or(neg, mask)
       

       #cv2.imshow('Negacion mask', neg)
       #cv2.imshow('Convinacion negacion y mask', im2)
       return im2

def busqueda(im):   
      
      Datos = []
      imtype = im.astype(np.int32)
      h,w = im.shape
      Etiqueta = 0
      i = 0
      j = 0
      for i in range(h):
           for j in range(w):
                 if imtype[i,j] == 255:
                      imtype[i,j] == -1

      for i in range(h):
            for j in range(w):
                 if imtype[i,j] == 255: 
                      Etiqueta = Etiqueta +   1                        
                      cv2.floodFill(imtype,None,(j,i),Etiqueta)

      Datos.append(imtype)
      Datos.append(Etiqueta)

      return Datos

def mascara(im,imtype,x):
     mask = imtype == x
     im2 = im.copy()
     im2[~mask]=0
     
     return im2

def remplazo(res):
     im = cv2.imread('ejemplo2.png')
     hsv = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
     sus = cv2.bitwise_and(im,im,mask = res)
     return sus


im = fondo((0,0,0), (0,255,255))
objeto = busqueda(im) 

cv2.imshow('Algoritmo 12',im)     
cv2.waitKey(0)
print('Que objeto de la imagen quieres visualizar 1 -',objeto[1])
op2 = int(input())

res = mascara(im,objeto[0],op2)

cv2.imshow(str(op2),res)  
cv2.waitKey(0)

sustituto = remplazo(res)
cv2.imshow(str(op2),sustituto)
cv2.waitKey(0)
print('fin del programa.\n')
