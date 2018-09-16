import threading, queue, time, random


# producer
def produce(id, q):
    while True:
        num = random.randint(0, 10000)
        q.put(num)
        print("producer %d make  data %d" % (id, num))
        time.sleep(3)
    q.task_done()


# consumer
def consume(id, q):
    while True:
        item = q.get()
        if item is None:
            break

        time.sleep(2)
        print("consumer %d cost data %d" % (id, item))


if __name__ == '__main__':

    q = queue.Queue()
    for i in range(5):
        threading.Thread(target=produce, args=(i, q)).start()
    for i in range(3):
        threading.Thread(target=consume, args=(i, q)).start()

    print("Main thread end..")