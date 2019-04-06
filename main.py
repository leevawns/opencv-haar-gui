import wx
#import mysql
from frame_main import mainframe,MyDialog_type_name
#################################################################################
#################################################################################
############################################################Aa#####################
import json
import sys
import cv2
import os
import pickle
#import mysql.connector
import numpy as np
import datetime
#from playsound import playsound
#################################################################################
###########################file config defaut as dictinary#######################
#################################################################################
defaut_config = '{"server":{"host":"192.168.1.1","user":"levanlap", "password":30, "database":"New York"},"local":{"host":"localhost","user":"user", "password":25021993, "database":"New York"},"camera":{"name":"noname","id":0}}'
#read config file
try:
    file_config = open("config.ini")
except:
    print("-create file config defaut")
    file_config = open("config.ini","w")
    file_config.write(defaut_config)
#take parameter config
try:
    config = json.loads(file_config.read())
except:
    config = json.loads(defaut_config)
################################################################################
########################### DATA BASE ##########################################
################################################################################
try:
  mydb = mysql.connector.connect(
    host=config["local"]["host"],
    user=config["local"]["user"],
    passwd=str(config["local"]["password"]))
  mycursor = mydb.cursor()
  print("connect localhost")
except:
  print("can not connect to server")
  #exit()
###############################################################################
id_name={"levanlap":"e6184","shiba":"e1111","bo":"7000","chung":"9000"}
this_time = "time_in"
list_time_in = []
list_time_out = []
################################################################################
sql_insert = "INSERT INTO `detect_person`.`history` (`id`, `name`,`time_in`, `time_out`) VALUES (%s, %s , %s, %s)"
#################################################################################
########################initilize camera#########################################
#################################################################################
cap = cv2.VideoCapture(config["camera"]["id"])
if cap.isOpened():
    cap.open(config["camera"]["id"])
else:
    print("camera is used by other program")
    sys.exit(1)
