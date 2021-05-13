import numpy as np 
import cv2 as cv

image_name = "tree"
print("read an image from the file")
color_image = cv.imread("images/"+image_name+".jpg",cv.IMREAD_COLOR)

print("image in native color")
cv.imshow("Original_image",color_image)
cv.moveWindow("Original_image",0,0)

height, width, channels = color_image.shape

print("Split the image into three channels")
blue, green, red = cv.split(color_image)

cv.imshow("Blue Channel", blue)
cv.moveWindow("Blue Channel",0, height)

cv.imshow("green Channel", green)
cv.moveWindow("green Channel",0, height)

cv.imshow("red Channel", red)
cv.moveWindow("red Channel",0, height)

print("split the image into HSV")
hsv = cv.cvtColor(color_image, cv.COLOR_BGR2HSV)
h, s, v = cv.split(hsv)
hsv_image = np.concatenate((h,s,v), axis=1)
cv.imshow("Hue, Saturation, Value Image", hsv_image)

cv.waitKey(0)
cv.destroyAllWindows()
