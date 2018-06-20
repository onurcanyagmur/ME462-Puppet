from Tkinter import *

import time 
import paho.mqtt.publish as publish 

root=Tk()
root.title("Puppet GUI")

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()


def rshoulder():
	global x
	x = var1.get()
	

def rupper():
	global y
	y = var2.get()

def rlower():
	global z
	z = var3.get()

def rleg():
	global q 
	q = var4.get()
	

def lshoulder():
	global m
	m = var1.get()
	

def lupper():
	global n
	n = var2.get()

def llower():
	global l
	l = var3.get()

def lleg():
	global t 
	t = var4.get()


def senddata():
	global message
	message = ""
	message = x+","+y+","+z+","+q+","+m+","+n+","+l+","+t
	publish.single('puppet/test',command,hostname='test.mosquitto.org')
	time.sleep(0.1)






Label(root, text="Joint Controls").grid(row=0,columnspan=3,sticky=W)

Label(root, text="Right Shoulder").grid(row=1,columnspan=3,sticky=W)
right_shoulder = Scale(root,from_= 200,to_= 600,orient=HORIZONTAL,variable=var1,command=rshoulder).grid(row=2,columnspan=10)

Label(root, text="Right Upper Arm").grid(row=3,columnspan=3,sticky=W)
right_upper_arm = Scale(root,from_= 250,to_= 550,orient=HORIZONTAL,variable=var2,command=rupper).grid(row=4,columnspan=10)

Label(root, text="Right Lower Arm").grid(row=5,columnspan=3,sticky=W)
right_lower_arm = Scale(root,from_= 250,to_= 530,orient=HORIZONTAL,variable=var3,command=rlower).grid(row=6,columnspan=10)

Label(root, text="Right Leg").grid(row=7,columnspan=3,sticky=W)
right_leg = Scale(root,from_= 300,to_= 550,orient=HORIZONTAL,variable=var4,command=rleg).grid(row=8,columnspan=10)


Label(root, text="Left Shoulder").grid(row=9,columnspan=3,sticky=W)
left_shoulder = Scale(root,from_= 200,to_= 600,orient=HORIZONTAL,variable=var5,command=lshoulder).grid(row=10,columnspan=10)

Label(root, text="Left Upper Arm").grid(row=11,columnspan=3,sticky=W)
left_upper_arm = Scale(root,from_= 250,to_= 550,orient=HORIZONTAL,variable=var6,command=lupper).grid(row=12,columnspan=10)

Label(root, text="Left Lower Arm").grid(row=13,columnspan=3,sticky=W)
left_lower_arm = Scale(root,from_= 250,to_= 530,orient=HORIZONTAL,variable=var7,command=llower).grid(row=14,columnspan=10)

Label(root, text="Left Leg").grid(row=15,columnspan=3,sticky=W)
left_leg = Scale(root,from_= 200,to_= 550,orient=HORIZONTAL,variable=var8,command=lleg).grid(row=16,columnspan=10)


SEND = Button(root, text="SEND", bg="red", fg="white", command=senddata).grid(row=17,columnspan=5)




root.mainloop()