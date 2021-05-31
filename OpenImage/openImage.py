import cv2
import numpy as np

image=cv2.imread("001.jpg",0) # makes "0" grey

cv2.imshow("Dogukan Topallar vesikalik",image) #show image"001.jpg"

print(image)        #how many pixels - with matrix
print(image.size)   #size output
print(image.dtype)  #data informations
print(image.shape)  #width, height, how many channels are used
                    #When the gray picture is made, the channel is not specified
                    #in this way, memory and speed are advantageous


cv2.waitKey(0)              #function used to log out
cv2.destroyAllWindows()     #function used to log out