import threading
from net_util import *

def test_tcp1():
#use 10 server, 10 client
	for i in range(10):
		t = threading.Thread(target=tcp_sp,args=(5000+i,))
		t.start()
		time.sleep(0.1)
		t = threading.Thread(target=tcp_cp,args=(5000+i,'%d-abc'%i,))
		t.start()

def test_tcp2():
#use 1 server, 10 client
	t = threading.Thread(target=tcp_sp,args=(5000,))
	t.start()
	for i in range(10):
		t = threading.Thread(target=tcp_cp,args=(5000, '%d-abc'%i,))
		t.start()
		time.sleep(0.2)

def test_udp():
	t = threading.Thread(target=udp_sp,args=(5000,))
	t.start()
	for i in range(10):
		t = threading.Thread(target=udp_cp,args=(5000, '%d-abc'%i,))
		t.start()
		time.sleep(0.2)
def main():
	#test_tcp1()
	#test_tcp2()
	test_udp()
	
if __name__ == '__main__':
	main()