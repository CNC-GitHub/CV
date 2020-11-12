import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img1 = cv.imread('C:\Test_CV\Pictures\saved_new_K10.jpg')

img = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)

ret,thresh1 = cv.threshold(img,0,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,35,255,cv.THRESH_BINARY)
ret,thresh3 = cv.threshold(img,65,255,cv.THRESH_BINARY)
ret,thresh4 = cv.threshold(img,128,255,cv.THRESH_BINARY)
ret,thresh5 = cv.threshold(img,256,255,cv.THRESH_BINARY)
titles = ['Original Image','k=10,T=0','k=10,T=35','k=10,T=65','k=10,T=128','k=10,T=255']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()