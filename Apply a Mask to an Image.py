import cv2 as cv
# Read the output from Kmeans
img_Kmeans = cv.imread('pictures/saved_new_K6.jpg')
img_Kmeans_gray = cv.cvtColor(img_Kmeans, cv.COLOR_BGR2GRAY)

#Make a Binary treshould
ret,thresh1 = cv.threshold(img_Kmeans_gray,128,255,cv.THRESH_BINARY)


# Loop to turn all Zeros to one and 255 to Zeros
for x in range(thresh1.shape[0]):
    for y in range(thresh1.shape[1]):
        if thresh1[x,y]==0: thresh1[x,y]=1
        else: thresh1[x,y]=0

# Read main photo and make a copy
img_Original=cv.imread("pictures/kids1.jpg")
img_Original_Copy=img_Original.copy()

#Multiple the mask to the copy of the origin file
for x in range(thresh1.shape[0]):
    for y in range(thresh1.shape[1]):
       img_Original_Copy[x,y]=img_Original[x,y]*thresh1[x,y]


# Merge the origin and masked photo
img_Hconcat=cv.hconcat([img_Original,img_Original_Copy])


#Show the result
cv.imshow('result',img_Hconcat)
cv.waitKey(0)
cv.destroyAllWindows()