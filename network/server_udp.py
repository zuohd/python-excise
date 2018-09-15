# udp need not to connect and broadcast message

import socket

udpserver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpserver.bind(('192.168.254.135', 3000))
while True:
    data, addr = udpserver.recvfrom(1024)
    print("client said:" + data.decode("utf-8"))
    udpserver.sendto(input("say to client:").encode("utf-8"),addr)