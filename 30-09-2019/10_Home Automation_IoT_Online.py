############## STTP on IoT & MicroPython ####################
# Author:- Rutvik Mehta 
#Title:-   Home Automation Project - NoT - Using Relay
#E-mail:- rutvik.mehta@paruluniversity.ac.in
#############################################################
#import socket module from firmware

import machine
import time
from urllib import urequest as ur
import ujson

#function for wifi station
def wifi_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Rutvik', 'blackpearl1234')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    
   
   

wifi_connect()

#Initialize GPIO2 as D4 as output
led = machine.Pin(2, machine.Pin.OUT)

#code for online webpage by sending the request and getting the response
while True:
    response = ur.urlopen('https://rutvikmehtaiottets.000webhostapp.com/State.json')
    print(type(response))
    data = response.read().decode()
    print(type(data))
    parsed = ujson.loads(data)
    print(parsed)
    print(type(parsed))
    if (parsed["State"] == 'on'):
        led.off()
    else:
        led.on()


