import threading
import time

ls = []

def count(n):
	for i in range(1,n+1):
		ls.append(i)
		time.sleep(0.01)

def count2(n):
	for i in range(1,n+1):
		ls.append(i)
		time.sleep(0.02)

# for _ in range(2):
x = threading.Thread(target = count,args=(5,))
x.start()

y = threading.Thread(target = count2,args=(5,))
y.start()
# time.sleep(0.01)

x.join()
y.join()

print(ls)