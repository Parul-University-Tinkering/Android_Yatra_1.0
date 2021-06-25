
############## STTP on IoT & MicroPython ####################
# Author:- Rutvik Mehta 
#Title:-   Home Automation Project - NoT - Using Relay
#E-mail:- rutvik.mehta@paruluniversity.ac.in
#############################################################


import usocket as _socket             #import usocket as _socket
import machine
import ussl as ssl                    #import ssl module from firmware
import network                        #import network module from firmware 
import time         #import time module from firmware
#sensor = dht.DHT11(machine.Pin(6))
#sensor.measure()  
pin1 = machine.Pin(16, machine.Pin.OUT)
pin2 = machine.Pin(4, machine.Pin.OUT)
pin1.off()
pin2.off()
#function for identify wifi
nic = network.WLAN(network.STA_IF)
nic.active(True)
print(nic.active())
nic.connect('Rutvik', 'blackpearl1234')
print(nic.isconnected())
  
  

temp = 0 

#API_KEY for Write & HOST as www.thingspeak.com
API_KEY = "HTSIBI487CHK2XVK"  
HOST = "api.thingspeak.com"


#takes the value from sensor and send it to HOST
while True:

    #sense the Data from the sensor
    adc = machine.ADC(0)
    temp = adc.read()
    temp = (temp/1024.0) * 3300
    temp = temp/10 #Disable comment in case of LM35 temperature sensor
    print(temp)
    if temp > 35:
      pin1.on()
      pin2.on()
    else:
      pin1.off()
      pin2.off()
    #Send the data to the HOST 
    data = b"api_key="+ API_KEY + "&field1=" + str(temp)  
    s = _socket.socket()
    ai = _socket.getaddrinfo(HOST, 443)  
    #Connecting to the HOST
    print(ai)
    
    addr = ai[0][-1]
    print(addr)
    s.connect(addr)
    s = ssl.wrap_socket(s)
    s.write("POST /update HTTP/1.0\r\n")
    s.write("Host: " + HOST + "\r\n")
    s.write("Content-Length: " + str(len(data)) + "\r\n\r\n")
    s.write(data)
    print(s.read(128))
    #print("Temperature = ", sensor.temperature())      #display temperature value 
    #print("Humidity= ", sensor.humidity())             #display humidity value
    s.close()
    time.sleep(1)








