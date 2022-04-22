#python FaceDe.py --video D:/test_hard.mp4
from ast import arg
from cv2 import waitKey
import face_recognition as fr 
import cv2
from sqlalchemy import true
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import cv2
import time
from imutils.video import FileVideoStream
import _thread


vid_path='D:/test_hard.mp4'

# construct the argument parse and parse the arguments
'''
# open a pointer to the video stream and start the FPS timer
stream = cv2.VideoCapture(vid_path)
time.sleep(1.0)
count=0
while True:  
    # Read the frame  
    _, img = stream.read()
    #if count==0: face_locations=fr.face_locations(img)
    #if count%4==0:
        #face_locations=fr.face_locations(img)
    #face_locations=fr.face_locations(image,model='cnn') dùng khi có GPU
    #print(len(face_locations))
    #for loc in face_locations:
        #cv2.rectangle(img, (loc[1], loc[0]), (loc[3], loc[2]), (0, 255, 0), 2)  
 
    # Display
    count+=1
    img=cv2.resize(img,(800,750))  
    cv2.imshow('Video', img)  
  
    # Stop if escape key is pressed  
    k = cv2.waitKey(30) & 0xff  
    if k==27:  
        break 
'''
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True,
	help="path to input video file")
args = vars(ap.parse_args())

# start the file video stream thread and allow the buffer to
# start to fill
frames=[]
minframe=30
def render_clip(threadName):
    global frames
    print(threadName)
    while fvs.more():        
        frame = fvs.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = np.dstack([frame, frame, frame])
        frame = imutils.resize(frame, width=450)
        # display the size of the queue on the frame

        # face_locations=fr.face_locations(frame)
        # for loc in face_locations:
        #     cv2.rectangle(frame, (loc[1], loc[0]), (loc[3], loc[2]), (0, 255, 0), 2)
        
        cv2.putText(frame, "Queue Size: {}".format(fvs.Q.qsize()),
            (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2) 
        frames.append(frame)
        print('rendering:'+str(len(frames)))
    

def showx(threadName):
    global minframe
    global frames
    print(threadName)
    if len(frames)>= minframe:
        print("Showing clip")
        minframe=0
        print(len(frames))
        for i in frames:
            cv2.imshow("Frame", i)
            #frames.remove(i)
            waitKey(1)

print("[INFO] starting video file thread...")
fvs = FileVideoStream(args["video"]).start()
count=0

      
#length = int(fvs.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
#print(length)
try:
    t1=_thread.start_new_thread( render_clip, ("Thread-1",) )
    time.sleep(30)
    while count<600:
        if(count <len(frames)):
            frame=frames[count]
            count+=1
            cv2.imshow("video",frame)
            waitKey(1)
        else:
            time.sleep(15)
        time.sleep(0.05)
except:
   print("Error: unable to start thread")





