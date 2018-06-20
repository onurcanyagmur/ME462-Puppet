import os
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

import puppet 
import puppet2 
import puppet3 
from puppet import *
from puppet2 import *
from puppet3 import *
#Init gpio's for led
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)

#Define count for messages
mycount=0;
#Define definitions for action libs(puppet,puppet2,puppet3)
def removethings(k):
    mylist=['Adafruit_PCA9685', '__builtins__', '__doc__', '__file__', '__name__', '__package__','servo_max', 'servo_min', 'set_servo_pulse', 'setpos','pwm','time']
    for i in range(0,len(mylist)):
        k.remove(mylist[i]);
    return k;
list1=dir(puppet)
list2=dir(puppet2)
list3=dir(puppet3)
list1=removethings(list1)
list2=removethings(list2)
list3=removethings(list3)
print(list1)
print(list2)
print(list3)
list1=list1+list2+list3
print(list1);

hellolist=['hello','hi']
#GPIO.cleanup()

def lightup():
    GPIO.output(37, GPIO.LOW)
    GPIO.output(38, GPIO.HIGH)

def set_count_one():
    global mycount
    mycount=1;
def set_count_zero():
    global mycount
    mycount=0;
set_count_zero();
def checkmsg():
    
    for i in range(0,len(hellolist)):
        if((str(message)).__contains__(hellolist[i])):
            lightup()
    for i in range(0,len(list1)):
        if((str(message)).__contains__(list1[i])):
            globals()[list1[i]]();
           
def on_message(client, userdata, msg):
	global message;
	message=str(msg.payload);
	if(mycount%2==1):
            checkmsg()
            #Checkmsg is over here
            set_count_zero();
        else:
            checkmsg()
            message='say {0}'.format(message)
            os.system(message)
            set_count_one();
	print(message)

def on_connect(client, userdata, flags ,rc):
    print("Connected")
    client.subscribe("puppet/test")

client=mqtt.Client()
client.on_connect=on_connect;
client.on_message=on_message;

client.connect("test.mosquitto.org",1883,60)
client.loop_forever()




