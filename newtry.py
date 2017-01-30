import numpy as np
import cv2
from __builtin__ import bool
from ctypes.wintypes import BOOLEAN


# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
class EyeBlinkDetector:	
	def blink(self):
		
		face_cascade = cv2.CascadeClassifier('classifiers/haarcascade_frontalface_default2.xml')
		#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
		eye_cascade = cv2.CascadeClassifier('classifiers/haarcascade_eye2.xml')
		
		cap = cv2.VideoCapture(0)
		i=0
		cl=[]
		while 1:
		    ret, img = cap.read()
		    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		    faces = face_cascade.detectMultiScale(gray, 1.3,5)
		    i=i+1
		    if i%100==0:
		    	print len(cl)
		    	if len(cl)>10:
		    		print "ALERTALERTALERTALERTALERTALERTALERTALERT",i
		    		break
		        cl=[]
		    
		    '''
		    eyes = eye_cascade.detectMultiScale(gray,1.3,5)
		    print eyes 
		    blink=False
		    if (len(eyes)==0):
		        blink = True
		        print "blinked"
		        	
		    else:
		       	print "open bro"
		    for (ex,ey,ew,eh) in eyes:
		        cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
		    cv2.imshow('img',img)
		    k = cv2.waitKey(30) & 0xff
		    if k == 27:
		        break
		
		    
		'''
		    for (x,y,w,h) in faces:
		        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		        roi_gray = gray[y:y+h, x:x+w]
		        roi_color = img[y:y+h, x:x+w]
		        
		        eyes = eye_cascade.detectMultiScale(roi_gray)
		        blink=False
		        if (len(eyes)==0):
		        	blink = True
		        	print "close",i
		        	cl.append("1")
		        else:
		        	print "open",i
		        	print eyes
		        for (ex,ey,ew,eh) in eyes:
		            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
		
		    cv2.imshow('img',img)
		    k = cv2.waitKey(30) & 0xff
		    if k == 27:
		        break
		
		cap.release()
		cv2.destroyAllWindows()
		
cd=EyeBlinkDetector()
cd.blink()