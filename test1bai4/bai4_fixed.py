import threading
# tạo một class con 
lock = threading.RLock()
result = 0 
class SummingThread(threading.Thread):
	#init thực hiện trước, selt là con trỏ this trong java
	def __init__(self,low,high,lock):
		#super gọi đến hàm parent của nó
		super(SummingThread, self).__init__()
		self.low=low
		self.high=high
		self.lock=lock
		
	def run(self):
		global result 
		for i in range(self.low,self.high):
			lock.acquire()
			result+=i
			lock.release()

threads = []
data = int(input('Enter your input:'))

thread1 = SummingThread(0,round(data/2)+1,lock)
thread2 = SummingThread(round(data/2)+1,data+1,lock)

threads.append(thread1)
threads.append(thread2)

for t in threads:
	t.start()

for t in threads:
    t.join()

print(result)
