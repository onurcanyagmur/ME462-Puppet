from tkinter import *
import time 
import paho.mqtt.publish as publish 
#this package is for communicating with raspberry pi 
from PIL import ImageTk, Image
#this package is for showing an image on the GUI

root=Tk() #main GUI window   

root.title("Puppet GUI")

#since there are a total of 10 servos includig the dog , there 
#exists 
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()

def rshoulder(var1):
	global x
	x = int(var1)
	

def rupper(var2):
	global y
	y = int(var2)

def rlower(var3):
	global z
	z = int(var3)

def rleg(var4):
	global q 
	q = int(var4)
	

def lshoulder(var5):
	global m
	m = int(var5)
	

def lupper(var6):
	global n
	n = int(var6)

def llower(var7):
	global l
	l = int(var7)

def lleg(var8):
	global t 
	t = int(var8)

def dhead(var9):
	global p
	p = int(var9)

def dtail(var10):
	global r 
	r = int(var10)

def senddata():
	global message
	message = ""
	message = str(x)+","+str(y)+","+str(z)+","+str(q)+","+str(m)+","+str(n)+","+str(l)+","+str(t)+","+str(p)+","+str(r)
	publish.single('puppet/test',message,hostname='test.mosquitto.org')
	time.sleep(0.1)






Label(root, text="JOINT CONTROLS",font='Helvetica 15 bold').grid(row = 0, column = 10)

Label(root, text="Right Shoulder").grid(row=1, column=0)
right_shoulder = Scale(root,from_= 200,to_= 600,orient=HORIZONTAL,variable=var1,command=rshoulder).grid(row=2, columnspan = 10)

Label(root, text="Right Upper Arm").grid(row =3 , column =0 )
right_upper_arm = Scale(root,from_= 250,to_= 550,orient=HORIZONTAL,variable=var2,command=rupper).grid(row=4,columnspan = 10)

Label(root, text="Right Lower Arm").grid(row = 5, column = 0)
right_lower_arm = Scale(root,from_= 250,to_= 530,orient=HORIZONTAL,variable=var3,command=rlower).grid(row=6,columnspan = 10)

Label(root, text="Right Leg").grid(row = 7, column = 0)
right_leg = Scale(root,from_= 300,to_= 550,orient=HORIZONTAL,variable=var4,command=rleg).grid(row = 8 , columnspan=10)


Label(root, text="Left Shoulder").grid(row = 1 , column = 11)
left_shoulder = Scale(root,from_= 200,to_= 600,orient=HORIZONTAL,variable=var5,command=lshoulder).grid(row = 2 , column=11, columnspan=10)

Label(root, text="Left Upper Arm").grid(row = 3, column=11)
left_upper_arm = Scale(root,from_= 250,to_= 550,orient=HORIZONTAL,variable=var6,command=lupper).grid(row = 4, column = 11, columnspan=10)

Label(root, text="Left Lower Arm").grid(row = 5, column=11)
left_lower_arm = Scale(root,from_= 250,to_= 530,orient=HORIZONTAL,variable=var7,command=llower).grid(row = 6, column=11, columnspan=10)

Label(root, text="Left Leg").grid(row = 7, column=11)
left_leg = Scale(root,from_= 200,to_= 550,orient=HORIZONTAL,variable=var8,command=lleg).grid(row = 8, column=11, columnspan=10)

Label(root, text="Dog's Head").grid(row = 9, column=10)
dog_head = Scale(root,from_= 350,to_= 400,orient=HORIZONTAL,variable=var9,command=dhead).grid(row = 10, column=1, columnspan=10)

Label(root, text="Dog's Tail").grid(row = 11, column=10)
dog_tail = Scale(root,from_= 450,to_= 475,orient=HORIZONTAL,variable=var10,command=dtail).grid(row = 12, column=1, columnspan=10)



SEND = Button(root, text="SEND",font='Helvetica 18 bold', bg="green", fg="white", command=senddata).grid(row = 13,column = 10)
img = ImageTk.PhotoImage(Image.open('puppet2.jpg'))
panel = Label(root, image = img)
panel.grid(row=15,column=10)



root.mainloop()

print('goodbye')