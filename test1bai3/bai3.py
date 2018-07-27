from random import randint
# sinh ra 1 điểm 
#point la 1 set
points = {(randint(0, 40), randint(0, 40)) }

#khi dưới 1000 điểm
while len(points) < 1000:
	#thêm điểm vào tập hợp points
	#|= là phép thêm vào tập hợp, nếu trùng nó sẽ không ghi vào 
	points |= {(randint(0, 40), randint(0, 40))}
#print(type(points))
#print(points)
file_output = open ('output.txt', 'w', encoding='utf-8')
file_output.write(str(points))