import config
import socket
import threading
from HallLampCallBack import HallLampCallBack

class myThread (threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		print ("Starting " + self.name)
		threadlock.acquire()
		myListener()
		threadlock.release()

	def stop(self):
		exit()


def myListener():
#	UDP_IP = "192.168.254.69"
	UDP_IP = "0.0.0.0"
	UDP_PORT = 5005
 
	sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP Datagram
	sock.bind((UDP_IP, UDP_PORT))
 
	print ("starting udp listener")

	while True:
		msg, addr = sock.recvfrom(1024)	# buffer size is 1024 bytes
		m = msg.decode('utf-8')
		#print (m)
		#print (addr)
		#if m == '':
		HallLampCallBack(int(m))
		#config.test=m
		#print (config.test)
		if m == 'quit':
			thread1.stop()
			pass


threadlock = threading.Lock()
thread1= myThread(1,"Thread1", 1)
thread1.start()

#text = "start"
#while text <> "end":
#	text = raw_input("prompt")  # Python 2
#	sendMessage(text)


#def sendMessage(msg):
#	UDP_IP = "192.168.254.70"
#	UDP_PORT = 5005
#	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

#	s.connect((UDP_IP, UDP_PORT))
#	bytesToSend = str.encode(msg)

#	s.send(bytesToSend)
#	s.close()


#text = "start"
#while text <> "end":
#        text = raw_input("prompt")  # Python 2
#        sendMessage(text)


#sendMessage("hello ")
#sendMessage("hello 2")
