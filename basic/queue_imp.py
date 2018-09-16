#queue-first in first out
import collections
queue=collections.deque()

print(queue)
print(type(queue))
queue.append("A")
print(queue)
queue.append("B")
print(queue)
queue.append("C")
print(queue)

res1=queue.popleft()
print(res1)
print(queue)


res2=queue.popleft()
print(res2)
print(queue)

res3=queue.popleft()
print(res3)
print(queue)