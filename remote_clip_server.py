#!/usr/bin/env python
import socket
from subprocess import Popen, PIPE

port = 43516
eof = '\0'

def read_data(socket):
	data = ''
	while True:
		chunk = socket.recv(512)
		idx = chunk.find(eof)
		if idx > -1:
			data += chunk[:idx]
			return data
		else:
			data += chunk

def copy_to_clipboard(data):
	p = Popen('pbcopy', stdin = PIPE)
	p.stdin.write(data)
	p.stdin.close()

def print_data(data):
	print 'Copy to clipbaord: '
	print '============================'
	print data
	print '============================\n\n'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', port))
s.listen(5)
while 1:
	(clientsocket, address) = s.accept()
	data = read_data(clientsocket)
	copy_to_clipboard(data)
	print_data(data)
