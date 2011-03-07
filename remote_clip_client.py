#!/usr/bin/env python
import sys
import socket

port = 43516
eof = '\0'
# read from stdin
data = sys.stdin.read()
# send it to a socket port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', port))
sent = s.send(data + eof)
s.close()
