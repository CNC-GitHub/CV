import cv2
import numpy as np
# Read the output from Kmeans
img_Mask = cv2.imread('Pictures/Mask1.jpeg')
img_Mask_gray = cv2.cvtColor(img_Mask, cv2.COLOR_BGR2GRAY)

#Make a Binary treshould
ret,thresh1 = cv2.threshold(img_Mask_gray,128,255,cv2.THRESH_BINARY)

# Loop to turn all Zeros to one and 255 to Zeros
for x in range(thresh1.shape[0]):
    for y in range(thresh1.shape[1]):
        if thresh1[x,y]==0: thresh1[x,y]=1
        else: thresh1[x, y] = 0
# Shape[0] is the height and shape[1] is the width
height = int(thresh1.shape[0])
width = int(thresh1.shape[1])
# for resize function width is 1st parameter and height is the 2nd parameter
dim = (width, height)
camera = cv2.VideoCapture(0)
while True:
    ret,snapshot = camera.read()
    snapshot=cv2.resize(snapshot,dim)
    snapshot_gray=cv2.cvtColor(snapshot, cv2.COLOR_BGR2GRAY)
    for x in range(thresh1.shape[0]):
        for y in range(thresh1.shape[1]):
            snapshot_gray[x, y] = snapshot_gray[x, y] * thresh1[x, y]
    cv2.imshow('Result', snapshot_gray)
    if cv2.waitKey(1) == 13:  # 13 is the Enter Key
        break
    # Release camera and close windows
cap.release()
cv2.destroyAllWindows()