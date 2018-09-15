import socket
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    data=input("input data:")
    client.sendto(data.encode("utf-8"),('192.168.254.135', 3000))
    info=client.recv(1024).decode("utf-8")
    print("server said:"+info)