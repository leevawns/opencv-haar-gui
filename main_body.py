import json
import sys
import cv2
import pickle
#file config defaut as dictinary
defaut_config = '{"server":{"host":"192.168.1.1","user":"levanlap", "password":30, "database":"New York"},"local":{"host":"192.168.1.1","user":"levanlap", "password":30, "database":"New York"},"camera":{"name":"noname","id":0}}'
#read config file
try:
    file_config = open("config.ini")
except:
	print "-create file config defaut"
	file_config = open("config.ini","w")
	file_config.write(defaut_config)
#take parameter config
try:
	config = json.loads(file_config.read())
except:
    config = json.loads(defaut_config)

#initilize camera
cap = cv2.VideoCapture(config["camera"]["id"])
if cap.isOpened():
    cap.open(config["camera"]["id"])
else: 
	print "camera is used by other program" 
	sys.exit(1)
#font for text
font = cv2.FONT_HERSHEY_SIMPLEX
#cascade classifier
upperbody_cascade = cv2.CascadeClassifier('classifier/haarcascade_upperbody.xml')
face_cascade = cv2.CascadeClassifier('classifier/haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner/trainner_face.yml")
#read pickle file
labels = {}
with open("labels.pickle","rb") as f:
	og_labels = pickle.load(f)
	labels = {v:k for k,v in og_labels.items()}
#print(labels)
print("Starting app:")
print("type: q keyboard to exit")
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #--------------------------------------------
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    bodys = upperbody_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in bodys:
                frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    for (x,y,w,h) in faces:
                frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    # Display the resulting frame
    cv2.imshow('BODY DETECT',frame)
    # Exit program
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()