from socket import *
import threading
import time

HOST = 'localhost'
BUFSZ = 2048
def tcp_sp(port):
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
			t = threading.Thread(target=tcp_sp_thread, args=(c,))
			t.start()
			#t.join()
	
def tcp_sp_thread(s):
	print('s: client socket:',s)
	while True:
		data = s.recv(BUFSZ).decode()
		if not data:
			continue
		print('s:recv%s'%data)
		s.send(data.encode())
	
def tcp_cp(port, msg):
	s = socket(AF_INET, SOCK_STREAM)
	s.connect((HOST, port))
	while True:		
		s.send(msg.encode())
		print('c:send%s'%msg)
		time.sleep(2)
	s.close()

def udp_sp(port):
	s = socket(AF_INET, SOCK_DGRAM)
	s.bind((HOST, port))
	print('bind UDP on ', port)
	while True:
		data, addr = s.recvfrom(BUFSZ)
		print('s:',data.decode())
		s.sendto(data, addr)
		
def udp_cp(port, msg):
	s = socket(AF_INET, SOCK_DGRAM)
	while True:
		s.sendto(msg.encode(),(HOST, port))
		print('c:send', msg)
		print('c:recv', s.recv(BUFSZ).decode())
		time.sleep(1)