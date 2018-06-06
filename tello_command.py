sock = None
tello_address = None
recv = None

def send_addr(addr):
	global tello_address
	tello_address = addr

def send_obj(obj, obj2):
	global sock
	global recv
	sock = obj
	recv = obj2

def command(number):
	msg = "command"
	print number
	send(msg)
	
def Setspeed(number):
	msg = "speed" + " " + str(number[0])
	print number
	send(msg)
    
def takeoff(number):
	msg = "takeoff"
	print number
	send(msg)
	
def land(number):
	msg = "land"
	print number
	send(msg)
	
def up(number):
	msg = "up" + " " + str(number[0])
	print number
	send(msg)
	
def down(number):
	msg = "down" + " " + str(number[0])
	print number
	send(msg)
	
def flip(number):
	msg = "flip" + " " + str(number[0])
	print msg
	send(msg)
	
def left(number):
	msg = "left" + " " + str(number[0])
	print number
	send(msg)
	
def right(number):
	msg = "right" + " " + str(number[0])
	print number
	send(msg)
	
def forward(number):
	msg = "forward" + " " + str(number[0])
	print number
	send(msg)
	
def back(number):
	msg = "back" + " " + str(number[0])
	print number
	send(msg)

def cw(number):
	msg = "cw" + " " + str(number[0])
	print number
	send(msg)
	
def ccw(number):
	msg = "ccw" + " " + str(number[0])
	print number
	send(msg)
	
def speed(number):
	msg = "speed?"
	print number
	send(msg)
	
def battery(number):
	msg = "battery?"
	print number
	send(msg)
	
def time(number):
	msg = "time?"
	print number
	send(msg)

def exit(number):
	global sock
	global recv
	print("Closing socket...")
	sock.close()
	recv.terminate()
	exit()
	
	
def send (msg):
	global sock
	meg = msg.encode(encoding="utf-8") 
	sent = sock.sendto(msg, tello_address)