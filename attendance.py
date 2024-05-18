
from pyzbar.pyzbar import decode
from pip import Image
import cv2
import time
import csv
video=cv2.VideoCapture(0)
student=[]
with open("1.csv","r")as file:
    render=csv.reader(file)
    for row in reader:
        student.append((row[1]))


while true:
    check,frame=video.read()
    d=decode(frame)
    try:
        for obj in d:
            name=d[0].data.decode()
            if name in student:
                student.remove(name)
                print("delected....")


    except:
        print("error")

    cv2.imshow("attendence",frame)
    key=cv2.waitKey(1)
    if key==ord("q"):
        print(student)
        break
video.release()
cv2.destroyAllWindows()