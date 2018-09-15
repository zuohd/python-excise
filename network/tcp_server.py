import socket

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


server.bind(('192.168.254.135',3000))

server.listen(5)
print("server start successfully...")
clientSocket, clientAddress = server.accept()
print("%s----%s connected"%(str(clientSocket),clientAddress))

while True:
    try:
        data=clientSocket.recv(1024)
        print("client said:"+data.decode("utf-8"))
        sendData=input("say somthing to client:")
        clientSocket.send(sendData.encode("utf-8"))
    except socket.error as e:
        print(e)
