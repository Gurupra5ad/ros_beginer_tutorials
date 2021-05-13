import numpy as np
import cv2

image_name = "tree"
print("read an image from file")
img = cv2.imread("images/"+image_name+".jpg")
cv2.imshow("Image",img)
print("Press a key inside the image to make a copy")
cv2.waitKey(0)
print("Image copied successfully to folder images/copy")
cv2.imwrite("images/copy/"+image_name+"copy.jpg",img)
