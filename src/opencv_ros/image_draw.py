import numpy as np 
import cv2 

image = np.zeros((512,512,3), np.uint8)
#CV2.LINE(image, start_point, End_point, color, thickness) Same goes for everything
cv2.line(image,(0,0),(511,511), (255,255,255),5) 

cv2.rectangle(image,(384,0),(510,128),(0,255,0),3) 
cv2.ellipse(image,(256,256),(100,50),0,0,180,255,-1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape(-1,1,2)
cv2.polylines(image, [pts],True,(0,255,255))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, 'ROS,OPENCV',(10,500),font, 2, (255,255,255),2,cv2.LINE_AA)

cv2.imshow("Image Panel", image)
cv2.waitKey(0)
cv2.destroyAllWindows()