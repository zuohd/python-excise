import socket
import threading

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


server.bind(('192.168.254.135',3000))

server.listen(5)
print("server start successfully...")

def run(sk):
    data = sk.recv(1024)
    print("client said:" + data.decode("utf-8"))
    sendData = "say somthing to client:hi"
    sk.send(sendData.encode("utf-8"))
while True:
    try:
        clientSocket, clientAddress = server.accept()
        print("%s----%s connected" % (str(clientSocket), clientAddress))

        t=threading.Thread(target=run,args=(clientSocket,))
        t.start()
        # data=clientSocket.recv(1024)
        # print("client said:"+data.decode("utf-8"))
        # sendData=input("say somthing to client:")
        # clientSocket.send(sendData.encode("utf-8"))
    except socket.error as e:
        print(e)
