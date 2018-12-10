import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        conn.sendall(bytes("welcome to sign in.", encoding="utf-8"))

        while True:
            print("waitting from client side...")
            ret_bytes = conn.recv(1024)
            ret_str = str(ret_bytes, encoding="utf-8")
            print(ret_str)

            if ret_str == "q":
                break

            inp = input("Please input your content to send client:")
            conn.sendall(bytes(inp, encoding="utf-8"))


if __name__ == '__main__':
    ip_port = ('127.0.0.1', 8001)
    server = socketserver.ThreadingTCPServer(ip_port, MyServer)
    server.serve_forever()
