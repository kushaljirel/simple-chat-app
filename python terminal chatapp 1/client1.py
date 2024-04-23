# import socket module
import socket

# create a socket object
s = socket.socket()

# define a port on which you want to connect
port = 12345

# connect to a server in a local computer
s.connect(('127.0.01', port))

# recieve data from server
print(s.recv(1024))

# close the connection
s.close()
