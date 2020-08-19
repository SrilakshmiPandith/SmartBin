import time
import pyrebase
import  RPi.GPIO  as GPIO
import datetime
trigger_pin = 18
echo_pin = 16
GPIO.setmode(GPIO,BCK)
GPIO.setup(trigger_pin,GPIO.OUT)
GPIO.setup(echo_pin,GPIO.IN)
now=datetime.datetime.now()
dt=now.strftime(“%Y-%m-%d %H:%M:%S”)
config={“apiKey”: “api-key from firebase”,
“authDomain”: “authDomain from firebase”,
“databaseURL”: “database url”,
“storageBucket”: “storageBucket”}
Def send_trigger_pulse():
               GPIO.output(trigger_pin,True)
               time.sleep(0.0001)
def  wait_for_echo(value,timeout):
               count = timeout
               while  GPIO.input(echo_pin) = value and count > 0:
                           count = count-1

def  get_distance():
                 send_trigger_pulse()
                 wait_for_echo(True,10000)
                 start a time,time()
                 wait_for_echo(False,10000) 
            finish a time,time()
                 pulse_len = finish-start
                  distance_cm = pulse_len
                  return (distance_cm)
                  ********** GPIO setting ***********

GPIO.setup(11,GPIO.IN)
GPIO.setup(12,GPIO.OUT)

          ************** setting up MQTT **************
Def  on_connect(client,userdata,flags,rc):
      print ‘connection made’ , client,  userdata, flags, rc
      (result,mid) = client.subscribe(“paho/abc3”)
Def on_message(client,userdata,mag):
       print(msg.topic-“ “-str(msg.payload))
       data = int(msg.payload)	
       print(“data_my=%d” %data)
        GPIO.output(12,data)

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect(“iot.eclipse.org”,1883,60)
mqttc.loop_start()
********* Getting the status of the  bin ***********
While 1:
        a=get_distance()
        if(a>=15):
            msg= “Bin is empty”
            firebase=pyrebase.initialize_app(config)
            db=firebase.database()
            data= {“date”: dt, “msg”: msg}
            db.child(“users”).push(data)
            time.sleep(10)
      elif(a<=5):
            msg= “Bin is full, please collect”
            firebase=pyrebase.initialize_app(config)
            print(firebase)
            db=firebase.database()
            data= {“date”: dt, “msg”: msg}
            db.child(“users”).push(data)
            time.sleep(10)
