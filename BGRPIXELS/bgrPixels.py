import cv2
import numpy as np

image = cv2.imread("astranaut.jpg")
cv2.imshow("ASTRANAUT",image)

print(image)
print(image[(25,50)]) #BLUE, GREEN, RED color scale

print("İmage size: " + str(image.size))
print("features of the image: " + str(image.shape))
print("Data type of the image: " +str(image.dtype))




cv2.waitKey(0)
cv2.destroyAllWindows()