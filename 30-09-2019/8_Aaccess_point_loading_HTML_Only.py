############## STTP on IoT & MicroPython ####################
# Author:- Rutvik Mehta 
#Title:-   making esp8266 access point - serving HTML
#E-mail:- rutvik.mehta@paruluniversity.ac.in
#############################################################
#import socket module from firmware
try:
  import usocket as socket
except:
  import socket
#import network module from firmware

import network
#Setting ESP8266 in AP Mode
ap_if = network.WLAN(network.AP_IF)
ap_if.active(True)
print(ap_if.ifconfig())

def web_page():
  html = """<html>
            <head> 
            <title>ESP as access point</title> 
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="icon" href="data:,"> 
             <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
                    h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}</style></head>
                    <body> 
                        <h1>ESP as station</h1>
                        <h2> Author : Rutvik Mehta </h2>
                        <p> Howdy Developers !!!</p>
                        <strong> Enjoying Session? </strong>
                        <p>How's the Josh?</p>
                        <p> If high !! Shout High sir!!</p>
                    </body>
            </html>"""
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
  response = web_page()
  conn.send(response)
  conn.close()


