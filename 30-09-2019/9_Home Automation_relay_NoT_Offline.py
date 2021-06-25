############## STTP on IoT & MicroPython ####################
# Author:- Rutvik Mehta 
#Title:-   Home Automation Project - NoT - Using Relay
#E-mail:- rutvik.mehta@paruluniversity.ac.in
#############################################################
#import socket module from firmware

try:
  import usocket as socket
except:
  import socket
#import network module from firmware

import machine
import network
#Setting ESP8266 in AP Mode
ap_if = network.WLAN(network.AP_IF)
ap_if.active(True)
print(ap_if.ifconfig())
led = machine.Pin(16, machine.Pin.OUT)
def web_page():
  if led.value() == 1:
    gpio_state="ON"
  else:
    gpio_state="OFF"
  
  html = """<html><head> <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}</style></head><body> <h1>ESP Home Automation</h1> 
  <h2> Howdy developers!!</h2><p>Author: Rutvik Mehta </p><h1> It's A@br@ c@ d@br@ time<p>GPIO state: <strong>""" + gpio_state + """</strong></p><p><a href="/?led=on"><button class="button">ON</button></a></p>
  <p><a href="/?led=off"><button class="button button2">OFF</button></a></p></body></html>"""
  return html

#creating tcp stream socket
#AF_INET is for ipv4. Change it to AF_INET6 for ipv6.SOCK_STREAM is for TCP Socket.
#UDP sockets can be create using AF_DGRAM

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#binding port 80 with default addrss of esp8266 - port 80 is reserved for web communication
s.bind(('192.168.4.1', 80))
#listing for incoming connection
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  led_on = request.find('/?led=on')
  led_off = request.find('/?led=off')
  if led_on == 6:
    print('LED ON')
    led.value(1)
  if led_off == 6:
    print('LED OFF')
    led.value(0)
  response = web_page()
  conn.send(response)
  conn.close()







