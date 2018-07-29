# import thư viện
import sys
import math

# Nhập vào số int N từ bàn phím
data = int(input('Enter your input:'))

#In ra giá trị từ 0 đến N
if(data >= 2):
	print(2, end = ' ')
	for num in range(3,data,2):

		if all(num%i!=0 for i in range(3,int(math.sqrt(num))+1)):
		# end= ' ' để in theo hàng ngang
			print (num,  end=' ')