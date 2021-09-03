import cv2
import numpy
import pandas as pd
import numpy as np
import math

image=cv2.imread('starfield_bright.jpg',0)
df = pd.read_csv('starsReal.csv')
y,x=image.shape

black = 1 * np.ones((y,x,3), np.uint8)

X_coordinate=df[df.columns[0]]
Y_coordinate=df[df.columns[1]]
#print(len(X_coordinate))
#print(Y_coordinate.shape)
L=int(40/2)
radius=[]
count=0
#while(count!=len(X_coordinate)):
for each in range(len(X_coordinate)):
    x = int(X_coordinate[each])
    y = int(Y_coordinate[each])
    cropped = image[y - L:y + L, x - L:x + L]
    _, threshold = cv2.threshold(cropped, 127, 255, cv2.THRESH_BINARY, dst=None);
    contours = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
    if contours:
        contours=contours[0]
        area = cv2.contourArea(contours)
        R = math.sqrt(area / math.pi)
        R = math.ceil(R)
        if R>10:
            R=20
        if R==0:
            R=3
        radius.append(R)

        #print(each)
        cv2.circle(black, (x, y), R, (255, 255, 255), -1)

#cv2.imwrite('out.png',cropped)
cv2.imwrite('out.png',black)
cv2.waitKey(0)
cv2.destroyAllWindows()
