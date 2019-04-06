import json
import sys
import cv2
import pickle
import mysql.connector
#################################################################################
#file config defaut as dictinary
defaut_config = '{"server":{"host":"192.168.1.1","user":"levanlap", "password":30, "database":"New York"},"local":{"host":"localhost","user":"user", "password":25021993, "database":"New York"},"camera":{"name":"noname","id":0}}'
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
########################### DATA BASE ##########################################
try: 
  mydb = mysql.connector.connect(
    host=config["local"]["host"],
    user=config["local"]["user"],
    passwd=str(config["local"]["password"]))
  mycursor = mydb.cursor()
  print "connect localhost"
  mycursor.execute("SHOW DATABASES")
  myresult = mycursor.fetchall()
  for x in myresult:
    if x[0]=="detect_person":
         print "database ok"
         break
except:
  print "can not connect to server"

#################################################################################
#initilize camera
cap = cv2.VideoCapture(config["camera"]["id"])
if cap.isOpened():
    cap.open(config["camera"]["id"])
else: 
	print "camera is used by other program" 
	sys.exit(1)
############################SETTING LABEL#########################################
#font for text
font = cv2.FONT_HERSHEY_SIMPLEX
#read pickle file
labels = {}
with open("labels.pickle","rb") as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}
#print(labels)
print("Starting app...")
print("type: q keyboard to exit")
##################################################################################
#cascade classifier
face_cascade = cv2.CascadeClassifier('classifier/haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner/trainner_face.yml")
###################################################################################
################################ MAIN #############################################
###################################################################################
###################################################################################
while(True):
    # Capture frame-by-frame
    try:
        ret, frame = cap.read()
    except:
        break
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #--------------------------------------------
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
                
                #take gray of face
                roi_gray = gray[y:y+h, x:x+w]
                #check confident of gray in data train
                id_,conf = recognizer.predict(roi_gray)
                #print(conf) for debug
                if conf>=15 and conf <=80:
                    bel = labels[id_]
                    color = (0,255,0)
                else:
                    bel = "Unknow"
                    color = (0,0,255)
                #draw rectangle in face
                frame = cv2.rectangle(frame,(x,y),(x+w,y+h),color,2)
                #--------------------------------------------------------------
                cv2.putText(frame,bel,(x+10,y-10), font, 1,color,2,cv2.LINE_AA)
    # Display the resulting frame
    cv2.imshow('FACE DETECTION PROGRAM',frame)
    # Exit program
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
########################################################################################
###############################  END   #################################################
########################################################################################
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()