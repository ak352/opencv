import numpy as np
import cv2
import sys

face_cascade = cv2.CascadeClassifier('../data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('../data/haarcascades/haarcascade_eye.xml')
#face_cascade = cv2.CascadeClassifier('../data/hand/palm.xml')

cap = cv2.VideoCapture(0)

while True:
    while True:
        ret, img = cap.read()
        resized = cv2.resize(img, (0,0), fx=0.2, fy=0.2)
        #cv2.imwrite("../example_data/canera1.jpg", img)


        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

        # Computer crashes when calling detectMultiScale 
        # on grayscale version of camera image. Why?
        #gray = None
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
#             x += (0.25*w)
#             w *= 0.6
#             y += (0.25*h)
#             h *= 0.6
            x,y,w,h = [int(k) for k in (x,y,w,h)]

            img = cv2.rectangle(resized, (x, y), (x+w, y+h), (255,0,0), 2)
            #roi_gray = gray[y:y+h, x:x+w]
            #roi_color = resized[y:y+h, x:x+w]
            #eyes = eye_cascade.detectMultiScale(roi_gray)
            #for (ex, ey, ew, eh) in eyes:
            #    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255,0), 2)

        #Subtract background to get rid of background artifacts during detection stage
        #Detect palm (later palm, fist or closed palm)
        #Use Camshift on color histogram and (perhaps KLT feature tracking (SIFT for scale of hand?))



        cv2.imshow('img', resized)
        key = cv2.waitKey(1)
        if np.array(faces).any() and key == ord('a'):
            break

        if int(key) == 27:
            break


    if np.array(faces).any():
        (x, y, w, h) = faces[0]
        x += (0.25*w)
        w *= 0.6
        y += (0.25*h)
        h *= 0.6
        x,y,w,h = [int(k) for k in (x,y,w,h)]
        
        track_window = (x,y,w,h)
        roi = resized[x:x+w, y:y+h]
        hsv_roi =  cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
        roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
        cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
        
        # Setup the termination criteria, either 10 iteration or move by atleast 1 pt
        term_crit =  (cv2.TERM_CRITERIA_COUNT + cv2.TERM_CRITERIA_EPS,20,0.03)
        
        while(1):
            ret ,frame = cap.read()
            frame = cv2.resize(frame, (0,0), fx=0.2, fy=0.2)
            if ret == True:
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)

                # apply meanshift to get the new location
                ret, track_window = cv2.CamShift(dst, track_window, term_crit)

                # Draw it on image
                pts = cv2.boxPoints(ret)
                pts = np.int0(pts)
                img2 = cv2.polylines(frame, [pts], True, 255,2)
                cv2.imshow('img',img2)

                #k = cv2.waitKey(0)
                k = cv2.waitKey(60) & 0xff
                if k == 27 or k == ord('a'):
                    break
                #else:
                #    cv2.imwrite(chr(k)+".jpg",img2)

            else:
                break
        if k == 27:
            break
        elif k == ord('a'):
            continue
        

cv2.destroyAllWindows()
cap.release()

