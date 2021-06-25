############## STTP on IoT & MicroPython ####################
# Author:- Rutvik Mehta 
#Title:-   To toggle (Blink) LED every 1s 
#E-mail:- rutvik.mehta@paruluniversity.ac.in
#############################################################

import network         #import network module from firmware


nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect('Rutvik','blackpearl1234')

import machine
import time
from umqtt.simple import MQTTClient
    
    # Publish test messages e.g. with:
    # mosquitto_pub -t foo_topic -m hello
led = machine.Pin(2, machine.Pin.OUT)
    # Received messages from subscriptions will be delivered to this callback
state = 0                   #initial state as 0

#call back function for subscribe
def sub_cb(topic, msg):
    global state
    print((topic, msg))
    if msg == b"on":
        led.value(0)
        state = 1

        c.publish(b"ACK", b"LED is ON")
        #c.disconnect()
        
    elif msg == b"off":
        led.value(1)
        state = 0

        c.publish(b"ACK", b"LED is off")
        #c.disconnect()
    elif msg == b"toggle":
            # LED is inversed, so setting it to current state
            # value will make it toggle
        led.value(state)
        state = 1 - state
        c.publish(b"ACK", b"LED is toggling")

    
c = MQTTClient("umqtt_client", "broker.hivemq.com") #provide "broker.hivemq.com" for IoT instead of IP address
c.set_callback(sub_cb)                          #calling call back function
c.connect()
c.subscribe(b"led")                             #subscribe topic as led


while True:
    
                # Non-blocking wait for message
  c.check_msg()
                # Then need to sleep to avoid 100% CPU usage (in a real
                # app other useful actions would be performed instead)
  time.sleep(1)
c.disconnect()
        
    


