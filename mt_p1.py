from threading import Thread
from time import sleep
n = 10
def odd():
    for i in range(n + 1):
        if i % 2 != 0:
            print(i)
            sleep(2)
def even():
    for i in range(n + 1):
        if i % 2 == 0:
            print(i)
            sleep(1)

t1 = Thread(target=odd)
t2 = Thread(target=even)

t1.start()
t2.start()

t1.join()
t2.join()

print("Done")