#Hotai-chan

import osc_receive, event
import tello_command as t
receiver = osc_receive.OscReceive(20001)

def foo(vals):
  for val in vals:
    print(val)


# start from tello3.py


# Tello Python3 Control Demo
#
# http://www.ryzerobotics.com/
#
# 1/1/2018

import threading
import socket
import sys
import time


host = ''
port = 9000
locaddr = (host,port)


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break


print ('\r\n\r\nTello Python3 Demo.\r\n')

print ('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')

print ('end -- quit demo.\r\n')


#recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()

# end from tello3.py



event.add("/foo",foo)
receiver.setup("/foo")

# Hotai add >>tello command<<

t.send_addr(tello_address)
t.send_obj(sock, receiver)

event.add("/command",t.command)
receiver.setup("/command")

event.add("/Setspeed",t.Setspeed)
receiver.setup("/Setspeed")

event.add("/takeoff",t.takeoff)
receiver.setup("/takeoff")

event.add("/land",t.land)
receiver.setup("/land")

event.add("/up",t.up)
receiver.setup("/up")

event.add("/down",t.down)
receiver.setup("/down")

event.add("/flip",t.flip)
receiver.setup("/flip")

event.add("/left",t.left)
receiver.setup("/left")

event.add("/right",t.right)
receiver.setup("/right")

event.add("/forward",t.forward)
receiver.setup("/forward")

event.add("/back",t.back)
receiver.setup("/back")

event.add("/cw",t.cw)
receiver.setup("/cw")

event.add("/ccw",t.ccw)
receiver.setup("/ccw")

event.add("/flip",t.flip)
receiver.setup("/flip")

event.add("/speed",t.speed)
receiver.setup("/speed")

event.add("/battery",t.battery)
receiver.setup("/battery")

event.add("/time",t.time)
receiver.setup("/time")

event.add("/exit",t.exit)
receiver.setup("/exit")


# end


try:
    while True:
        pass

except KeyboardInterrupt:
    receiver.terminate()
    exit()
