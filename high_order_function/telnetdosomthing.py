import telnetlib

def doSomething(IP,user,password,command):
    try:
        telnet = telnetlib.Telnet(IP)
        telnet.set_debuglevel(2)

        rt = telnet.read_until("Login username:".encode("utf-8"))
        telnet.write(user + "\n").encode("utf-8")

        rt = telnet.read_until("Login password:".encode("utf-8"))
        telnet.write(password + "\n").encode("utf-8")

        rt = telnet.read_until(">".encode("utf-8"))
        telnet.write(command + "\n").encode("utf-8")

        rt = telnet.read_until(">".encode("utf-8"))
        telnet.close()
        return True
    except:
        return False

if __name__ == '__main__':
        IP="192.168.254.134"
        user="username"
        pwd="******"
        command="ls"
        doSomething(IP,user,pwd,command)