import socket

ip_port = ('127.0.0.1', 9999)
sk = socket.socket()
sk.connect(ip_port)
data=sk.recv(1024)
print(data)

while True:
    inp=input(">>>")
    sk.sendall(bytes(inp,encoding="utf-8"))

sk.close()