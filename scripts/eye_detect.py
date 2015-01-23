import numpy as np
import cv2
import sys

eye_cascade = cv2.CascadeClassifier('../data/haarcascades/haarcascade_eye.xml')

img = cv2.imread(sys.argv[1])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
eyes = eye_cascade.detectMultiScale(gray)
for (x,y,w,h) in eyes:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
