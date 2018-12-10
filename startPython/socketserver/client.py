import socket

obj = socket.socket()
ip_port=('127.0.0.1', 8001)
obj.connect(ip_port)
ret_bytes = obj.recv(1024)
ret_str = str(ret_bytes, encoding="utf-8")
print(ret_str)

while True:
    inp=input("please input content to send:")
    if inp=="q":
        obj.sendall(bytes(inp,encoding="utf-8"))
        break
    else:
        obj.sendall(bytes(inp,encoding="utf-8"))
        print("waitting server side...")
        ret=str(obj.recv(1024),encoding="utf-8")
        print(ret)

obj.close()
