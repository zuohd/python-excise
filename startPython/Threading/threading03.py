import threading
import time


def print_time(string):
    print("task ", string)
    time.sleep(2)


start_time = time.time()
t_list = []
for i in range(50):
    t = threading.Thread(target=print_time, args=('t={0}'.format(i),))
    t.start()
    t_list.append(t)
for t in t_list:
    t.join()
print(time.time() - start_time)
