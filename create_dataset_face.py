import cv2
import os
cam = cv2.VideoCapture(0)
facecascade =cv2.CascadeClassifier("classifier/haarcascade_frontalface_default.xml")
i=0
j=0
offset = 50
name = raw_input("enter your name:")
#creat folder in images folder
path = "images/"+name
if os.path.exists(path):
	print("folder is exists")
else:
    print("folder is created")
    os.mkdir(path)
print(path)
#count image sample in folder
for root,dirs,files in os.walk(path):
   for file in files:
   	   j += 1	   
while True:
	ret,img = cam.read()
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces = facecascade.detectMultiScale(gray,1.2,5)
	for (x,y,w,h) in faces:
		i +=1
		cv2.imwrite(path+"/"+name+str(i+j)+".jpg",gray[y-offset:y+h+offset,x-offset:x+w+offset])
		cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),1)
		cv2.imshow("create dataset face",img)
		cv2.waitKey(100)
	print(i)
	if i>=50:
		cam.release()
		cv2.destroyAllWindows()
		break