from random import randint
#class tạo point
class Point:
    def __init__(self,x_init,y_init):
        self.x = x_init
        self.y = y_init

    def shift(self, x, y):
        self.x += x
        self.y += y

    def __repr__(self):
        return "".join(["(", str(self.x), ",", str(self.y), ")"])


def check (p, listPoint):
    for s in listPoint:
        if(s.x == p.x and s.y == p.y):
            return False
    return True

listp = []
# khi dưới 5 điểm
while len(listp) < 1000:
	#sinh ra một điểm random 
	p = Point(randint(0, 40), randint(0, 40))
	if(check(p, listp)):
		listp.append(p)
#in ra deltas
file_output = open ('output1.txt', 'w')
file_output.write(str(listp))
