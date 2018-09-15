import time

f = open("testfile.txt", "w")

# 1.write information into buffer
# f.flush()

while True:
    time.sleep(3)
    f.write("soderberg is  a good man\n")
    f.flush()  # refresh buffer
    pass
f.close()
