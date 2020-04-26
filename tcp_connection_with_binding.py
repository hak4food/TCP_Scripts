import socket

class SOC: 

	socketConn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	szMsg = 0

	def __init__ (self, hostname, portN, szMsg):
		self.hostname = hostname
		self.portN = portN
		self.szMsg = szMsg


	def displayHost(self):
		print("Hostname: ", self.hostname, " PortNumber: ", self.portN )

	def httpGet(self, INST='GET', FNAME=''):
		return INST + " /" + FNAME + "HTTP/1.1\r\n\n"

	def timeOut(self,time=10):
		self.time=time
		SOC.socketConn.settimeout(time)

	def binding(self,networkInterface='',listenPort=6):
		self.networkInterface=networkInterface
		self.listenPort=listenPort
		SOC.socketConn.bind((networkInterface,listenPort))

	def sendMsg(self,Message):
		self.Message = Message
		SOC.socketConn.send(Message)

	def sendRcv(self):
		data = SOC.socketConn.recv(self.szMsg)
		print("received data: ", data.decode('utf-8'))

	def connectServer(self):
		try:
			SOC.socketConn.connect((self.hostname,self.portN))
			print ("Successful connection")

		except socket.error as err:
			print ("Caught exception socket.error : %s" % err)


	def connectionClose(self):
		SOC.socketConn.close()


def main():
	website = 'xxx.com'
	for lwrPort in range(1,1023):
		connect1 =  SOC("",8101,4096)
		connect1.displayHost()
		connect1.timeOut()
		connect1.binding('',lwrPort)
		connect1.connectServer()
		connect1.sendMsg( b'GET /flag.txt HTTP/1.1\r\n\n')
		connect1.sendRcv()
		connect1.connectionClose()
		del connect1



if __name__ == "__main__":
	main()
	print("end of program")



#Bryan Gonzalez
#gonzalez.bryan@gmail.com
#MIT LICENSE
