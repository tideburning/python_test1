import threading
# tạo một class con 
class SummingThread(threading.Thread):
	#init thực hiện trước, selt là con trỏ this trong java
	def __init__(self,low,high):
		#super gọi đến hàm parent của nó
		super(SummingThread, self).__init__()
		self.low=low
		self.high=high
		self.total=0
	def run(self):
		for i in range(self.low,self.high):
			self.total+=i

data = int(input('Enter your input:'))

thread1 = SummingThread(0,round(data/2)+1)
thread2 = SummingThread(round(data/2)+1,data)
#Run the thread
thread1.start() # This actually causes the thread to run
thread2.start()
#waits until the thread has completed
thread1.join()  
thread2.join()
print(thread1.total)
print(thread2.total)
result = thread1.total + thread2.total
print (result)