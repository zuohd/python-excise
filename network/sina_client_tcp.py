import socket
# actively sending connection side is client
# receieve request side is server

sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #AF_INET is IPV4

sk.connect(("www.sina.com.cn",80)) #parameter is atuple-ip address and port number

sk.send(b'GET / HTTP/1.1\n Host: www.sina.com.cn\n Connection: close\n\n')

data=[]
while True:
    tempData=sk.recv(1024)
    if tempData:
        data.append(tempData)
    else:
        break
dataStr=(b''.join(data)).decode("utf-8")

sk.close()
print(dataStr)




