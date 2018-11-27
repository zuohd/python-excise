import select
import socket

ip_port = ('127.0.0.1', 9999)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)
while True:
    rlist,w,e=select.select([sk,],[],[],1)
    print(rlist)
    for r in rlist:
        print(r)
        if r==sk:
            conn,address=r.accept()
            conn.sendall(bytes('hello',encoding='utf-8'))
        else:
            r.receieve(1024)
