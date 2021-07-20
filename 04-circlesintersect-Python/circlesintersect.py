# Write the function circlesIntersect(x1, y1, r1, x2, y2, r2) 
# that takes 6 numbers (ints) -- x1, y1, r1, x2, y2, r2 -- 
# that describe the circle centered at (x1,y1) with radius r1, 
# and the circle centered at (x2,y2) with radius r2, and returns True 
# if the two circles intersect and False otherwise.

def fun_circlesintersect(x1, y1, r1, x2, y2, r2):
	distance=((x2-x1)**2+(y2-y1)**2)**0.5
	if distance > (r1+r2):
		return False
	else:
		return True
# print(fun_circlesintersect(5, 6, 14, 8, 7, 9))
# print(fun_circlesintersect(3, 4, 5, 14, 18, 8))
# print(fun_circlesintersect(2, 3, 12, 15, 28, 10))
# print(fun_circlesintersect(-10, 8, 30, 14, -24, 10))
