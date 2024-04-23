#sets up sensor to transmit data to GUI
#Modified example code from this site:
#https://people.csail.mit.edu/albert/bluez-intro/x232.html


import bluetooth

bd_address = "01:23:45:67:89:AB"

port = 1

socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
socket.connect((bd_addr, port))

socket.send("hello!!")

socket.close()