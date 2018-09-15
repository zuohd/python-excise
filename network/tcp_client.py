import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("192.168.254.135",3000))


while True:
    data=input("please say something  to server:")
    client.send(data.encode("utf-8"))
    info=client.recv(1024)
    print("server reply:",info.decode("utf-8"))