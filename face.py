import cv2

#Trained Dataset
trainedDataset=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Read a Image
img=cv2.imread('images/ajithkumar.jpg')

#Convert into grayscale
gray=cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
faces=trainedDataset.detectMultiScale(gray)
print(faces)
for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow('ajithgrey',gray)
cv2.imshow('ajith',img)
cv2.waitKey()
