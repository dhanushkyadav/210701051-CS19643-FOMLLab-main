import cv2

#Trained Dataset
trainedDataset=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video=cv2.VideoCapture(0)
while True:
    Success, frame = video.read()
    if Success==True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
        faces = trainedDataset.detectMultiScale(gray)
        print(faces)
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imshow('video', frame)
        cv2.waitKey(1)
    else:
        print('video completed or frame null')
        break

