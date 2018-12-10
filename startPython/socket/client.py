import socket
import os

ip_port = ('127.0.0.1', 9999)
obj = socket.socket()
obj.connect(ip_port)
size = os.stat("old_file.txt").st_size
obj.sendall(bytes(str(size), encoding="utf-8"))
obj.recv(1024)
with open("old_file.txt", "rb") as f:
    for line in f:
        obj.sendall(line)

obj.close()
