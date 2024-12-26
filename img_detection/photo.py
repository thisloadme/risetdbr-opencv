import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('jokowi2.jpg')
# img = cv2.resize(img, (150, 150))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
    print(x)
    print(y)
    print(w)
    print(h)

    crop_img = img[y:(y+h), x:(x+w)]

    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('img',img)
# cv2.imshow('crop_img',crop_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
quit()