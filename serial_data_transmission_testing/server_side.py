#sets up device running GUI to recieve sensor data
#and send data requests
#Modified example code from this site:
#https://people.csail.mit.edu/albert/bluez-intro/x232.html
#this code assumes a uniform dose for all alarms

import bluetooth
from time import localtime, asctime, sleep

alert_times = []    #times for alarm to go off

#set up bluetooth socket
server_socket = bluetooth.BluetoothSocket( bluetooth.RFCOMM )

#search for connection
port = 1
server_socket.bind(("",port))
server_socket.listen(1)

client_socket, address = server_socket.accept()
print("Accepted connection from ",address)

#accept data
data = client_socket.recv(1024)
print(f"received {data}")

#close
client_socket.close()
server_socket.close()