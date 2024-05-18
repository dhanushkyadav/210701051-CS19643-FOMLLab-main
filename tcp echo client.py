import socket
s=socket.socket()
s.connect(("127.0.0.1",5000))

data=s.recv(100).decode()
print(data)
file=open( )
file.write(data)
s.close()