#################################################################################
############################SETTING SOUND########################################
#################################################################################
path_sound = {"levanlap":"audio/hi_lap_san.mp3","shiba":"audio/hi_shiba_san.mp3","bo":"audio/hi_bo_san.mp3","chung":"audio/hi_chung_san.mp3"}
#################################################################################
############################SETTING LABEL########################################
#################################################################################
font = cv2.FONT_HERSHEY_SIMPLEX
#read pickle file
labels = {}
print("Starting app...")
print("type: q keyboard to exit")
#################################################################################
###########################cascade classifier####################################
#################################################################################
face_cascade = cv2.CascadeClassifier('classifier/haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner/trainner_face.yml")
#################################################################################
################################ CLASS ##########################################
#################################################################################
class frame(mainframe):
    """docstring for ClassName"""
    def __init__(self, parent):
        mainframe.__init__(self,parent)
    def mainframeOnClose( self, event ):
        cap.release()
        cv2.destroyAllWindows()
        dialog.Destroy()
        self.Destroy()
    def m_menuItem_exitOnMenuSelection( self, event ):
        cap.release()
        cv2.destroyAllWindows()
        dialog.Destroy()
        self.Destroy()

    def m_menuItem_aboutOnMenuSelection( self, event ):
        wx.MessageBox("this is face recognizer program v1")

    def m_button_runOnButtonClick( self, event ):
        recognizer.read("trainner/trainner_face.yml")
        with open("labels.pickle","rb") as f:
            og_labels = pickle.load(f)
            labels = {v:k for k,v in og_labels.items()}
            #print(labels)
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
                #print(conf)
                if conf>=15 and conf <=60:
                    bel = labels[id_]
                    color = (0,255,0)
                    if this_time == "time_in":
                        if bel in list_time_in:
                            pass
                        else:
                            try:
                                playsound(path_sound[bel])
                            except:
                                pass
                                ############ SAVE DATABASE #############
                            list_time_in.append(bel)
                            #print "hello "+bel
                            try:
                                time_now = datetime.datetime.now()
                                val_insert = (id_name[bel], bel,time_now .strftime('%Y-%m-%d %H:%M:%S'),None)
                                mycursor.execute(sql_insert,val_insert)
                                mydb.commit()
                                print(mycursor.rowcount, "record inserted.")
                            except:
                                #print "error insert"
                                pass
                    else:
                        if bel in list_time_out:
                            pass
                        else:
                            try:
                                playsound(path_sound[bel])
                            except:
                                pass
                                ############ SAVE DATABASE #############
                            list_time_out.append(bel)
                            #print "googbye "+bel
                            try:
                                time_now = datetime.datetime.now()
                                val_insert = (id_name[bel], bel,time_now .strftime('%Y-%m-%d %H:%M:%S'),None)
                                mycursor.execute(sql_insert,val_insert)
                                mydb.commit()
                                print(mycursor.rowcount, "record inserted.")
                            except:
                                #print "error insert"
                                pass
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
        cv2.destroyAllWindows()
    def m_button_train_datasetOnButtonClick( self, event ):
        y_labels = []
        x_train = []
        #get dir of folder program
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        image_dir = os.path.join(BASE_DIR,"images")
        current_id = 0
        label_ids ={}
        for root,dirs,files in os.walk(image_dir):
            for file in files:
               if file.endswith("png") or file.endswith("jpg"):
                    path = os.path.join(root,file)
                    label = os.path.basename(root).replace(" ","-").lower()
                    if label in label_ids:
                        pass
                    else:
                        label_ids[label] = current_id
                        current_id += 1
                    id_ = label_ids[label]
                    try:
                        image_array = cv2.imread(path,0)
                    except:
                        continue
                    faces = face_cascade.detectMultiScale(image_array, 1.3, 5)
                    #if face is detect, append to x_train array, y_labels array
                    for(x,y,w,h) in faces:
                        roi = image_array[y:y+h,x:x+w]
                        x_train.append(roi)
                        y_labels.append(id_)
                    cv2.imshow("TRAINING",image_array)
        with open("labels.pickle","wb") as f:
            pickle.dump(label_ids,f)
        recognizer.train(x_train,np.array(y_labels))
        recognizer.save("trainner/trainner_face.yml")
        cv2.destroyAllWindows()
        wx.MessageBox("FINISH TRAINING DATA")
        #print "finish"
    def m_button_create_datasetOnButtonClick( self, event ):
        dialog.Show()

class dialog_type_name(MyDialog_type_name):
    def __int__(self,parent):
        MyDialog_type_name.__int__(self,parent)
    def m_sdbSizerOnCancelButtonClick( self, event ):
        event.Skip()

    def m_sdbSizerOnOKButtonClick( self, event ):
        name = self.m_textCtrl.GetLineText(0)
        i=0
        j=0
        offset = 50
        if name == "":
            wx.MessageBox("type your name please !")
        else:
            dialog.Show(False)
            path = "images/"+name
            if os.path.exists(path):
               print("folder is exists")
            else:
               print("folder is created")
               os.mkdir(path)
            for root,dirs,files in os.walk(path):
               for file in files:
                   j += 1
            while True:
                ret,img = cap.read()
                gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray,1.2,5)
                for (x,y,w,h) in faces:
                   i +=1
                   cv2.imwrite(path+"/"+name+str(i+j)+".jpg",gray[y-offset:y+h+offset,x-offset:x+w+offset])
                   cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),1)
                   cv2.putText(img,"sample"+str(i),(x,y), font, 1,(0,0,255),2,cv2.LINE_AA)
                   cv2.imshow("create dataset face",img)
                cv2.waitKey(100)
                if i>=50:
                   cv2.destroyAllWindows()
                   wx.MessageBox("create dataset finish")
                   break
###################################################################################
################################ MAIN #############################################
###################################################################################
app = wx.App()
#-------------------------------
frame = frame(None)
dialog = dialog_type_name(None)
#-------------------------------
frame.Show()
#-------------------------------
app.MainLoop()