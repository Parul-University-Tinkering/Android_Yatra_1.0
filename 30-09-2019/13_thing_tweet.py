############## STTP on IoT & MicroPython ####################
# Author:- Rutvik Mehta 
#Title:-   Speaking to twitter using thingspeak - Making tweets
#E-mail:- rutvik.mehta@paruluniversity.ac.in
#############################################################


import machine
import ussl as ssl                    #import ssl module from firmware
import network                        #import network module from firmware 
import time         #import time module from firmware

import urequests


API_KEY = "WZQWZAZ4CNVNX1N2"  

nic = network.WLAN(network.STA_IF)
nic.active(True)
print(nic.active())
nic.connect('Rutvik', 'blackpearl1234')
print(nic.isconnected())

adc = machine.ADC(0)
temp = adc.read()
temp = (temp/1024.0) * 3300
temp = str(temp/10) #Disable comment in case of LM35 temperature sensor
print(temp)

url = 'https://api.thingspeak.com/apps/thingtweet/1/statuses/update'
payload = "status=Hey current temperature is"+temp
headers = {"X-THINGSPEAKAPIKEY":API_KEY}
response = urequests.request('POST', url, headers = headers, data = payload)
print(response.text)
