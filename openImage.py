import cv2
import numpy as np

image=cv2.imread("001.jpg",0) #0 gri yapar

cv2.imshow("Dogukan Topallar vesikalık",image)

#cv2.imwrite("newImage.png",image)

cv2.waitKey(0)              #cıkıs fonksiyonları   
cv2.destroyAllWindows()     #cıkıs fonksıyonları