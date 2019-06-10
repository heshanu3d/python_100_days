from socket import *
import threading
import time

HOST = 'localhost'
LEN = 2048
def sp(port):
	s = socket(AF_INET, SOCK_STREAM)
	s.bind((HOST, port))
	s.listen()
	print('waiting connected...')
	while True:
		c, addr = s.accept()
		print(addr,' connected')
		if not c:
			s.close()
		else:
			t = threading.Thread(target=sp_thread, args=(c,))
			t.start()
			#t.join()
	
def sp_thread(s):
	while True:
		data = s.recv(LEN).decode()
		if not data:
			continue
		print('s:recv%s'%data)
		s.send(data.encode())
	
def cp(port, msg):
	s = socket(AF_INET, SOCK_STREAM)
	s.connect((HOST, port))
	while True:		
		s.send(msg.encode())
		print('c:send%s'%msg)
		time.sleep(2)
	s.close()