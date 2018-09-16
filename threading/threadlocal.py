import threading

# used in crawler multiple threading,resource maybe database/http request etc. shared resources
a = 0
local = threading.local()


def run(n):
    local.x = a  # every threading has a local x variant
    for i in range(10000000):
        local.x += n
        local.x -= n


if __name__ == '__main__':
    t1 = threading.Thread(target=run, name="t1", args=(1,))
    t2 = threading.Thread(target=run, name="t2", args=(10,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("a=", a)
