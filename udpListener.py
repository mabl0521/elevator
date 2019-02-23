import config
import socket
import threading

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


def myListener():
	UDP_IP = "127.0.0.1"
	UDP_PORT = 5005
 
	sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP Datagram
	sock.bind((UDP_IP, UDP_PORT))
 
	print ("starting udp listener")

	while True:
		msg, addr = sock.recvfrom(1024)	# buffer size is 1024 bytes
		print ("received message:", msg.decode())
		config.test=msg.decode()
		print (config.test)

threadlock = threading.Lock()
thread1= myThread(1,"Thread1", 1)
thread1.start()


def sendMessage(msg):
	UDP_IP = "127.0.0.1"
	UDP_PORT = 5005
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

	s.connect((UDP_IP, UDP_PORT))
	bytesToSend = str.encode(msg)

	s.send(bytesToSend)
	s.close()

sendMessage("hello ")
sendMessage("hello 2")






