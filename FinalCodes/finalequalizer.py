import pyaudio
import numpy as np
import paho.mqtt.publish as publish
import time

CHUNK = 2**11
RATE = 44100

p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True, input_device_index =8,frames_per_buffer=CHUNK)

averageAmount=100;	#ADJUST THESE PARAMETERS 
levelScale=2;
levelMargin=50;
rangeAmount=int(10*44100/1024) #Be careful with this, IT CAN UPDATE LEVEL INFORMATION MORE FREQUENTLY IF IT IS LOWER, IT MAY BE BETTER JUST CHECK IT OUT
sleepMargin=0.01;	#ADJUST UP TO HERE SLEEP SEEMS FINE JUST CHECK IT OUT
while True:
	average=0;
	count=0;
	for i in range(rangeAmount): #go for a few seconds #TRY DECREASING THIS RANGE AS WELL,

		data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
		peak=np.average(np.abs(data))*2
		bars="#"*int(50*peak/2**16)
		if(count<averageAmount):	#THIS IS LISTENING PERIOD TO GET AN AVERAGE OF LEVEL
			print("Listening ATM {0} \n".format(count))
			average=average+peak/averageAmount
			count+=1
		else:
			if(peak>average*levelScale+levelMargin):
				print("Boom Boom")
				message=str(peak)
				publish.single('puppet/test',message,hostname='test.mosquitto.org')
				time.sleep(sleepMargin)



stream.stop_stream()
stream.close()
p.terminate()