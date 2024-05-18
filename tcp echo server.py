import socket
s=socket(Af_INET,SOCK_STREAM)
s.bind(("",8000))
s.listen(5)
with open( ) as file:
    data=file.read()
c,a=s.accept()
c.send(data.encode('utf-8'))
c.close()

